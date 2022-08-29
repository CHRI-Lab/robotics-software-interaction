#!/usr/bin/env python
# coding: utf-8

# In[1]:


import jupyros as jr
import rospy
import sys
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from IPython.display import display, Image
import ipywidgets as widgets
import threading
import cv2


# In[2]:


# Stop button
# ================
stopButton = widgets.ToggleButton(
    value=False,
    description='Stop',
    disabled=False,
    button_style='danger', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Description',
    icon='square' # (FontAwesome names without the `fa-` prefix)
)

global image

# Display function
# ================
def view(button):
    cap = cv2.VideoCapture(0)
    display_handle=display(None, display_id=True)
    i = 0
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1) # if your camera reverses your image
        _, frame = cv2.imencode('.jpeg', frame)
        display_handle.update(Image(data=frame.tobytes()))
        if stopButton.value==True:
            cap.release()
            display_handle.update(None)
        image = frame

            
# Run
# ================
display(stopButton)
thread = threading.Thread(target=view, args=(stopButton,))
thread.start()


# In[3]:



cv_image = image
ros, cols , channels = cv_image.shape
cv2.circle(cv_image, (cols/2,ros/2), 50, (0,0,255), -1)
image_pub.publish(bridge.cv2_to_imgmsg(cv_image,"brg8"))

rospy.init_node('image_processing')
bridge = CvBridge()
image_pub = rospy.Publisher("processed_image", Image)

while not rospy.is_shutdown():
    rospy.spin()


# In[ ]:




