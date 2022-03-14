This is the README.md file for Ana and Sayo's 20.440 project. 


Overview
-------------------------------------

This repository contains a python file "network_visualization.py" with the code necessary to 
generate the figure "4008_network.pdf". The database used for 
the code and figure is stored in "4008.pdb".

A protein can be represented as nodes and edges, where the individual amino acid residues are 
represented by nodes, and residue interactions are represented by edges. These interactions
are the summation of an "energetic" network and a "centroid" network. The energetic network
is the non-covalent interactions between all the residues, and the centroid network is the
interactions driven by hydrophobic packing. 

"network_visualization.py" is a script that takes the "4008.pdb" file and outputs all the Cas9
residues, the sgRNA, and the target DNA as nodes in a network. Then, it calculcates the 
centroid network for the Cas9 residues and outputs it as edges in the network.

The database employed comes from: 

Nishimasu, H., Ran, F. A., Hsu, P. D., Konermann, S., Shehata, S. I., Dohmae, N., Ishitani, 
R., Zhang, F., & Nureki, O. (2014). Crystal structure of Cas9 in complex with guide RNA and 
target DNA. Cell, 156(5), 935–949.

The basis for the analytical methods comes from: 

Gaiha, G. D., Rossin, E. J., Urbach, J., Landeros, C., Collins, D. R., Nwonu, C., ... 
& Walker, B. D. (2019). Structural topology defines protective CD8+ T cell epitopes in the 
HIV proteome. Science, 364(6439), 480-484.


Data
-------------------------------------

The data was generated by ...

The data used can be found in 4008.pdb.


Folder Structure
-------------------------------------

This repository only contains one folder where all the python scripts, data files, and 
outputs are located.


Installation
-------------------------------------

In order to run the code, the user needs to have an IDE that can run python scripts. The
user also must also have "4008.pdb" in the same folder as the python script.

The packages necessary are:
- 

