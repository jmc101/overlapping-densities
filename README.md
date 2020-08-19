# overlapping-densities
Plot two overlapping 2D density plots (using Plotly's histogram2dcontour) on the same figure.

When I was trying visualize clusters from two separate classes of data using TSNE, I ran into a problem. With too many data points, my scatter plots looked like large blobs and I couldn't see the areas of high density:

![Image of overlapping scatter plots](https://i.imgur.com/pLDz8kt.png)

I couldn't find any code that allowed me to plot two separate density/contour plots on the same figure, so I created this code to plot the following:

![Image of overlapping density plots](https://i.imgur.com/szZy1ud.png)

Look at those beautiful clusters!
