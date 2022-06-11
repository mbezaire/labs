# Fractions

A fraction represents a quantity as a numerator (how much we have) and a denominator (the total). We can perform common math functions on fractions.

<img title="Diagram of a pie chart fraction" src="https://github.com/mbezaire/labs/blob/ahs/fractions/pie.png?raw=true" width=400>

Let's create a Fraction class in Java and then write methods to perform math functions on Fraction objects. Then we can create `Fraction`s and add, subtract, multiply, and divide them.

{% next %}

Open Fraction.java to begin. The class we'll define will be called  `Fraction`. 

Next, consider what **attributes** or fields a `Fraction` should have.

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

Let's test our code. To compile, run the following command in the terminal:
```
javac Client.java
```
If there are any compile errors, troubleshoot them before moving on.

Once the program compiles, run it by executing the following command in the terminal:
```
java Client
```


## Math methods



## Copy Constructor


## More Client Code


## Testing

As a reminder, to compile our code we will enter a command at the terminal:

`javac Client.java`

This will compile our Client class and also our Fraction class. Look in the terminal for any compile errors.

Once compiled, the Client code (which contains the main method) can be run by entering at the terminal:

`java Client`

## How to Submit

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 mbezaire/checks/main/fractions
```
## Reviewing Feedback



## Challenge

After submitting your fraction work, you may continue with these challenges:
1. Add a method to reduce the fraction. Find the largest common factor of the numerator and denominator and divide them both by that factor.

You can submit your updated code using:

```
submit50 mbezaire/checks/main/fractions-challenge
```

