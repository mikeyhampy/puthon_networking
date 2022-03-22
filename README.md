# Overview

This is a simple server to client and peer to peer networking program. I wanted to get more familiar with how server and client relationships work. Also, I wanted to get more aquainted with a peer to peer network.

This prgram is prep work for a quiz app I'm developing with my team. We want to connect users online to each other is a similar way as in this program.

[Software Demo Video](https://youtu.be/AA7CyFNxp48)

# Network Communication

The programs functionality works as a client server relationship just to have a common connection IP for people that may not know the IP addresses of those they are connecting to. Then once at least 2 people are connected to the server, they will then be connected to each other and be able to send messages back and forth.

I used UDP and for the server I used port 22 and the two clients, on separate machines, used ports 4375 and 4374. They used one port to receive and the other to send messsages to each other.

# Development Environment

Python 3
socket
threading

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Engineer Man (youtube channel)](https://www.youtube.com/watch?v=IbzGL_tjmv4)
* [Sonar Systems (youtube channel)](https://www.youtube.com/watch?v=DFsO-ZBCxH0)

# Future Work

list of things to fix, improve, and add in the future.
* make funtional with a game
* network using mobile devices
* impliment user login