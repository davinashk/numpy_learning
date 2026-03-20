import numpy as np # Imports NumPy
from skimage import data # Getting the image
import matplotlib.pyplot as plt # Showing the image


camera = data.camera()
plt.imshow(camera)

plt.show()


rows,cols = camera.shape

print(rows)
print(cols)

img_centre=camera[int(rows*0.25):int(rows*0.75),int(cols*0.25):int(cols*0.75)]

#print(img_centre.shape)

plt.imshow(img_centre)

plt.show()


img_black=camera[int(rows*0.25):int(rows*0.75),int(cols*0.25):int(cols*0.75)]

#print(img_centre.shape)

plt.imshow(img_black)

plt.show()