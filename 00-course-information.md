# Course Information

## COURSE OBJECTIVES  

The main goal of this course is to open up new career options in robotics for computer science and engineering students. To that end, the course will teach you the basics of robotics and give you implementation experience. You will learn to use libraries and tools within the most popular robot programming framework [ROS](Robot Operating System). We will touch on robot motion, navigation, perception, planning, and interaction through mini-lectures, labs and assignments, eventually integrating these components to create autonomous or semi-autonomous robotic functionalities. The project will give you team-work experience with large scale software integration and it will get you thinking about opportunities for using robots to make people's lives easier. At the end of the quarter students are expected to:  

- Understand basics of robot navigation, perception, planning, interaction; have a sense of challenging problems in robotics  
- Know how to use important tools in ROS, be able to contribute to ROS, have awareness of available packages in ROS  
- Be comfortable operating a robot platform, have experience using ROS tools to control a robot platform  
- Understand the importance of interface design and robustness of functionalities in robotics  
- Intergate human-centered design in a robotics solution
- Be prepared to interview for a robotics job  

## PROJECT: THE NEXT ROBOTICS START-UP  

This is a great time to start a software robotics company: the basic technology has matured, early companies are gaining traction, the public is receptive, and the investors want a piece of it. The last few years have witnessed an amazing growth in robotics investments. A new robotics startup company pops up almost every week.  

A good portion of these companies are *robotics applications* companies (as opposed to *robotics technology* companies). They take existing robotic capabilities (perhaps improve or customize them a little bit) and integrate them in a way that solves a real need or exploits a proven market. Many of these companies are involve applications of mobile robots (e.g. [Savioke](http://www.google.com/url?q=http%3A%2F%2Fwww.savioke.com%2F&sa=D&sntz=1&usg=AOvVaw3bwRnKy54PTVThkEOqBCDd), [Cobalt](https://www.google.com/url?q=https%3A%2F%2Fwww.cobaltrobotics.com%2F&sa=D&sntz=1&usg=AOvVaw2vMgEJp9Gh2PNGr_3sOQcP), [Simbe](http://www.google.com/url?q=http%3A%2F%2Fwww.simberobotics.com%2F&sa=D&sntz=1&usg=AOvVaw0E8df-WO1bb1FUzvNpMJir)) or social robots (e.g. [Jibo](https://www.google.com/url?q=https%3A%2F%2Fwww.jibo.com%2F&sa=D&sntz=1&usg=AOvVaw3lOkp4hAq_0XbnAO7g6eLp), [Aido](http://www.google.com/url?q=http%3A%2F%2Fwww.aidorobot.com%2F&sa=D&sntz=1&usg=AOvVaw3Bg7fHBkskk_eGxQeelMGQ), [Kuri](https://www.google.com/url?q=https%3A%2F%2Fwww.heykuri.com&sa=D&sntz=1&usg=AOvVaw1rK2my2H-2aIgdh8BZnxxI)).  

You will do the same in your projects, but for **mobile manipulator robots.** You will find a viable application of mobile manipulators and you will develop an early prototype of something that could eventually become a product. While there has been great progress on making mobile manipulators capable, they are still far from having *general-purpose* functionalities, such as the ability to detect and grasp any type of object. Instead, your projects should scope down the robot's task to a smaller set of objects to be manipulated and take advantage of the task structure to develop *special-purpose* manipulation capabilities. We highly encourage *structuring the robot's task environment* to enable functionalities that might not be possible in environments that are structured for humans.  

What tools and resources are available to you?  

- We will have an Ubuntu desktop for each team  
- We will have one Fetch mobile manipulator robot for teams to share  
- You can request an Android tablet and/or a mobile smartphone that can be attached to the robot or used for controlling the robot  
- You can request Arduino or Raspberry Pi kits  
- You can request servo motors, LEDs, or other actuators  
- You will have access to the CoMotion Makerspace for 3D printing, laser cutting, and other tools; you can request fabrication materials  
- You can request additional sensors or peripherals for the robot  
- You can request special controllers or wearables  
- You can request home automation tools  
- You can request furniture related to the robot's functionality  

We will mainly support software development within [ROS](http://www.google.com/url?q=http%3A%2F%2Fwww.ros.org%2F&sa=D&sntz=1&usg=AOvVaw1ZwFFpaXeI8T-3VZPIxxko) but you will get the opportunity to learn or practice web, Android, or embedded programming if you wish to do so.  

You will do projects in teams. The number of teams and persons per team will be determined based on total number of registered students. Team structure is flexible, but we recommend an even distribution of the following roles among team members:  

- **ROS guru:** Understands the nitty gritty details of ROS (e.g. what's the difference between a topic and a message?) and knows how to use different ROS tools.  
- **Perception guru:** Understands sensor data and can write software for processing it.  
- **Hardware guru:** Understand the hardware, is not afraid of using a screw-driver or a 3D printer.  
- **Design and fabrication guru:** Makes sketches of ideas, knows 2D and 3D computer-aided design tools, knows how to operate the laser cutter and 3D printer.  
- **User interface guru:** Understands human factors and usability, makes things look good.  
- **Manager:** Makes sure every team member is on the same page at all times. Help make decisions (layout pros and cons). Enforce "interface agreements" so components can be easily integrated.  
- **Documentation and communications:** Makes videos, takes notes, writes blog posts, gives presentations and acts as spokesperson.

## LOGISTICS & RULES  

Please keep in mind:  
**Collaboration:**  

- Our main collaboration platform will be [GitHub](https://www.google.com/url?q=https%3A%2F%2Fgithub.com%2F&sa=D&sntz=1&usg=AOvVaw3K6x2c5JSD7q3c6-7F5JdK). If you do not yet have an account please create one.  
- One member from your team should create a repository for the class project and add the others as collaborators.  
- Use the wiki for internal documentation.  

**Assignments:**  

- You will give a weekly update every week in the form of a blog post on your Tumblr page.  
- Each week we will give you a list of things we would like to see in the blog post and tell you how the blog post will be reviewed and graded, here.  
- Your blog posts are due on the following **Monday at 5pm**. The teaching staff will review and grade blogs immediately after this deadline.  
- One member from each team should submit a link to the post on [Canvas](https://www.google.com/url?q=https%3A%2F%2Fcanvas.uw.edu%2F&sa=D&sntz=1&usg=AOvVaw0Eb0tU-buxkylFjlJDp0zG) by this deadline.  
- You will have a total of 5 "grace days" for late submissions. Late posts will be reviewed the following week. If you are out of grace days, you will receive 1/2^n of the total grade, where n is the number of weeks that the post is late for.  

**Lecture versus lab:** We will have mini-lectures (~30min) during some classes and use the rest of the lecture time for labs and feedback from the instructors.  

**Office hours:** There will be an office hour with one of the TAs once a week on Thursday afternoons. Notify the instructors if no one from your team is able to make it to the office hour. If you are having team issues or feel lost in terms of your project direction, you can schedule a team meeting with the instructor from [this calendar](https://www.google.com/calendar/selfsched?sstoken=UUtrX3dObVNyNFVQfGRlZmF1bHR8YzdlZTk0NWQyOGRkZWFjYTczM2RlYjkyYTJmNjMxYmQ).  

**Robotics news of the day:** At the beginning of Tuesday lectures at least one person will give a two-minute presentation of a robotics-related news or fun-fact. You can volunteer for this by sending the instructors a link to a news and a 1 or 2 sentence blurb about the link, which will be posted on the [course Tumblr page](http://www.google.com/url?q=http%3A%2F%2Fcse481sp17news.tumblr.com%2F&sa=D&sntz=1&usg=AOvVaw0f1nqAiYr_mX39q8-dtqSe).  

**Sharing the robot:** Six teams will need to share one robot! To make this as smooth as possible please reserve time on the [robot google calendar](https://calendar.google.com/calendar/embed?mode=week&src=cs.washington.edu_u990n37gkbs31e810jctf0ial8%40group.calendar.google.com&ctz=America/Los_Angeles) in blocks of at most 1h30m. We recommend that you use the robot simulator to test and debug your work before trying things on the physical robot.  
**E-mails:** When you email the instructor and/or the TA, please remember to include the word "CSE481" in your subject line.  
**Discussions:** Please use Canvas discussion boards for questions that might be relevant for the rest of the class.  
**Sharing the driver's seat:** All labs and assignments will be done in teams. Please make sure that the lead programmer role rotates among team members, no matter how slow you type or how little experience you have.

## GRADING

The distribution of your grades will be as follows:

- 60% Weekly blog posts
- 20% Final project demo and video
- 20% Participation and teamwork