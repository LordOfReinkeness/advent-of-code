import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.ion()

def create_initial_plot(data):
    fig, ax = plt.subplots()

    # Identify the valid normal values (>=0 and < sys.maxsize)
    normal_values = data[(data >= 0) & (data < sys.maxsize)]
    if normal_values.size > 0:
        max_valid_val = normal_values.max()
    else:
        max_valid_val = 0

    # Normalization: -1 maps to 0.0, sys.maxsize maps to 1.0
    norm = matplotlib.colors.Normalize(vmin=-1, vmax=max_valid_val+1)

    # Calculate fractions for the key points
    # fraction = (value + 1)/(max_valid_val + 2)
    frac_neg_1 = 0.0  # for value -1
    frac_0 = (0 + 1)/(max_valid_val + 2)           # for value 0
    frac_max = (max_valid_val + 1)/(max_valid_val + 2)  # for value max_valid_val
    frac_maxsize = 1.0  # for value sys.maxsize (mapped to max_valid_val+1)

    # Define colors:
    # At -1: black
    # At 0: firebrick (#B22222) - a lighter dark red
    # At max_valid_val: bright red (#FF0000)
    # At sys.maxsize: white
    cdict = [
        (frac_neg_1, 'black'),
        (frac_0, '#B22222'),   # Firebrick
        (frac_max, '#FF0000'), # Bright red
        (frac_maxsize, 'white')
    ]

    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("custom_red_map", cdict)

    img = ax.imshow(data, cmap=cmap, norm=norm, origin='lower')
    plt.colorbar(img, ax=ax)
    plt.show(block=False)
    plt.pause(0.1)

    return fig, ax, img, max_valid_val

def update_plot(img, data):
    normal_values = data[(data >= 0) & (data < sys.maxsize)]
    if normal_values.size > 0:
        max_valid_val = normal_values.max()
    else:
        max_valid_val = 0

    # Update normalization if needed
    img.norm.vmax = max_valid_val + 1

    # Update the data
    img.set_data(data)

    # Redraw
    img.figure.canvas.draw()
    img.figure.canvas.flush_events()

if __name__ == '__main__':
    initial_data = np.array([
        [0, 1, 2, -1],
        [2, -1, 5, sys.maxsize],
        [3, 4, 9, 10]
    ], dtype=int)

    fig, ax, img, max_val = create_initial_plot(initial_data)

    for _ in range(5):
        new_data = np.random.randint(-1, 20, initial_data.shape)
        new_data[0,0] = sys.maxsize
        update_plot(img, new_data)
        plt.pause(1)
