import numpy as np
from color_scales import color_scales
import plotly.graph_objs as go
import plotly as py

# Create some fake data points drawn from two different distributions
n_features = 2
n_observations = 20000
X0 = np.concatenate((np.random.normal(0,1,(n_observations,n_features)),np.random.normal(2.5,1,(n_observations,n_features))))
X1 = np.concatenate((np.random.normal(1,1,(n_observations,n_features)),np.random.normal(3.5,1,(n_observations,n_features))))

# Custom color scale choices: choice of oranges, blues (more to come)
scales = color_scales()

# Plotly density plots with the new color scales
fig = go.Figure()
fig.add_histogram2dcontour(
        x = X0[:,0],
        y = X0[:,1],
        contours = dict(coloring='heatmap'),
        colorscale = scales.oranges,
        reversescale = True,
        xaxis = 'x',
#         yaxis = 'y',
        showscale = False,
        name="X0",
        showlegend=True
    )
fig.add_histogram2dcontour(
        x = X1[:,0],
        y = X1[:,1],
        contours = dict(coloring='heatmap'),
        colorscale = scales.blues,
        reversescale = True,
        xaxis = 'x',
        yaxis = 'y',
        showscale = False,
        name="X1",
        showlegend=True
    )
fig.layout.update(
    legend_orientation="v",
    title=go.layout.Title(
        text="Two Overlapping Density Plots",
    ),
)

# Save figure
fig.write_image("overlapping_densities.png", width=700, height=600, scale=2)