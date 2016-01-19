# rboex
Remote Buffer Overflow Exploit &amp; Avoidance

#How it works(Basic)
+ Create a buffer of \x41 multiplied 3000 times
+ Declare s as socket
+ Connect to the socket
+ Send the buffer
+ Close the socket
