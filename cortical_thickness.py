from math import inf
from time import sleep
from typing import List
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from skimage import filters
from skimage import morphology

img = nib.load("./raw_t1_subject_02.nii.gz").get_fdata()
# plt.imshow(t1[:,128,:])
# plt.show()

wm_img = np.ndarray(shape = (256,256,256), dtype=float)
gm_img = np.ndarray(shape = (256,256,256), dtype=float)
srwm_img = np.ndarray(shape = (256,256,256), dtype=float)


for i in range(256):
    for j in range(256):
        for k in range(256):
            x = img[i][j][k]
            if x > 100:
                srwm_img[i,j,k] = 1
            if x > 77:
                wm_img[i,j,k] = 1
            if x <= 40:
                gm_img[i,j,k] = 1

# plt.imshow(srwm_img[:,128,:])
# plt.show()
# wm_skull_rmd = np.ndarray(shape = (256,256,256), dtype=float)

# Required
# for i in range(256):
#     for j in range(256):
#         for k in range(256):
#             x = mwm_img[i][j][k]
#             y = mgm_img[i][j][k]
#             if x > 0:
#                 mwm_img[i,j,k] = 1
#             if y > 0:
#                 mgm_img[i,j,k] = 1
            
# plt.imshow(wm_skull_rmd[:,128,:])
# plt.show()
# dwm_img = morphology.binary_dilation(mwm_img)
# # dwm_img = morphology.binary_dilation(dwm_img)
# # dwm_img = morphology.binary_dilation(dwm_img)
# # dwm_img = morphology.binary_dilation(dwm_img)
# dgm_img = morphology.binary_dilation(mgm_img)
# bwm_img = dwm_img - mwm_img
# bgm_img = dgm_img - mgm_img
# mwm_img = filters.median(wm_img)
# mgm_img = filters.median(gm_img)
# msrwm_img = filters.median(srwm_img)
# plt.imshow(msrwm_img[:,128,:])
# plt.show()
# dwm_img = morphology.binary_dilation(mwm_img)
dsrwm_img = morphology.binary_dilation(srwm_img)
print("Dilation loop: Start")
for i in range(9):
    dsrwm_img = morphology.binary_dilation(dsrwm_img)

print("Dilation loop: End")
dgm_img = morphology.binary_dilation(gm_img)
sr_img = np.ndarray(shape = (256,256,256), dtype=float)

# plt.imshow(dsrwm_img[:,128,:])
# plt.show()
for i in range(256):
    for j in range(256):
        for k in range(256):
            x = dsrwm_img[i][j][k]
            if x > 0:
                sr_img[i][j][k] = img[i][j][k]
                # if y > 56 and y < 
plt.imshow(sr_img[:,128,:])
plt.show()
# bsrwm_img = dsrwm_img - msrwm_img
# bwm_img = dwm_img - mwm_img
# bgm_img = dgm_img - gm_img
# skull_img = np.ndarray(shape = (256,256,256), dtype=float)
# for i in range(256):
#     for j in range(256):
#         for k in range(256):
#             x = bwm_img[i][j][k] - bsrwm_img[i][j][k]
#             if x == 1:
#                 skull_img[i][j][k] = 1

# def isBounPt(x,z,y, img) -> bool:
#     if img[x+1,z,y] == 0:
#         return True
#     elif img[x-1,z,y] == 0:
#         return True
#     elif img[x,z,y+1] == 0:
#         return True
#     elif img[x,z,y-1] == 0:
#         return True
#     return False

# print("Making List: Start")
# wml = []
# gml = []
# for i in range(256):
#     for j in range(256):
#         for k in range(256):
#             wmp = bwm_img[i][j][k]
#             gmp = bgm_img[i][j][k]
#             if wmp > 0:
#                 wml.append([i,j,k])
#             if gmp > 0:
#                 gml.append([i,j,k])
# print("Making List: End")

# print("WML Size: ",len(wml)," GML Size: ", len(gml))

# print("Finding Closest: Start")
# cgmpl = []
# for i in wml:
    
#     cgmpl.append(closest)
# print("Finding Closest: End")
# print("Making closest img: Start")
# cgm_img = np.ndarray(shape = (256,256,256), dtype=float)
# for i in cgmpl:
#     cgm_img[i[0]][i[1]][i[2]] = 1
# print("Making closest img: End")





# figure, axis = plt.subplots(1,3)
# axis[0].imshow(bwm_img[:,128,:])
# axis[0].set_title("WM Boun")
# axis[1].imshow(bgm_img[:,128,:])
# axis[1].set_title("GM Boun")
# # axis[2].imshow(bsrsw_img[:,128,:])
# # axis[2].set_title("With Skull")
# axis[2].imshow(bwm_img[:,128,:] - skull_img[:,128,:])
# axis[2].set_title("Without Skull")
# plt.show()

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