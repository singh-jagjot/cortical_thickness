import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import cv2
from skimage import filters
from skimage import morphology

img = nib.load("./raw_t1_subject_02.nii.gz").get_fdata()

gm_img = np.ndarray(shape = (256,256,256), dtype=float)

for i in range(256):
    for j in range(256):
        for k in range(256):
            x = img[i][j][k]
            if x <= 40:
                gm_img[i,j,k] =  x

mgm_img = filters.median(gm_img)

for i in range(256):
    for j in range(256):
        for k in range(256):
            x = mgm_img[i][j][k]
            if x > 0:
                mgm_img[i,j,k] =  1

dilgm = morphology.binary_dilation(mgm_img)
b_gm = dilgm - mgm_img
plt.imshow(b_gm[:,128,:]);
plt.show()

# for i in range(256):
#     for j in range(256):
#         for k in range(256):
#             x = img[i][j][k]
#             if x > 77:
#                 wm_img[i,j,k] = x
