#!/usr/bin/env python3

ipchk = input('Apply an IP address: ') # collect user input

if ipchk == '192.168.70.1': # if input is a match for 192.168.70.1
    print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.')
elif ipchk: # if any other input was provided, this is True
    print('Looks like the IP address was set: ' + ipchk)
else: # if input is False
    print('You did not provide input.')

print()
print('Now exiting the script...')
