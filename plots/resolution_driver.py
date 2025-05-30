'''
Edited from github repo: 
    Accessed: May 26, 2025
'''

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from pandas.api.types import CategoricalDtype
import numpy as np

# Load the CSV file
csv_file_path = "/home/uribe055/sedona_experiments/results/all_resolutions.csv"
df = pd.read_csv(csv_file_path)


line = "sys"
y = "total_time"

# Get unique plot values
# cur_plot = "t_res"
# unique_plots = ["hour", "day", "year"]
# tick_list = [0.25, 0.5, 1.0]
# tick_labels = [0.25, 0.5, 1.0]
# x = "s_res"
# x_label = "Spatial resolution (degrees)"

cur_plot = "s_res"
unique_plots = [0.5, 1.0]
tick_list = ["hour", "day", "month", "year"]
tick_labels = ["hour", "day", "month", "year"]
x = "t_res"
x_label = "Temporal resolution"

marker_size = 25
m_fill = "none"
font_size = 30
tick_font_size = 30
tick_size = 30

line_width = 4
above = "bottom"
below = "top"
y_label = "Execution time (sec)"
viridis = matplotlib.colormaps["gray"]       # color - viridis 
colors = [viridis(i) for i in [0, 0.10, 0.20]]

# Define style dictionary based on 'line' values
style_dict = {
    "Polaris": {"marker": "o", "markersize": marker_size, "linewidth": line_width, "color": colors[0], "labelsize": font_size, "ticksize": tick_size, "ticklist": tick_list, "ticklabels": tick_labels, "fill": "none"},
    "Sedona": {"marker": "d", "markersize": marker_size, "linewidth": line_width, "color": "blue", "labelsize": font_size, "ticksize": tick_size, "ticklist": tick_list, "ticklabels": tick_labels, "fill": "none"},
    "Vanilla": {"marker": "v", "markersize": marker_size, "linewidth": line_width, "color": colors[1], "labelsize": font_size, "ticksize": tick_size, "ticklist": tick_list, "ticklabels": tick_labels, "fill": "none"},
    "TileDB": {"marker": "s", "markersize": marker_size, "linewidth": line_width, "color": "blue", "labelsize": font_size, "ticksize": tick_size, "ticklist": tick_list, "ticklabels": tick_labels, "fill": "none"},
}

# Determine global y-axis limits
y_min = df[y].min()
y_max = np.power(10, np.log10(df[y].max()) + 0.1)

legend_position = ["best", "lower left", "best", "center"]    # 'best', 'upper right', 'upper left', 'lower left', 'lower right', 'right', 'center left', 'center right', 'lower center', 'upper center', 'center'

# Generate and save individual plots
for plot_value, position  in zip(unique_plots, legend_position):
    fig, ax = plt.subplots(figsize=(7.4, 6))
    subset = df[df[cur_plot] == plot_value] # df[df[t_res]]==hour
    
    for line_value in subset[line].unique():
        line_data = subset[subset[line] == line_value]  # df[df[system] == polaris]
        cat_type = CategoricalDtype(categories=tick_list, ordered=True)
        line_data[x] = line_data[x].astype(cat_type)

        line_data = line_data.groupby(x, as_index=False)[y].mean()  # Average over x values
        
        line_data = line_data.sort_values(by=x)  # Ensure lines are connected correctly

        # Get style properties from dictionary, use defaults if not found
        style = style_dict.get(line_value, {"marker": "o", "markersize": 4, "linewidth": 1.5, "color": "black", "labelsize": 10, "ticksize": 8})
        
        ax.plot(line_data[x], line_data[y], 
                marker=style["marker"], markersize=style["markersize"], fillstyle=style["fill"],
                linewidth=style["linewidth"], color=style["color"], label=f"{line_value}")
    
    ax.set_xlabel(x_label, fontsize=font_size)
    if style["ticklist"] is not None:
        ax.set_xticks(ticks=style["ticklist"])
        ax.set_xticklabels(style["ticklabels"])
    ax.set_ylabel(y_label, fontsize=font_size)
    ax.set_yscale("log")  # Set y-axis to log scale
    ax.set_ylim(y_min, y_max)
    if plot_value == "day" or plot_value == "year":
        ax.legend(fontsize=font_size-8, loc="best")   # for datasets_averaged
    elif plot_value == 0.5 or plot_value == 1.0:
        ax.legend(fontsize=font_size-8, loc="best") 
    else: # plot_value == hour:
        ax.legend(fontsize=font_size-3, loc=position)     # for datasets_averaged
    ax.tick_params(axis='both', labelsize=tick_font_size)
    
    # test
    plt.tight_layout()
    plt.savefig(f"/home/uribe055/sedona_experiments/plots/tdb_blue/res__{plot_value}.png")  # Save the plot to a file
    # plt.close(fig)

    # final
    plt.tight_layout()
    plt.savefig(f"/home/uribe055/sedona_experiments/plots/tdb_blue/res__{plot_value}.eps")  # Save the plot to a file
    plt.close(fig)