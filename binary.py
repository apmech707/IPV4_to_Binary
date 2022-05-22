""" This program converts IPV4 dotted-decimal notation addresses into their binary
equivalents for the purposes of speeding up networking calculations. Specifically figuring
out which part of the address is the network and which part is the computer's ip while
using the subnet mask. Work smarter not harder! :) Feel free to verify that this
code works as it should before you rely on it, but I have done good testing on it. """


def cycle_through_octet(n, f):

    temp = []
    num = n
    flag = f

    if num >= 128:
        temp.append('1')
        num = num-128
    elif num < 128:
        temp.append('0')
    if num >= 64:
        temp.append('1')
        num = num-64
    elif num < 64:
        temp.append('0')
    if num >= 32:
        temp.append('1')
        num = num-32
    elif num < 32:
        temp.append('0')
    if num >= 16:
        temp.append('1')
        num = num-16
    elif num < 16:
        temp.append('0')
    if num >= 8:
        temp.append('1')
        num = num-8
    elif num < 8:
        temp.append('0')
    if num >= 4:
        temp.append('1')
        num = num-4
    elif num < 4:
        temp.append('0')
    if num >= 2:
        temp.append('1')
        num = num-2
    elif num < 2:
        temp.append('0')
    if num >= 1:
        temp.append('1')
        num = num-1
    elif num < 1:
        temp.append('0')
  
    if flag == 1:
        temp.append('.')

    return temp



def ipv4_to_binary(thing):

    byte = None
    binary_number = []
    x,y,z,a = thing.split(".")

    print("Processing IPv4 address " + x+'.'+y+'.'+z+'.'+a)
    print("|")
    

    

    byte = int(x)
    binary_number += cycle_through_octet(byte, 1)
    byte = int(y)
    binary_number += cycle_through_octet(byte, 1)
    byte = int(z)
    binary_number += cycle_through_octet(byte, 1)
    byte = int(a)
    binary_number += cycle_through_octet(byte, 0)

    binary_number = ''.join(binary_number)
    
    print(f"Binary equivalent: {binary_number}")

        
    
    
        
    
   
print("Convert IPV4 address into thier binary equivalent")
ipv4_address = input("Enter the IPV4 address to be converted \n ")

ipv4_to_binary(ipv4_address)
