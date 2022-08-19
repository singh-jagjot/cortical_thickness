import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from math import sqrt
from skimage import filters, morphology

#Loading the image file
raw = nib.load("./raw_t1_subject_02.nii.gz").get_data()


wm = raw > 95
dm = raw < 40

# plt.imshow(dm[:,128,:])
# plt.show()

wmf = filters.median(wm)
wmd = morphology.binary_dilation(wmf)
# plt.imshow(wmd[:,138,:])
# plt.show()
raw2  = np.full((256,256,256), 0, dtype=float)
mask = wmd
# print(mask.shape)
for _ in range(6):
    mask = morphology.binary_dilation(mask)

wwm = np.full((256,256,256), False, dtype=bool)
ddm = np.full((256,256,256), False, dtype=bool)
seg = np.full((256,256,256), 0, dtype=float)

for z in range(256):    
    for x in range(256):
        for y in range(256):
            m =  mask[x][z][y]
            if m:
                val = raw[x][z][y]
                raw2[x][z][y] = val
                if val > 90:
                    wwm[x][z][y] = True
                if val >= 50:
                    ddm[x][z][y] = True
                if val >=50 and val <=90:
                    seg[x][z][y] = val
    


# plt.imshow(filters.median(wwm[:,128,:]))
# plt.draw()
# plt.figure()
# plt.imshow(filters.median(ddm[:,128,:]))
# plt.draw()
# plt.figure()
# plt.imshow(filters.median(seg[:,128,:]))
# plt.draw()
# plt.show()

wwmf = filters.median(wwm)
ddmf = filters.median(ddm)
seg = filters.median(seg)
wwmd = morphology.binary_dilation(wwmf)
ddmd = morphology.binary_dilation(ddmf)
wmb = wwmd ^ wwmf
dmb = ddmd ^ ddmf

# plt.figure()
# plt.imshow(wmb[:,128,:])
# plt.draw()
# plt.figure()
# plt.imshow(dmb[:,128,:])
# plt.draw()
# plt.figure()
# plt.imshow(seg[:,128,:])
# plt.draw()
# plt.show()

dis_map = np.full((256,256,256), 0, dtype=float)
thickness_map = np.full((256,256,256), 0, dtype=float)

for z in range(256):
    for x in range(256):
        for y in range(256):
            if wmb[x][z][y]:
                min_dis = float('inf')
                for x2 in range(256):
                    for y2 in range(256):
                        if dmb[x2][z][y2]:
                            distance =  sqrt((x2 - x)**2 + (y2-y)**2)
                            if distance < min_dis:
                                min_dis = distance
                dis_map[x][z][y] = min_dis
    for x in range(256):
        for y in range(256):
            if seg[x][z][y] > 0:
                min_dis = float('inf')
                boundary_distance_value = 0
                for x2 in range(256):
                    for y2 in range(256):
                        if dis_map[x2][z][y2] > 0:
                            distance =  sqrt((x2 - x)**2 + (y2-y)**2)
                            if distance < min_dis:
                                min_dis = distance
                                boundary_distance_value = dis_map[x2][z][y2]
                if boundary_distance_value < 5.5:
                    thickness_map[x][z][y] = boundary_distance_value
                else:
                    thickness_map[x][z][y] = 5.5
    print("Rendered: ", z)

# plt.imshow(thickness_map[:,128,:])
# plt.draw()
# plt.show()
fi = nib.Nifti1Image(thickness_map, None)
nib.save(fi, "./final_thickness_map_kabir.nii.gz")