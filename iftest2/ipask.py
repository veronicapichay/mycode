#!/usr/bin/env python3
"""Veronica Pichay | TLG Learning
   Conditionals - testing if strings test true"""

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
if ipchk:
   print("Looks like the IP address was set: " + ipchk) # indented under if
else:    # if data is NOT provided
   print("You did not provide input.") # indented under else
