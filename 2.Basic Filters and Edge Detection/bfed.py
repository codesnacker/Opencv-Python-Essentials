
# coding: utf-8

# In[1]:


#Author: Arun
#Site  : https://codesnacker.com
#Please support me by subscribing to my blog for more content


# In[2]:


#Basic Filter , edge detection
import numpy as np
import matplotlib.pyplot as plt
import cv2


# In[9]:


#read in image
image = cv2.imread('images/tower.jpg')
#make a copy
imcopy = np.copy(image)
#BGR to RGB channels
imcopy = cv2.cvtColor(imcopy,cv2.COLOR_BGR2RGB)

plt.imshow(imcopy)


# In[18]:


#convert to gray 
grayimage = cv2.cvtColor(imcopy ,cv2.COLOR_RGB2GRAY)
#The resulting image is a grayscale image. imshow uses by default, a kind of heatmap  to display the image intensities. Just specify the gryascale colormap as shown below:
plt.imshow(grayimage,cmap = 'gray')

#a basic filter , we are looking for changes in horizontal direction ie. vertical lines in image 
#also called a sobel filter


# In[20]:



kernel_sobel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

filtered_image = cv2.filter2D(grayimage,-1,kernel_sobel)

plt.imshow(filtered_image,cmap = 'gray')
# a -1 param means op image is same type as input


# In[33]:


x = cv2.threshold(filtered_image,220,255,cv2.THRESH_BINARY)
#thresholdinf to remove bogus dots


# In[34]:


plt.imshow(x[1],cmap='gray')
# threshold returns 2 values , x[0] is optimum value as per otsu's threshold.(see next tuts) x[1] is the image

