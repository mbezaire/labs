<!-- https://lab.cs50.io/mbezaire/labs/rise/seaslug -->
# Aplysia 



## Gill withdrawal reflex

The gill is sensitive to touch. When the gill senses any pressure, it contracts, hiding the vulnerable, fleshy part of the gill from would-be predators.

This reflex is made possible by a sensory neuron that receives the touch information via activitation of mechanoreceptors. The sensory neuron is part of a circuit that connects to a motor neuron. When the motor neuron is activated, it releases neurotransmitter onto the gill muscle, contracting the muscle to pull the gill shut tight.

<img title="Diagram of a pie chart fraction" src="https://github.com/mbezaire/labs/blob/ahs/fractions/pie.png?raw=true" width=400>

Let's create a model of the circuit involved in this reflex.

{% next %}

## Building the circuit

Open seaslug.py to begin. 

First, we'll create the variables to represent the reflex circuit.

Our circuit will be quite simple:
* a variable to represent the touch input (or activation of the sensory neuron)
* a variable to represent the muscle state (or activation of the motor neuron)
* a manner of linking the touch input variable with the muscle state variable

Let's define our variables first:
```
sensory = 0
motor = 0
```
{% next %}

We want to calculate the motor state as a function of the sensory input, perhaps by using a function. The function would need to know the state of the sensory neuron as an input and would calculate and return the state of the motor neuron.

Ideally, we would like to have a line of code such as the following:

```
motor = calculate_output(sensory)
```

The `calculate_output` function should calculate the output by scaling the input value by a factor that represents the strength of the connection between the sensory input and the muscle activity (output). We'll call this scale the `connweight` and set its default value to `4`.

Let's write code to define the function.

{% spoiler "See Code" %}
```
connweight = 4

def calculate_output(input):
    return input*connweight
```
{% endspoiler %}

{% next %}

Now, let's use the function to calculate the value of motor.

Below the function definition, assign `motor` to the output of a call to the `calculate_output` function, where `sensory` is provided as the input.

Let's test what we have so far. Set the value of `sensory` to 1. After assigning `motor` to the result of the call to `calculate_output`, print `motor` to verify that it is set to 4.

Once `motor` is set correctly, let's develop this simulation further.

{% next %}

So far, our program only calculates a response at a single point in time. We have a snapshot, but what we really want is a whole video. We would like to model what happens with this gill over time.

To incorporate the dimension of time into this program, we need to set up our simulation so that it takes in the sensory neuron activity at multiple points in time. At each time point, the program must calculate the motor neuron activity or output.

Ideally, we would store this information over time so that we can graph the activity of the motor neuron over the time course of the whole simulation.

Take a moment and brainstorm how we might model the relationship between the sensory and motor neurons over time in this program.

{% next %}

## Simulating Over Time



## Graphing the sensory and motor neuron activity



## Modeling Habituation


## Exploring the Parameterspace



Now you're ready for the final check!

{% next %}
## Check the Code

Once you have finished the assignment, you can test grade it by executing the command below in the terminal:

```
check50 mbezaire/checks/main/rise/seaslug
```

Once you are satisfied with your work, you can submit it. First, follow the steps to get a [Github Personal Access Token](https://cs50.readthedocs.io/github/#personal-access-token) and then execute this command in the terminal to submit:

```
submit50 mbezaire/checks/main/rise/seaslug
```