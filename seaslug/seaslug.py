"""
Computational Lab 2: Sea slug skeleton
Starter File by mbezaire@bu.edu, based on
Tom Anastasio's habituation model in MATLAB
which sets up a simple simulation of the
Aplysia gill withdrawal reflex with
desensitization

Program completed by:
Date: 
"""

connweight = 4

def calculate_output(input):
    return input*connweight


print(calculate_output(3))