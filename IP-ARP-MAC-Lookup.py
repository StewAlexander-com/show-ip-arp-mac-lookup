#!/usr/bin/env python3
import os
import sys
import time
import csv

#if file "Found_MAC_Addresses.txt" exists, delete it
if os.path.exists("Found_MAC_Addresses.txt"):
    os.remove("Found_MAC_Addresses.txt")

mac_address =""

#Show the contents of the current directory
print("\nPlease select the #SH IP ARP Data text file from the current directory\n")
print(os.listdir(), "\n")

#while the file name is not valid, ask the user to input the file name again
while True:
    csv_file = input("Please enter the file name: ")
    if os.path.isfile(csv_file):
        break
    else:
        print("\nThe file name is not valid, please try again\n")

while mac_address != "q" :
    #Ask the user for the mac address to search for
    mac_address = input("Please enter the MAC address to search for in any format, or press q to quit: ")
    #if the mac address has ":" or "-" in it, then it's a PC address, convert it to Cisco format
    if ":" in mac_address or "-" in mac_address:
        #convert the mac address to cisco format
        #save mac_address as lowecase
        mac_address = mac_address.lower()
        #remove the ":" from the mac_address
        mac_address = mac_address.replace(":", "")
        #remove the "-" from the mac_address
        mac_address = mac_address.replace("-", "")
        #Every 4 characters, insert a "."
        mac_address = mac_address[0:4] + "." + mac_address[4:8] + "." + mac_address[8:12]
    #if neither ":" or "-" or "." in it then tell the user it's not a valid mac address
    elif ":" not in mac_address and "-" not in mac_address and "." not in mac_address and "q" not in mac_address:
        print("\nWhat was entered is not a valid MAC address.\n")
        continue
    else :
        pass      
    #For every line split the line into a word list 
    with open(csv_file, 'r') as f:
        for line in f:
            #split the line into words
            words = line.split()
            #if words[2] is equal to the mac address, then print the line
            if words[2] == mac_address:
                print("\n===================================================\n\n",line + "\n===================================================\n")
                #save the line to a file called "Found_MAC_Addresses.txt"
                with open("Found_MAC_Addresses.txt", "a") as f:
                    f.write(line)
                break   
        else :
            if mac_address != "q":
                print("\nThe MAC address you entered was not found in the file\n")
                pass
            else:
                pass    

#close the file
f.close()

#if the file "Found_MAC_Addresses.txt" was created, tell the user
if os.path.exists("Found_MAC_Addresses.txt"):
    print("\nPlease see file \"Found_MAC_Addresses.txt\" which shows the found MAC Addresses\n")

#Wait for the user to press enter to exit the program
input("\nPress enter to exit the program ")
sys.exit()



            






