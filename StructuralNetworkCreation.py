#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy as sp
from pylab import *
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import cm
import networkx as nx
import seaborn as sns
import pandas as pd  
import collections
from IPython.display import clear_output
import random
from Bio.PDB.PDBParser import PDBParser
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches


# In[2]:


parser = PDBParser()
structure_id = "Cas9"
filename = "4oo8.pdb"
structure = parser.get_structure(structure_id, filename)

model = structure[0]
protein = model["A"]
guide = model["B"]
target_DNA = model["C"]


# In[3]:


graph = nx.Graph()
locations = []
for i in range(len(protein)):
    try:
        residue = protein[i+3]
        ca = residue["CA"].get_vector()
        residue_info = [residue.get_resname()+str(i+3), ca[0], ca[1], ca[2]]
        locations.append(residue_info)
        graph.add_node(residue.get_resname()+str(i+3), pos=(ca[0], ca[1]), color='gray')
    except:
        print("Cas9 Residue "+ str(residue) + ": This residue appears to be missing")
        
for j in range(len(guide)):
    try:
        nucleotide = guide[j+1]
        p = nucleotide["P"].get_vector()
        nucleotide_info = [nucleotide.get_resname()+str(j+1), p[0], p[1], p[2]]
        locations.append(nucleotide_info)
        graph.add_node(nucleotide.get_resname()+str(j+1), pos=(p[0], p[1]), color='orange')
    except:
        print("sgRNA Base "+ str(nucleotide) + ": This base appears to be missing")

for k in range(len(target_DNA)):
    try:
        nucleotide = target_DNA[k+1]
        p = nucleotide["P"].get_vector()
        nucleotide_info = [nucleotide.get_resname()+str(k+1), p[0], p[1], p[2]]
        locations.append(nucleotide_info)
        graph.add_node(nucleotide.get_resname()+str(k+1), pos=(p[0], p[1]), color='green')
    except:
        print("Target DNA Base Pair "+ str(nucleotide) + ": This base appears to be missing")

for x in range(len(locations)):
    residue = locations[x]
    for y in range(len(locations)):
        residue_test = locations[y]
        distance = np.sqrt((float(residue_test[1])-float(residue[1]))**2
                           + (float(residue_test[2])-float(residue[2]))**2 
                           + (float(residue_test[3])-float(residue[3]))**2) 
        if distance < 8.5 and abs(x-y) > 1:
            graph.add_edge(residue[0], residue_test[0], weight=distance)


# In[4]:


fig = figure(num=1, figsize=(10, 15), dpi=300)
ax  = fig.add_subplot(111)
pos = nx.get_node_attributes(graph,'pos')
color = nx.get_node_attributes(graph, 'color')
cmap = plt.cm.coolwarm
edges, weights = zip(*nx.get_edge_attributes(graph, 'weight').items())
g = nx.draw_networkx(graph, pos, node_size = 20, with_labels = False, 
                     node_color = color.values(), edge_color=weights, edge_cmap=cmap)

handles, labels = ax.get_legend_handles_labels()
handles.append(mpatches.Patch(color='grey',label='Cas9 residues'))
handles.append(mpatches.Patch(color='orange',label='sgRNA'))
handles.append(mpatches.Patch(color='green',label='Target DNA strand'))
ax.set_axis_off()
ax.set_title("2D Representation of Cas9 Structural Network")
ax.legend(handles=handles, loc='best')
ax.margins(x=0, y=0)

norm = mpl.colors.Normalize(vmin=0,vmax=8.5)
fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, 
             orientation='horizontal', location='bottom', 
             label='Distance between Cas9 residues (Angstroms)', pad=0)

plt.savefig("2D Representation of Cas9 Structural Network.pdf", bbox_inches = 'tight',
    pad_inches = 0)


# In[ ]:




