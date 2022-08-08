import time
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from math import sqrt
from skimage import filters, morphology, segmentation

st = time.time()
INPUT_FILE = "./raw_t1_subject_02.nii.gz"

image = nib.load(INPUT_FILE).get_fdata()
final_image = np.full((256,256,256),0, dtype = float)

for z in [84,128]:
    sst = time.time()
    im00 = image[:,z,:]

    # Generating mask to remove skull
    im01 = morphology.convex_hull_image(np.logical_and(im00 > 100, im00 < 111))
    # plt.imshow(im00)
    # plt.show()
    im02 = segmentation.expand_labels(im01, distance= 6)

    im03 = np.full((256,256),0,dtype=float)
    for i in range(256):
        for j in range(256):
            x = im02[i][j]
            if x:
                im03[i][j] = image[i][z][j]

    im04 = im03 > 87 #White Matter
    im05 = im03 < 51 #Dark Matter(Grey Matter)
    im06 = filters.median(im04)
    im07 = morphology.binary_dilation(im06)
    im08 = filters.median(im05)
    im09 = morphology.binary_dilation(im08)
    im10 = im07 ^ im06 #Whitematter boundary
    im11 = im09 ^ im08 #Darkmatter boundary
    # im12 = im10 | im11 #White and Dark matter boundary combined

    # im12 = segmentation.flood_fill(im04, (110,z),True)
    # plt.imshow(im03, cmap=plt.cm.gray)
    # plt.show()

    # plt.figure()
    # plt.imshow(im10)
    # plt.show()
    # plt.figure()
    # plt.imshow(im11)
    # plt.show()


    im12 = np.logical_not(im06) #Inverse White Matter(Median Filtered)
    im13 = np.logical_not(im08) #Inverse Dark(Grey Matter) Matter(Median Filtered)
    im14 = filters.median(im12 & im13) # Cortical Map(Filtered)
    # plt.figure()
    # plt.imshow(im14)
    # plt.draw()

    # plt.figure("RAW")
    # plt.imshow(im03)
    # plt.show()


    ## Filling the White Matter boundary points with the closest distance of Dark matter(Grey Matter) point
    im15 = np.full((256,256),0,dtype=float)
    for i1 in range(256):
        for j1 in range(256):
            x = im10[i1][j1]
            if x:
                min_dis = float('inf')
                # px = py = -1
                for i2 in range(256):
                    for j2 in range(256):
                        y = im11[i2][j2]
                        if y:
                            dis = sqrt((i2 - i1)**2 + (j2-j1)**2)
                            if dis < min_dis:
                                min_dis = dis
                                # px = i2
                                # py = j2
                im15[i1][j1] = min_dis #if min_dis < 5.1 else 0
                # if min_dis > 5:
                #     im15[px][py] += 1
                # im15[px][py] = 1

    # plt.figure().suptitle("WM | DM")
    # plt.imshow(im15)
    # plt.draw()

    # Filling the thickness value in the Cortical Map
    # im16 = np.full((256,256),0,dtype=float)
    for i1 in range(256):
        for j1 in range(256):
            x = im14[i1][j1]
            if x:
                min_dis = float('inf')
                val = 0 # Closest value of White matter boundary point
                for i2 in range(256):
                    for j2 in range(256):
                        y = im15[i2][j2]
                        if y > 0:
                            dis = sqrt((i2 - i1)**2 + (j2-j1)**2)
                            if dis < min_dis:
                                min_dis = dis
                                val = y
                # im16[i1][j1] = val if val <= 5 else 0
                final_image[i1][z][j1] = val if val <= 5 else 0 #Ignoring the error values

    # plt.figure().suptitle("Final")
    # plt.imshow(im16)
    # plt.draw()

    # plt.show()
    print("Rendered z: ", z)
    pst = time.time() - sst 
    print('Execution time:', pst, ' secs')

et = time.time() - st
print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(et)))

# plt.figure().suptitle("Slice z = 64")
# plt.imshow(final_image[:,64,:])
# plt.draw()
# plt.figure().suptitle("Slice z = 128 [:,128,:]")
# plt.imshow(final_image[:,128,:])
# plt.draw()
# plt.figure().suptitle("Slice z = 192")
# plt.imshow(final_image[:,192,:])
# plt.draw()
# plt.show()
final_image = nib.Nifti1Image(final_image, None)
nib.save(final_image, "./final_thickness_map_fast.nii.gz")
