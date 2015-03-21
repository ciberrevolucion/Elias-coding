#!/usr/bin/python
# The goal of this script is to make a simple demonstration of an elias encoder, 
# in order to better understand this type of coding and to have an automated solver
# for my exercices at uni.


from elias_util import *

# Lets First get the String to encode:
toencode=raw_input("String to encode: ")
mode = raw_input("Choose the mode: 'auto' for real probabilities or 'custom' For custom probabilities: ")

# debug & testing
# toencode = 'ABBA'
# mode = 'auto'

# Lenght of the burst is set to the message lenght, in order to simpify the demonstartion
run = len(toencode)

# Setting probabilities for each symbol
prob=setProbabilities(toencode,mode)
print "Message: " + toencode
print "Probabilities: " + str(prob)

# Demo
print "Running encoder"
code=eliasEncoder(prob, run, toencode)
print "Running decoder"
message=eliasDecoder(prob,run,code)
print "Message: " + message
