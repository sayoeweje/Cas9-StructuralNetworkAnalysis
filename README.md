Overview
-------------------------------------
This repository contains a script (network_visualization.py) that generates a network 
representation of the Cas9 protein (4008_network.pdf) when bound to a single guide RNA 
(sgRNA) and its target DNA. The structural information is derived from a pdb file 
(4oo8.pdb) that details a crystal structure reported in:

Nishimasu, H., Ran, F. A., Hsu, P. D., Konermann, S., Shehata, S. I., Dohmae, N., Ishitani, 
R., Zhang, F., & Nureki, O. (2014). Crystal structure of Cas9 in complex with guide RNA and 
target DNA. Cell, 156(5), 935–949.

The analysis is inspired by the work of Gaiha et al (citation below), who generated a method
for representing a protein as nodes and edges, where the individual amino acid residues are 
represented by nodes, and residue interactions are represented by edges. These interactions
are the summation of an "energetic" network and a "centroid" network. The energetic network
is the non-covalent interactions between all the residues, and the centroid network is the
interactions driven by hydrophobic packing (where closer residues are considered to be more
packed). 

Gaiha, G. D., Rossin, E. J., Urbach, J., Landeros, C., Collins, D. R., Nwonu, C., ... 
& Walker, B. D. (2019). Structural topology defines protective CD8+ T cell epitopes in the 
HIV proteome. Science, 364(6439), 480-484.

network_visualization.py is a script that takes the 4008.pdb file and outputs all the Cas9
residues, the sgRNA, and the target DNA as nodes in a network. Then, it calculcates the 
centroid network for the Cas9 residues and outputs it as edges in the network. The basis for 
the analytical methods comes from Nishimasu et al (cited above). 

Data
-------------------------------------
Purified Cas9-sgRNA-DNA complex was crystallized and analyzed via X-ray diffraction to 
resolve it. The protein structral data was downloaded directly from The Protein Database 
in .pdb format.

Folder Structure
-------------------------------------

data: Contains .csv file containing data describing the activity of a library of Cas9 mutants
generated by Spencer et al (citation below). Will be used partially for validation and partially
for training in future work on this project. 

Spencer, J. M., & Zhang, X. (2017). Deep mutational scanning of S. pyogenes Cas9 reveals important 
functional domains. Scientific reports, 7(1), 1-14.

figures: Contains surface and cartoon representations of Cas9-sgRNA-DNA complex (from Nishimasu et 
al), along with network representation generated by code. Color code for surface and cartoon 
representations:
- Blue - RuvC domain
- Green - Bridge helix
- Light gray - REC1
- Dark gray - REC2
- Pink - HNH domain
- Orange - PAM interacting domain
- Red - sgRNA
- Yellow - Target DNA

pdb: Contains pdb file analyzed (4oo8.pdb)
src: Contains source code for project (currently just network_visualization.py)


Installation
-------------------------------------

To run the code, the user needs to have an IDE that can run python scripts. The
user also must also have 4008.pdb in the same folder as the python script.

The packages necessary are:
Bio version 1.3.3
ipython version 8.1.1
matplotlib version 3.5.1
networkx version 2.6.3
numpy version 1.21.2

