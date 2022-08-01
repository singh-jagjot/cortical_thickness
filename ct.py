import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from skimage import filters
from skimage import morphology

img = nib.load("./raw_t1_subject_02.nii.gz").get_fdata()
# plt.imshow(img[:,128,:])
# plt.show()
wm_img = np.ndarray(shape = (256,256,256), dtype=float)
gm_img = np.ndarray(shape = (256,256,256), dtype=float)
srwm_img = np.ndarray(shape = (256,256,256), dtype=float)

for i in range(256):
    j = 128
    for k in range(256):
        x = img[i][j][k]
        if x > 100:
            srwm_img[i,j,k] = x
        if x > 77:
            wm_img[i,j,k] = x
        if x <= 40:
            gm_img[i,j,k] = x

plt.imshow(wm_img[:,128,:])
plt.show()
# plt.imshow(gm_img[:,128,:])
# plt.show()
# plt.imshow(srwm_img[:,128,:])
# plt.show()
# dsrwm_img = morphology.binary_dilation(srwm_img)
mwm_img = filters.median(wm_img)
mgm_img = filters.median(gm_img)
msrwm_img = filters.median(srwm_img)
plt.imshow(mwm_img[:,128,:])
plt.show()
# plt.imshow(mgm_img[:,128,:])
# plt.show()
# plt.imshow(msrwm_img[:,128,:])
# plt.show()

# dwm_img = np.ndarray(shape = (256,256,256), dtype=float)
# dgm_img = np.ndarray(shape = (256,256,256), dtype=float)
# dsrwm_img = np.ndarray(shape = (256,256,256), dtype=float)

# for i in range(256):
#     j = 128
#     for k in range(256):
#         x = mwm_img[i][j][k]
#         y = mgm_img[i][j][k]
#         z = msr_img[i][j][k]
#         if x > 0:
#             dwm_img[i][j][k] = 1
#         if y > 0:
#             dgm_img[i][j][k] = 1
#         if z > 0:
#             dsrwm_img[i][j][k] = 1


# print("Dilation loop: Start")
# dwm_img = morphology.binary_dilation(dwm_img)
# dgm_img = morphology.binary_dilation(dgm_img)
# dsrwm_img = morphology.binary_dilation(dsrwm_img)

# # plt.imshow(dwm_img[:,128,:])
# # plt.show()
# # plt.imshow(dgm_img[:,128,:])
# # plt.show()
# # plt.imshow(dsrwm_img[:,128,:])
# # plt.show()
# for i in range(12):
#     dsrwm_img = morphology.binary_dilation(dsrwm_img)

# print("Dilation loop: End")
# sr_img = np.ndarray(shape = (256,256,256), dtype=float)
# for i in range(256):
#     j = 128
#     for k in range(256):
#         x = dsrwm_img[i][j][k]
#         if x > 0:
#             sr_img[i][j][k] = img[i][j][k]
# plt.imshow(sr_img[:,128,:])
# plt.show()