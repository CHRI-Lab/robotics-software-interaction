# 2. ROS and Nao/Emika/Miro

```{admonition} Note
Page underconstruction
```

## ROS

ROS is not an Operating systems
It is:

- a faily simple peer to peer message passing system
- a multi-processes management systems
- an API to this system (Python, C++,  and others)
- A set of message types that can be designed by the developper and can be used to facilitate communication between miules
- a set of convention to write packages
- a set of tools and libraries useful for robotics (OpenCV, tf, MoveIt...)
- a set of visualisation and simulation tools
- a community 


## ROS Basics

Nodes

Topics

Show graph and show a simple code, init node, sub pub
spin

see notebook to run a first image processing module
 read image, drw red cercle


### ervices
blocking, synchonous, so not good for long proceeses


### ROSCORE

### ROS MSG
Topics are TCP ports on which data is exchenged
data is serialized using specific format
data types = messages

See several types of messages

Pose
Joint state
Image

Message content

Echo a topic to see the content of the image_raw otopics

