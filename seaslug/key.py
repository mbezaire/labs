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
import matplotlib.pyplot as plt

sensory = [0, 0, 1, 0, 0]*6
connweight = 4
effconnweight = connweight
habrate = float(input("Enter a habituation rate: "))
def calculate_output(input):
    return input*effconnweight

motor = [0]*len(sensory)

for i, timestep in enumerate(sensory):
    motor[i] = calculate_output(timestep)
    if timestep == 1:
        effconnweight *= (1 - habrate)

print(motor)
"""
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(sensory)
ax1.set_ylabel('Sensory neuron activity')
ax1.set_xlim(0, len(sensory))
ax1.set_ylim(0, 1.1)

ax2 = fig.add_subplot(212)
ax2.plot(motor)
ax2.set_xlabel('Time step')
ax2.set_ylabel('Motor neuron activity')
ax2.set_xlim(0, len(motor))
ax2.set_ylim(0, connweight+0.5)
    
plt.show()
"""
