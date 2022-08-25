#!/usr/bin/env python
# coding: utf-8

# In[1]:


import jupyros as jr
import rospy
from std_msgs.msg import String

rospy.init_node('jupyter_node')
jr.subscribe('/sometopic', String, lambda msg: print(msg))


# In[2]:


import sys
sys.path.append('/opt/ros/melodic/lib/python2.7/dist-packages/')

# The next line should now work!
import jupyros


# In[ ]:




