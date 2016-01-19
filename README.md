# rboex
Remote Buffer Overflow Exploit &amp; Avoidance

#How it works(Basic)
+ Create a buffer of \x41 multiplied 3000 times
+ Declaring s as socket
+ Connecting to the socket
+ Sending the buffer
+ Closing the socket
