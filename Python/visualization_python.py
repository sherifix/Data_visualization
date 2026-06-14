import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec
import matplotlib.colors as mlc
from matplotlib.ticker import AutoMinorLocator



#reading the data
signals = pd.read_csv("data/10_project_data_signals.csv")
annotation = pd.read_csv("data/10_project_data_annotation.csv")

#creating figures and axes and aligning then with no space in between sharing the same x-axis
fig, ax = plt.subplots(5,1, sharex=True)
fig.set_size_inches(10,6)
fig.subplots_adjust(hspace=0) 

#capturing signals' columns names
signals_columns = list( signals.columns)

#iterating over signals_columns to adjust the upper 4 plots
for i in range(len(signals_columns)):
    ax[i].plot(signals[signals_columns[i]], color = "#505050")
    ax[i].set_ylim(0, 1.2)
    ax[i].set_ylabel(signals_columns[i], fontsize = 10)
    ax[i].grid(axis = "x", linestyle = "dotted", linewidth = 1.5, zorder=1)


#adjusting the lowest plot
ax[4].set_yticks([0.2, 0.8], labels = ("-", "+"))
ax[4].grid(axis = "x", linestyle = "dotted", linewidth = 0.8, zorder=1)
ax[4].set_ylabel("Annotation", fontsize = 8)
ax[4].set_xlabel("Genomic Position", fontsize = 9)


#creating list capturing all figures in annotation plot
annotation_figures = []

#iterating over each row in annotation to get the length
for i in annotation.index:
    start = annotation["start"].iloc[i]
    stop = annotation["stop"].iloc[i]
    length = stop - start
    
    #postisioning each strand
    if annotation["strand"].iloc[i] == "+":
        strand = 0.8
    else:
        strand = 0.25
    
    #drawing figures for start, end and whole transcript using if statement
    if annotation["type"].iloc[i] == "transcript":
        transcript_line = patches.Rectangle((start, strand), length, 0.02, facecolor="#505050", zorder=3)
        annotation_figures.append(transcript_line)
        start_figure = patches.Rectangle((start, strand - 0.045), 90, 0.1, facecolor="#505050", zorder=3)
        annotation_figures.append(start_figure)
        end_figure = patches.Rectangle((stop, strand - 0.045), 90, 0.1, facecolor="#505050", zorder=3)
        annotation_figures.append(end_figure)
    
    # else statement used to draw exons     
    else:
        exons = patches.Rectangle((start, strand - 0.045 ), length, 0.1, facecolor="#505050", zorder=3)
        annotation_figures.append(exons)
    
# adding all annotation figures to the annotation plot
for figure in annotation_figures:
    ax[4].add_patch(figure)
