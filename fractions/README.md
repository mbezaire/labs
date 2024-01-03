---
files:
  - Client.java
  - Fraction.java
url: https://raw.githubusercontent.com/mbezaire/labs/ahs/fractions/README.md
window:
  - terminal
---

<!-- https://lab.cs50.io/mbezaire/labs/ahs/fractions -->
# Fractions

A fraction represents a quantity as a numerator (how much we have) and a denominator (the total). We can perform common math functions on fractions.

<img title="Diagram of a pie chart fraction" src="https://github.com/mbezaire/labs/blob/ahs/fractions/pie.png?raw=true" width=400>

Let's create a Fraction class in Java and then write methods that allow us to add, subtract, multiply, and divide `Fraction`s.

{% next %}

## Fraction.java
Open Fraction.java to begin. The class we'll define will be called  `Fraction`.

Next, consider what **attributes** or fields a `Fraction` should have.

{% spoiler "Attributes" %}

In math, we define a fraction is a numerator over a denominator. Once we have those two pieces of information, our fraction is fully defined. So our fields could be:

* numerator
* denominator

{% endspoiler %}

{% next %}

## Fields
Once you have decided on the attribute(s) for the Fraction class, consider how to declare them in the `Fraction.java` file:

* Should the visibility be `public` or `private`?
* What data type should each attribute be?

Then, add the declarations for the attribute(s) to the Fraction class definition.

{% spoiler "Syntax" %}
```
private int numerator;
private int denominator;
```
{% endspoiler %}

{% next %}

## Creating Fractions

Now, let's construct a method that allows our client code to pass in a numerator and a denominator as the Fraction object is instantiated (created).

Add a constructor with parameters for a numerator and a denominator.

In the body of the constructor, add code to set the
value of each attribute (numerator or denominator) to the local variables.

Add some logic so that the Fraction cannot have a denominator of 0. If the denominator is 0, set it to 1 instead.

{% spoiler "Hint" %}
```
public Fraction(int n)
{
    numerator = n;
    if (d == 0)
        denominator = 1;
    else
        denominator = d;
}
```
{% endspoiler %}

<!--
{% spoiler "Hint" %}

`public Fraction(int n, int d)
{
    // Remember, when writing
    // equations in code,
    // the unknown or the
    // variable whose value
    // you want to set goes on
    // the left.

    // The right hand side is
    // what you know already,
    // whether a variable with
    // a value assigned, an expression
    // that evaluates to something,
    // or a hard-coded value such as
    // a number or String literal

    // We already know n and d,
    // which are the local variables
    // that get set to the arguments
    // passed in when a Fraction is instantiated.

    // On the left side go the variables
    // whose values we want to set, which
    // are the instance variables numerator
    // and denominator.
}
`

{% endspoiler %}
-->

{% next %}

## Alternate Constructor
Now let's add another constructor that allows us to pass in only a numerator, setting the denominator to 1.

{% spoiler "Hint" %}
```
public Fraction(int n)
{
    numerator = n;
    denominator = 1;
}
```
{% endspoiler %}

{% next %}

## Copy Constructor
Lastly, let's add a copy constructor. We'll need to pass in a reference to some other Fraction object and set all the fields of our object to the values of the corresponding fields in the other Fraction object.

{% spoiler "Hint" %}
Recall that, as we are in the Fraction class, we have access to the private fields and methods of other Fraction objects. We can either refer to the fields directly or use getters and setters, if we have defined them.
```
public Fraction(Fraction other)
{
    numerator = other.numerator;
    denominator = other.denominator;
}
```
{% endspoiler %}

{% next %}

## toString()
Next, let's add a `toString()` method that returns a String
displaying our Fraction as:
`numerator / denominator`

{% spoiler "Syntax Hint" %}
```
public String toString()
{
    return numerator + "/" + denominator;
}
```
{% endspoiler %}

Now we're ready to build some client code to try out our Fraction class.

{% next %}

## Client Code
In a new file called `Client.java`, define a `main` method.

Inside the main method, let's declare and instantiate some `Fraction`s, testing each of our constructors at least once. Remember to use the `new` keyword.

{% spoiler "Syntax" %}
```
Fraction quarter = new Fraction(1,4);
Fraction half = new Fraction(1,2);
Fraction whole = new Fraction(1);
Fraction one = new Fraction(whole);
```
{% endspoiler %}

After creating our `Fraction` objects, we will want to check them. Let's print our `Fraction` objects.


{% spoiler "Syntax" %}
```
System.out.println(quarter);
System.out.println(half);
System.out.println(whole);
System.out.println(one);
```
{% endspoiler %}


{% next %}
## Compile and Test

Let's test our code. To compile, run the following command in the terminal:
```
javac Client.java
```
If there are any compile errors, troubleshoot them before moving on.

Once the program compiles, run it by executing the following command in the terminal:
```
java Client
```

{% next %}
## Math methods
Create methods `add`, `subtract`, `multiply`, and `divide` to perform their respective mathematical operations based on fraction arithmetic. The `divide` method should use the current `Fraction` as the dividend and the passed-in reference as the divisor.

Each of these methods should expect a Fraction object as a parameter. The passed in object is
the right side of the arithmetic equation, this object is the left side.

Each arithmetic method builds a new instance of a Fraction object with the resulting calculation
and returns its value. These methods should not change the value of either this Fraction or the
parameter Fraction.

Provide a method called `value()` that returns the decimal equivalent of the fraction.

Then make sure the `Fraction` class still compiles:

```
javac Client.java
java Client
```

{% next %}
## Testing our math

Now let's add some more client code to test our math:

{% spoiler "Syntax" %}
```
Fraction threeQuarters = half.add(quarter);
Fraction oneEighth = half.multiply(quarter);
System.out.println(threeQuarters);
System.out.println(oneEighth);
```
{% endspoiler %}

Remember to (re)compile and run our code to test it after making these updates:

```
javac Client.java
java Client
```

Now you're ready for the final check!

{% next %}
## Check your code

Once you have finished the assignment, you can test grade it by executing the command below in the terminal:

```
check50 --local  mbezaire/checks/main/java/fraction
```

If you have joined our online classroom and wish to share your completed Fraction code to the teacher, you can submit it. First, follow the steps to get a [Github Personal Access Token](https://cs50.readthedocs.io/github/#personal-access-token) and then execute this command in the terminal to submit:

```
submit50 mbezaire/checks/main/java/fraction
```

{% next %}
## Challenge

Once your Fraction class passed all the `check50` tests (with everything in the check list showing up green and smiley), you may challenge yourself by adding additional functionality to your `Fraction` class:

First, define a `reduce` method in `Fraction.java` that will reduce the fraction to its lowest terms. Find the largest common factor of the numerator and denominator and divide them both by that factor.

Then, call `reduce()` from the constructors in `Fraction` so that instantiating a new `Fraction(4, 8)` would create a `Fraction` of 1/2 instead.

{% next %}

## Challenge Constructor

Lastly, create another constructor that takes in a double as a parameter and creates a Fraction object based on
the double value.

For example,

```
Fraction f = new Fraction(.25);
System.out.println(f); // prints 1/4
```

You can check your challenge code using:

```
check50 --local mbezaire/checks/main/java/fraction-challenge
```
If you have joined our online classroom and wish to share your completed Fraction/challenge code to the teacher, you can submit it. First, follow the steps to get a [Github Personal Access Token](https://cs50.readthedocs.io/github/#personal-access-token) and then execute this command in the terminal to submit:

```
submit50 mbezaire/checks/main/java/fraction-challenge
```
