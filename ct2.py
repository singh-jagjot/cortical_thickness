from tabnanny import verbose
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from skimage import filters
from skimage import morphology

image = nib.load("./raw_t1_subject_02.nii.gz").get_fdata()
# i = image[:,128,:] > 105
# i2 = image[:,128,:] < 30
# # plt.imshow(i2)
# # plt.show()

# im2 = filters.median(i)
# im3 = morphology.binary_dilation(im2)
# im4 = im3 ^ im2 #Whitematter boundary
# im5 = morphology.binary_dilation(im3)
# for x in range(12):
#     im5 = morphology.binary_dilation(im5)
# # im5 = 
# # plt.imshow(im5)
# # plt.show()
# im6 = np.ndarray(shape = (256,256,256), dtype=float)
# for i in range(256):
#     for j in range(256):
#         x = im5[i][j]
#         y = image[i][128][j]
#         if x == 1:
#             im6[i][128][j] = y

# im7 = np.ndarray(shape = (256,256,256), dtype=float)
# for i in range(256):
#     for j in range(256):
#         x = im2[i][j]
        


figure, axis = plt.subplots(1,3)
axis[0].imshow(image[:,128,:])
axis[0].set_title("Raw")
# axis[1].imshow(image[:,128,:] > 95)
# axis[1].set_title("dia")
axis[2].imshow(image[:,128,:] < 50)
axis[2].set_title("un")
iii = image[:,128,:] > 95
jjj = image[:,128,:] < 26
im8 = np.ndarray(shape=(256,256,256), dtype=float)
for i in range(256):
    for j in range(256):
        x = image[i][128][j]
        if x < 85 and x >48:
            im8[i][128][j] = image[i][128][j]


i  =image[:,128,:] > 0
axis[1].imshow(filters.median(im8[:,128,:]))
axis[1].set_title("un")
plt.show()

# fig, ax = filters.try_all_threshold(image[:,128,:],figsize=(15, 12),verbose=False)
# plt.show()
# plt.imshow(filters.median(image[:,128,:] >79))
# plt.show()