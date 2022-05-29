# Fractions

## Fraction Class

Fractions represent a quantity in terms of a numerator (how much we have) and a denominator (how much in total). In math, we learn how to perform common math functions on fractions.

![Diagram of a pie chart fraction](pie.png)

Let's create a Fraction class in Java and then write methods that can perform math functions on Fraction objects.

The class we'll define will be called  `Fraction`. And we'll also create some client code that will create `Fraction`s and add, subtract, multiply, and divide them.

First, consider what **attributes** or fields a `Fraction` should have.

{% spoiler "Attributes" %}

In math, we define a fraction is a numerator over a denominator. Once we have those two pieces of information, our fraction is fully defined. So our fields could be:

* numerator
* denominator

{% endspoiler %}

{% next %}

Once you have decided on the attribute(s) for the Fraction class, consider how to declare them in the `Fraction.java` file:

* Should the visibility be `public` or `private`?
* What data type should each attribute be?

Then, add the declarations for the attribute(s) to the Fraction class definition.

{% spoiler "Syntax" %}

`private int numerator;`

`private int denominator;`
{% endspoiler %}

{% next %}

## Creating Fractions

Now, let's construct a method that allows our client code to pass in a numerator and a denominator as the Fraction object is created. 

Add a constructor with parameters for a numerator and a denominator to be passed in as the Fraction object is instantiated (created).

In the body of the constructor, add code to set the
value of each attribute (numerator or denominator) to the local variables

{% spoiler "Syntax" %}
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
}
`

{% endspoiler %}

Next, let's add a `toString()` method that returns a String
displaying our Fraction as:
`numerator / denominator`

Now, let's build some client code to try out our Fraction class.

{% next %}

## Client Code


## Math methods



## Copy Constructor


## More Client Code


## Testing


## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 cs50/problems/2019/fall/mario/less
```
