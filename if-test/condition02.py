#!/usr/bin/env python3

## collect user input
hostname = input("What value should we set for hostname?: ")

## use the upper method to test if input matches the expected value
if hostname.upper() == 'MTG':
    print("The hostname was found to be MTG")
    print("Hostname matches expected config")

## Always notify when the script is ending
print("Existing the script...")
