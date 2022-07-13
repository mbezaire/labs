<!-- https://lab.cs50.io/mbezaire/labs/rise/nernst -->
# Ions in Neurons

The electrical behavior of neurons depends on the intracellular and extracellular ions, especially on ions capable of crossing the neuron's membrane. At rest, the neuron's membrane potential is mostly determined by the ions potassium (K+), sodium (Na+) and chloride (Cl-) as well as negatively charged proteins inside the neuron.

<img title="Membrane permeable ions" src="https://biocyclopedia.com/index/general_zoology/images/images31/fig008.jpg" width=400>

{% next %}

These three ions are unevenly concentrated across the cell membrane. Inside the cell, K+ is much more abundant than outside. Conversely, Na+ and Cl- are much more prevelant in the extracellular space. The ions cannot freely cross the membrane; they can only cross when ion channels in the membrane open. And they can only pass through specific types of ion channels - not all channels allow all types of ions through.

In addition to these concentration gradients across the membrane, there is also a difference in charge, leading to a membrane potential of around -70 mV. This means the inside of the neuron is negatively charged relative to the extracellular space outside of the neuron.

{% next %}

## Reversal Potential 

The charge difference across the membrane and the concentration gradients impel the ions to cross the membrane when they can (ie, when ion channels in the membrane open, allowing specific types of ions to cross). 

The direction in which the ions cross depends on the concentration gradient and the electrical charge difference. Sometimes these forces are in opposition. For example, potassium is more highly concentrated in the cell and therefore should exit the cell when channels are open. However, inside the cell is much more negatively charged, which is attractive to the positively charged potassium ion.

{% next %}

<img title="Ions at the Membrane" src="https://biocyclopedia.com/index/general_zoology/images/images31/fig008.jpg" width=400>

To determine which direction a particular ionic current will flow when its channels are open, we can calculate a property called the reversal potential of the ion. The reversal potential is the membrane potential at which the current will switch directions (ions flowing in versus out of the cell).

{% next %}

## Nernst Equation

We can calculate the reversal potential of an ion using the Nernst Equation.

<img src="https://render.githubusercontent.com/render/math?math=E_R = \frac{RT}{zF}ln\frac{[X]_{in}}{[X]_{out}}">

where [X] refers to the concentration of ion X either inside or outside the neuron and z refers to the valence of ion X (+1 for potassium or sodium, -1 for chloride).

{% spoiler "Parameters" %}

R is the gas constant, 8.314 J/(K * mol)
T is the temperature in Kelvins (K)
F is Faraday's constant, 96485.3 Coulombs (C) / mol

{% endspoiler %}

Let's create a Python function that can calculate the reversal potential of an ion, given its intracellular and extracellular concentrations and its valence.

{% next %}

## Building the function

Open nernst.py to begin. 

**Note:** it may be easier to work inside the regular CS50 code website instead of this sandbox. To do so, copy the contents of nernst.py and paste into a new nernst.py file within https://code.cs50.io .

First, we'll define a function called `nernst` that takes in three arguments:
* the valence of the ion
* the intracellular concentration of the ion in mM
* the extracellular concentration of the ion in mM

This function should return a variable calculated inside the function.

{% spoiler "See Code" %}

```
def nernst(valence, conc_in, conc_out)
    rev_pot = 0
    
    return rev_pot
    
```

{% endspoiler %}

{% next %}

Now, let's add the body of the `nernst` function. In the function, write code to calculate the reversal potential of an ion using the Nernst equation and the information passed as arguments to the function.

Note: we can use the `math` library in Python to calculate the natural log, `ln`. The command we will use is `math.log()`; by default, the `log` method of math uses `e` as its base.

{% spoiler "See Code" %}

```
def nernst(valence, conc_in, conc_out)
    rev_pot = # plug in the nernst equation here
    
    return rev_pot
    
```
{% endspoiler %}

{% next %}

Now, let's add code that calls our function. We will need to place this section of code below our `nernst` function. We will need to un-indent the code as well, so that it is not part of our `nernst` function.

Let's call the function using data that represents potassium: a valence of 1, an intracellular concentration of approximately 140 mM, and an extracellular concentration of 3 mM.

Since the function should return a value, let's assign the output of the function (the function call will evaluate to this output) to a new variable. Next, print the new variable so we can see what our function calculates for the reversal potential.

{% spoiler "Hint" %}
To call a function in python, type the name of the function with open and close parenthesis (). Some functions, like our `nernst` function, expect to receive arguments in the parenthesis. We must put all three of our arguments in the function, in the same order as our function definition, and separate them with commas.
{% endspoiler %}

Now let's run the code and test it. To execute the code file, enter in the terminal window: `python nernst.py`.

Verify that the code prints something like -75 when ran with the parameters given above (1, 140, 3).

{% next %}

## Check the Code

Once you have finished the assignment, you can reorganize your code a bit and then test it against our auto checker.

Take these steps before running the tests on your code:
1. 
You can now test your code by executing the command below in the terminal:

```
check50 --local mbezaire/checks/main/rise/nernst
```

Once you are satisfied with your work, you can submit it. First, follow the steps to get a [Github Personal Access Token](https://cs50.readthedocs.io/github/#personal-access-token) if you haven't yet. Then execute this command in the terminal to submit:

```
submit50 mbezaire/checks/main/rise/nernst
```
