# overlapping-densities
Plot two 2D density plots (using Plotly's histogram2dcontour) on the same figure.

I ran into this problem when I was trying visualize TSNE clusters from two separate classes. With too many data points, my scatter plots looked like large blobs:

![Image of overlapping scatter plots](https://i.imgur.com/pLDz8kt.png)

I couldn't find any code that allowed me to plot two separate density/contour plots on the same figure, so I created this code to plot the following:

![Image of overlapping density plots](https://i.imgur.com/szZy1ud.png)

Look at those clear, beautiful clusters!
