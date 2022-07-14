<!-- https://lab.cs50.io/mbezaire/labs/rise/ghk -->
# Resting membrane potential

In the Nernst lab, we calculated the reversal potential of a single ion. However, we may also want to know what happens in a neuron that is permeable to multiple ions. We can use a different equation to calculate the resting membrane potential of a neuron, taking into account the influence of multiple ions simultaneously.

{% next %}

## GHK Equation

The equation we will use to calculate the resting membrane potential of a cell is the Goldman-Hodgkin-Katz equation, aka the GHK or Goldman equation.

The GHK equation considers the influence of multiple ions simultaneously. It also takes into account the relative permeability of the ions. Membrane permeability (how easy it is for an ion to cross a membrane) depends on how many ion channels are open, of the type of channels that allow a particular ion to cross.

Different types of ion channels open under different conditions (voltage, temperature, presence of specific molecules), so the permeability of the membrane is different for each type of ion.

{% next %}

The GHK equation is as follows:

<img src="https://latex.codecogs.com/svg.image?E_R&space;=&space;\frac{RT}{F}ln\(\frac{P_{Na}[Na]_{out} + P_{K}[K]_{out} + P_{Cl}[Cl]_{in}}{P_{Na}[Na]_{in} + P_{K}[K]_{in} + P_{Cl}[Cl]_{out}}\)">

where [X] refers to the concentration of ion X either inside or outside the neuron. Notice that the concentrations for chloride are flipped, as chloride has a negative valence.

{% spoiler "Parameters" %}

* R is the gas constant, 8.314 J/(K * mol)
* T is the temperature in Kelvins (K)
* F is Faraday's constant, 96485.3 Coulombs (C) / mol

{% endspoiler %}

Let's create a Python function that can calculate the resting membrane potential of a cell.

{% next %}

## Building the function

Open ghk.py to begin. 

**Note:** it may be easier to work inside the regular CS50 code website instead of this sandbox. To do so, copy the contents of ghk.py and paste into a new ghk.py file within https://code.cs50.io .

First, we'll define a function called `ghk` that takes in seven arguments:
* the valence of the ion
* the intracellular concentration of each of Na, K, and Cl in mM
* the extracellular concentration of each of Na, K, and Cl in mM

This function should return a variable calculated inside the function.

{% spoiler "See Code" %}

```
def ghk(valence, conc_in, conc_out):
    Vm = 0
    
    return Vm
    
```

{% endspoiler %}

{% next %}

Now, let's add the body of the `ghk` function. In the function, first define variables for the permeability of each ion (for K, use 1; for Na, use 0.05; for Cl, use 0.3). Then, write code to calculate the resting membrane potential of a neuron using the GHK equation, the permeabilities, and the information passed as arguments to the function. 

Checking our units, it seems that our reversal potential will be calculated in units of volts (V). However, units of milliVolts would be more useful for us. To convert, multiply the right side of the GHK equation by a factor of 1000.

Note: we can use the `math` library in Python to calculate the natural log, `ln`. The command we will use is `math.log()`; by default, the `log` method of math uses `e` as its base.

{% spoiler "See Code" %}

```
def ghk(...):
    p_k = 1
    p_na = 0.05
    p_cl = 0.3
    Vm = # plug in the ghk equation here
    
    return Vm
    
```
{% endspoiler %}

{% next %}

Now, let's add code that calls our function. We will need to place this section of code below our `ghk` function. We will need to un-indent the code as well, so that it is not part of our `ghk` function.

Let's call the function using the following concentrations:

<img title="Ions at the Membrane" src="https://github.com/mbezaire/labs/blob/rise/ghk/conc.png?raw=true" width=400>

Since the function should return a value, let's assign the output of the function (the function call will evaluate to this output) to a new variable. Next, print the new variable so we can see what our function calculates for the reversal potential.

Now let's run the code and test it. To execute the code file, enter in the terminal window: `python ghk.py`.

Verify that the code prints something like -85.565 when ran with the parameters given above.

{% next %}

## Submit the Code

After confirming that the equation is calculating correctly, test the code against our auto-checker by executing the command below in the terminal:

```
check50 --local mbezaire/checks/main/rise/ghk
```

Once you are satisfied with your work, you can submit it. First, follow the steps to get a [Github Personal Access Token](https://cs50.readthedocs.io/github/#personal-access-token) if you haven't yet. Then execute this command in the terminal to submit:

```
submit50 mbezaire/checks/main/rise/ghk
```
