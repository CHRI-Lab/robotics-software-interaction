# 8. Robot software architecture and programming

Goal: Complete desired tasks while monitoring and reacting
to unexpected situations. Handle inputs and outputs (control/perception) from actuators
and sensors in real-time2 and under uncertainty.

## behavioural (reactive) control

sense-act

subsume / orvewrite behaviour

example Braintenberg machines

non-linear control functions -> complex behaviours


### combining behaviours

- Follow a human
    sensor: camera ; behavious follow human seen in camera
- avoid obstacle
    bumpers - move away from wall
- wander
    ecnoders - move forward and turn

Which one should have the priority?

#### Subsumption oprtator

### Subsumption architecture

### summary on behaviroual control

- strenghts
- weeknesses

###  event oriented programming

## deliberative architecture 

### sense-plan-act architecture

### task planning

HTN

primitive action

### Three-tiered Architecture

This architecture contains a planning, an executive, and a behavioral
control level that are hierarchically linked.

1. Planning: this layer is at the highest-level, and focuses on task-planning for
long-term goals.
2. Executive: the executive layer is the middle layer connecting the planner and
the behavioral control layers. The executive specifies priorities for the behav-
ioral layer to accomplish a specific task. While the task may come directly
from the planning layer, the executive can also split higher-level tasks into
sub-tasks.
3. Behavioral control: at the lowest-level. the behavioral control layer handles
the implementation of low-level behaviors and is the interface to the robot’s
actuators and sensors.

The primary advantage of this architecture is that it combines benefits of the
behavioral-based subsumption architecture (i.e. reactive planning) with better
long-term planning capabilities (i.e. resulting from the planning level). Each of
these levels will now be discussed in slightly further detail, however in practice
the division among these levels is often quite blurred!


##  Client-Server vs Publish-Subscribe

