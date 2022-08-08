from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
# from nipype.interfaces.fsl import BET
from skimage import filters, morphology, segmentation

INPUT_FILE = "./raw_t1_subject_01.nii.gz"
# OUT_SUKULLSTRIPPED = "./skull_stripped.nii.gz"

# skullstrip = BET(in_file = INPUT_FILE, out_file = OUT_SUKULLSTRIPPED, output_type='NIFTI_GZ')
# skullstrip.inputs.in_file = INPUT_FILE
# skullstrip.inputs.out_file = OUT_SUKULLSTRIPPED
# skullstrip.run()

image = nib.load(INPUT_FILE).get_fdata()
im0 = image[:,128,:]
im1 = im0 > 82
im2 = im0 < 51
im3 = filters.median(im1)
im4 = morphology.binary_dilation(im3)
im5 = filters.median(im2)
im6 = morphology.binary_dilation(im5)
im7 = im3 ^ im4 #Whitematter boundary
im8 = im5 ^ im6 #Darkmatter boundary
im9 = im7 | im8 #White and Dark matter boundary combined

# Generating mask to remove skull
im10 = morphology.convex_hull_image(im0 > 100)
im11 = segmentation.expand_labels(im10, distance= 6)

# plt.imshow(morphology.binary_dilation(im7))
# plt.show()
# plt.imshow(im11)
# plt.show()
# plt.imshow(filters.median(im4))
# plt.show()
im13 = np.full((256,256),0,dtype=float)
for i in range(256):
    for j in range(256):
        x = im11[i][j]
        if x:
            im13[i][j] = image[i][128][j]

plt.imshow(filters.median(np.logical_and(im13 < 83, im13 >50)))
plt.show()

# figure, axis = plt.subplots(1, 3)
# figure.suptitle("All")
# axis[0].imshow(image[:,128,:])
# axis[0].set_title("RAW")
# axis[1].imshow(im10)
# axis[1].set_title("WM B")
# axis[2].imshow(im8)
# axis[2].set_title("DM B")
# # axis[3].imshow(im9)
# # axis[3].set_title("WM & DM")
# plt.draw()

# im8 = np.full((256,256),0,dtype=float)

# for i1 in range(256):
#     for j1 in range(256):
#         x = im7[i1][j1]
#         if x:
#             min_dis = float('inf')
#             px = py = -1
#             for i2 in range(256):
#                 for j2 in range(256):
#                     y = im8[i2][j2]
#                     if y:
#                         d = sqrt((i2 - i1)**2 + (j2-j1)**2)
#                         if d < min_dis:
#                             min_dis = d
#                             px = i2
#                             py = j2
            
#             # im8[i1][j1] = 1
#             im8[px][py] = 1

# plt.figure().suptitle("WM | DM")
# plt.imshow(im8)
# plt.draw()
plt.show()