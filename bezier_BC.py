import numpy as np
import bezier
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

nodes = np.asfortranarray([
    [0.0, 0.1, 0.15,0.2, 0.25,0.3,0.35, 0.4, 0.45,0.48, 0.6,0.65,0.78,0.8],
    [0.0, 1.5, 1.5,0.5,-0.25,-0.25,0.5, 1.5, 1.5,0, -0.5, -0.5,-0.3,0],
    ])
#curve = bezier.Curve(nodes, degree=12)
curve = bezier.Curve.from_nodes(nodes)

ax = curve.plot(num_pts=256)

lines = ax.plot(nodes[0, :], nodes[1, :],marker='o', linestyle='None', color='black')