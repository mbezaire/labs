"""
===============
Basic pie chart
===============

Demo of a basic pie chart plus a few additional features.

In addition to the basic pie chart, this demo shows a few optional features:

* slice labels
* auto-labeling the percentage
* offsetting a slice with "explode"
* drop-shadow
* custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.
"""
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
pieprops = {"startangle":-90, "colors":["cornflowerblue", "white"], "shadow":True, "textprops":{'fontsize': 18, 'fontweight':'bold'}}
symbolprops = {"color":None, "fontweight":'bold', "fontsize":16, "verticalalignment":'baseline', "horizontalalignment":'left'}
    
fig1, ax = plt.subplots(2,3)
ax[0, 0].pie([1, 1], labels = ['$\\frac{1}{2}$',''], labeldistance=0.5,  **pieprops) # , explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90
ax[0, 0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax[0, 0].text(1.2, .0, '+', **symbolprops)

ax[0, 1].pie([1, 2], labels = ['$\\frac{1}{3}$',''], labeldistance=0.5, **pieprops) # , explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90
ax[0, 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax[0, 1].text(1.2, .0, '=', **symbolprops)


ax[1, 0].pie([1, 1], labels = ['$\\frac{1}{2}$',''], labeldistance=0.5, **pieprops) # , explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90
ax[1, 0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax[1, 0].text(1.2, .0, 'x', **symbolprops)


ax[1, 1].pie([1, 2], labels = ['$\\frac{1}{3}$',''], labeldistance=0.5, **pieprops) # , explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90
ax[1, 1].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax[1, 1].text(1.2, .0, '=', **symbolprops)

ax[0, 2].pie([5, 1], labels = ['$\\frac{5}{6}$',''], labeldistance=0.5, **pieprops) # , explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90
ax[0, 2].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

ax[1, 2].pie([1, 5], labels = ['$\\frac{1}{6}$',''], labeldistance=0.6, **pieprops) # , explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90
ax[1, 2].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
plt.savefig("pie.png")

#############################################################################
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.pie` / `matplotlib.pyplot.pie`
