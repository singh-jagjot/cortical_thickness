import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from skimage import filters
from skimage import morphology

# plt.figure()
t1 = nib.load("./thickness_map_subject_01.nii.gz").get_fdata()
# plt.imshow(t1[:,128,:])
# plt.show()

t2 = nib.load("./raw_t1_subject_01.nii.gz").get_fdata()
# plt.imshow(t2[:,128,:])
# plt.show()
t3 = nib.load("./raw_t1_subject_02.nii.gz").get_fdata()
plt.imshow(t3[:,128,:])
plt.show()

# figure, axis = plt.subplots(1,3)
# axis[0].imshow(t2[:,128,:])
# axis[0].set_title("Raw")
# axis[1].imshow(t1[:,128,:])
# axis[1].set_title("Exp")
# axis[2].imshow(t3[:,128,:])
# axis[2].set_title("My")
# plt.show()
# wm = np.ndarray(shape = (256,256,256), dtype=float)

# for i in range(256):
#     for j in range(256):
#         for k in range(256):
#             x = t1[i][j][k]
#             if x > 100:
#                 wm[i,j,k] = 1
#             else:
#                 wm[i,j,k] = 0

# # plt.imshow(wm[:,128,:])
# # plt.show()

# # med_wm = filters.median(wm)
# # dil = morphology.binary_dilation(wm)
# # plt.imshow(dil[:,128,:] - wm[:,128,:])
# # plt.show()

# ctwm = np.ndarray(shape = (256,256,256), dtype=float)

# for i in range(256):
#     for j in range(256):
#         for k in range(256):
#             x = t1[i][j][k]
#             if x > 60:
#                 ctwm[i,j,k] = 1
#             else:
#                 ctwm[i,j,k] = 0

# # plt.imshow(ctwm[:,128,:])
# # plt.show()

# plt.imshow(ctwm[:,128,:] - wm[:,128,:])
# plt.show()