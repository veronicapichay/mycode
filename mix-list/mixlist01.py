#!/usr/bin/env python3

# create a mix list and display it
my_list =my_list = [ "192.168.0.5", 5060, "UP" ]
print("The first item in the list (IP): " + my_list[0] )

# Forcing an int value to convert into string. Needs conversation to concatenate
print("The second item in the list (port): " + str(my_list[1]))

print("The last item in the list (state): " + my_list[2] )

# CHALLENGE 01 -
# Given the list iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ], display only the IP addresses on the screen

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
