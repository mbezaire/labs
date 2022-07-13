<!-- https://lab.cs50.io/mbezaire/labs/rise/seaslug -->
# Aplysia 

*Aplysia* is a simple sea slug with a gill located dorsally. Because the gill is fleshy and therefore vulnerable to predators, Aplysia must contract it when predators are near to avoid being eaten.

<img title="Aplysia" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Aplysia_californica%2C_dorsal.jpg/1280px-Aplysia_californica%2C_dorsal.jpg" width=400>

{% next %}

## Gill withdrawal reflex

The gill is sensitive to touch. When the gill senses any pressure, it contracts, hiding the vulnerable, fleshy part of the gill from would-be predators.

This reflex is made possible by a sensory neuron that receives the touch information via activitation of mechanoreceptors. The sensory neuron is part of a circuit that connects to a motor neuron. When the motor neuron is activated, it releases neurotransmitter onto the gill muscle, contracting the muscle to pull the gill shut tight.

<img title="Reflex circuit from Biocyclopedia" src="https://biocyclopedia.com/index/general_zoology/images/images31/fig008.jpg" width=400>

Let's create a simplified model of the circuit involved in this reflex.

{% next %}

## Building the circuit

Open seaslug.py to begin. 

**Note:** it may be easier to work inside the regular CS50 code website instead of this sandbox. To do so, copy the contents of seaslug.py and paste into a new seaslug.py file within https://code.cs50.io .

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

We want to calculate the motor state as a function of the sensory input, perhaps by using a python function. The function would need to know the state of the sensory neuron as an input and would calculate and return the state of the motor neuron.

Ideally, we would like to have a line of code such as the following:

```
motor = calculate_output(sensory)
```

The `calculate_output` function should calculate the output by scaling the input value by a factor that represents the strength of the connection between the sensory neuron and the motor neuron. We'll call this scale the `connweight` and set its default value to `4`.

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

To execute your code file, enter in the terminal window: `python seaslug.py`.

Once `motor` is set correctly, let's develop this simulation further.

{% next %}

So far, our program only calculates a response at a single point in time. We have a snapshot, but what we really want is a whole video. We would like to model what happens with this gill over time.

To incorporate the dimension of time into this program, we need to set up our simulation so that it takes in the sensory neuron activity at multiple points in time. At each time point, the program must calculate the motor neuron activity or output.

Ideally, we would store this information over time so that we can graph the activity of the motor neuron over the time course of the whole simulation.

Take a moment and brainstorm how we might model the relationship between the sensory and motor neurons over time in this program.

{% next %}

## Simulating over time

Now, let's edit our code so that it can simulate the relationship between the sensory and motor neurons over time. We can envision the simulation as a series of time steps. Each time step, the sensory neuron may be activated (sensing a touch at that point in time) or inactive.

We can represent the sensory neuron activity as 0 (silent) or 1 (active, sensing a touch) at each point in time.

If we want to run a simulation for, say, 30 time steps, we would need a way to store 30 values corresponding to the activity of the sensory neuron at each point in time.

How might you update your `sensory` variable so that instead of it being set to 1 at a single point in time, it holds a series of 30 1's to represent being active the whole simulation?

{% spoiler "See Code" %}
```
sensory = [1]*30
```
{% endspoiler %}

After updating your `sensory` neuron so that it's on for 30 time steps in a row, let's consider a more interesting stimulation pattern.

{% next %}

Suppose our gill experienced a pattern of pulses rather than a single sustained touch. We might describe a pulse as taking place over 5 time steps, where the touch was only sensed during the middle time step.

We can create a different pattern of activity by setting the sensory neuron to receive 6 pulses in a row, where each pulse takes 5 time steps.

Update your code to assign the `sensory` neuron an activity of 6 pulses as described above.

{% spoiler "See Code" %}
```
sensory = [0, 0, 1, 0, 0]*6
```
{% endspoiler %}

{% next %}

## Moving through time
Now we need to move through time, taking into account the activity of the sensory neuron at each time step and calculating the resulting motor neuron activity at each time step.

We can loop over each time step in the total duration that our simulation is meant to model.

Let's create a loop that iterates over each of the 30 time steps of our sensory neuron's activity.

{% spoiler "Hints" %}
There are multiple ways to accomplish this in python.

One is:
1. Find the length of the `sensory` neuron activity list.
2. Assign that length to a new variable, perhaps `num_time_steps`.
3. Using a for loop, iterate over a `range` from 0 to `num_time_steps`

Another would be to iterate directly over the sensory neuron's activity level at each time point, using a for loop.

{% spoiler "Code" %}

```
for timestep in range(0, len(sensory)):
    # do some stuff each time step
```
{% endspoiler %}

{% endspoiler %}

{% next %}

Once you have figured out how to access the activity of the sensory neuron at each point in time, you'll need to calculate the activity of the motor neuron at each point in time.

Each calculation will require a separate call to `calculate_activity`, providing the sensory neuron's activity at that time point.

And each resulting motor neuron activity will need to be stored in such a way that it doesn't overwrite the value from another time point.

Think of what you can do with the `motor` variable so that it can store the motor neuron activity levels from all 30 time points.

{% spoiler "Hints" %}
Either way, you'll need to turn your `motor` variable into a list.

You may wish to start out with an empty list and add new activity levels to the end as you compute them.

Or you may create a placeholder with space for all time points ahead of time, and update the appropriate element in the list each time you calculate the activity at a particular time point.

If your for loop is iterating over a range, accessing the correct time point may be straightfoward. If you are iterating over each element, consider making use of the `enumerate` function.

{% endspoiler %}

Once you have a simulation that can run for 30 time steps, considering the sensory neuron activity at each step and calculating the resulting motor neuron activity, you are ready to graph your model.

{% next %}

## Graphing the simulation

To graph the simulation, we need to add some additional functionality to python. We do this by importing libraries.

For graphing, one useful library is matplotlib. We need a specific component within matplotlib, called pyplot.

We can import this component with the command `import matplotlib.pyplot as plt`, conventionally added to the top or beginning of our program file.

The `as plt` part of the command gives a nickname to `matplotlib.pyplot`, so that rather than typing out that whole name each time we want to refer to a function from that package, we can just preface it with `plt`.

{% next %}

Let's graph the sensory neuron and motor neuron activity separately. First, create two horizontal subplots. Then, plot the sensory activity on the top graph and the motor activity on the bottom graph. By plotting a single variable in each plot, the independent variable will be automatically set to the time step of the simulation.

{% spoiler "Code" %}
```
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
```

{% endspoiler %}

To see the graph, upon running `python seaslug.py` in the terminal, click the *Desktop* tab in your Lab window to show the figure. You may wish to click the full-screen icon in the upper right corner to fully view the figure. When done, click the little x on the figure itself to close the figure. Your python program will then complete and the terminal will display another prompt `$`.

**Note:** Close the figure before closing the *Desktop* tab or else the program will freeze. It is recommended to leave the *Desktop* tab open so that you can run the program multiple times and view the graph each time.

Once you have examined your graph, let's enhance the model so that it can include the biological process of habituation.

{% next %}

## Modeling habituation

Habituation refers to the ability of an organism to unlearn a link between a sensation and a reaction. If a sea slug repeatedly experiences a touch on its gill without any painful predation following, it will gradually reduce the magnitude of its muscle contraction reflex.

We can represent this weakening of the connection between sensory and motor neuron activity in our circuit.

Take a moment to think of what we might change in our code to represent this change.

{% next %}

One candidate is our parameter `connweight`. We can reduce its value to weaken the link between the two neurons.

However, the initial weight, before habituation, should stay the same.

Instead, lets introduce a new variable, `effconnweight`, to represent the effective (current) connection weight.

We can update this variable over the course of the simulation, depending on the simulation experienced by the sensory neuron.

Initially, the value of `effconnweight` should be set to the value of `connweight`.

{% next %}

Now let's add code to update the value of effconnweight in response to activity of the sensory neuron.

Keep in mind:
* We only want to update the value of `effconnweight` if the sensory neuron has experienced input
* We want the effect of the sensory neuron on the motor neuron to be reduced with repeated inputs
* Although the value of `effconnweight` needs to be updated each time the sensory neuron is active, the update should happen after the motor neuron activity has been calculated for that time step (why?)

To start, add another variable, `habrate`, to represent the rate at which the reflex circuit habituates (or the rate at which the connection weakens), on a scale of 0 to 1 where 0 means no habituation ever occurs and 1 means instant, full disconnection of the circuit would occur.

{% spoiler "Code" %}
```
habrate = .1
effconnweight = connweight

# inside the for loop:
    # after calculating the motor neuron output,
    # if the sensory neuron is active at this time point
    # decrement the effconnweight by the rate of habituation
    effconnweight = (1 - habrate)*effconnweight


```

{% endspoiler %}

After updating the code, set the `habrate` to 0.3 and run your code. Observe the graphs - how are they different from previously?

{% next %}

## Exploring the parameterspace

Let's make one more update to the code. We may want to experiment with many different rates of habituation to see how they affect the simulation.

To make it easy to run the code multiple times, let's set the `habrate` variable according to user input where we prompt the programmer to enter the habituation rate.

Make sure to add the value of `habrate` to the title of your figure so that you can tell which rate of habituation led to which results.

{% spoiler "Code" %}
```
ax1.set_title("Habituation: " + str(habrate))
```
{% endspoiler %}

Try running the simulation with several different rates of habituation.

{% next %}

## Check the Code

Once you have finished the assignment, you can reorganize your code a bit and then test it against our auto checker.

Take these steps before running the tests on your code:
1. Comment out your plotting commands (use three double quotes to start and end a multi-line comment)
2. Comment out the line that imports matplotlib.pyplot
3. At the end of your code, print out the contents of your `motor` variable

You can now test your code by executing the command below in the terminal:

```
check50 --local mbezaire/checks/main/rise/seaslug
```

Once you are satisfied with your work, you can submit it. First, follow the steps to get a [Github Personal Access Token](https://cs50.readthedocs.io/github/#personal-access-token) and then execute this command in the terminal to submit:

```
submit50 mbezaire/checks/main/rise/seaslug
```
{% next "Optional Challenge" %}

## Challenge

For this program, we made several assumptions:
* The stimulus (the actual touch on the gill) would consistently affect the activity of the sensory neuron
* The habituation would only be a function of how many times the reflex had been activated
* The habituation would not be forgotten (in reality, after a long period without any touch, a subsequent touch is likely to elicit activation closer to the original, unhabituated level)

We also made simplifications, such as:
* The influence of the sensory neuron on the motor neuron could be characterized by a linear relationship
* The motor neuron activity could represent the muscle contraction

Consider what you would need to add to this simulation to relinquish any of the assumptions above. Also consider how you could refine the model so that it is more realistic, addressing any of the simplifications listed.

{% next %}

Now, try implementing your idea(s) in the program. You may need to add additional variables or functions in order to do so.

Add comments to your code, documenting the changes you have made and the assumption or simplification they address.

Make sure to test and graph your code - does it make sense? How does it compare to your original simulation?

When you are satisfied with your updated program, you may submit it to:

```
submit50 mbezaire/checks/main/rise/seaslug-challenge
```
