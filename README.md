# GPU Enabled SuperBihelix
is a boilerplate app to run portions of the patented molecular dynamics simulation, SuperBihelix, in parallel on graphics processing units (GPU) using the PyCUDA/CUDA framework.

# SuperBihelix
is a pattented sturctural bioinformatics algorithm used to determine the stability of G coupled protein receptors (GPCR) or seven transmembrane proteins (7TM) protein's conformations (possible orientations). This is done by constructing a model of the physical structure of the protein, followed by a brute force stability calculation of every single possible orientation of the protein, the most stable of which are outputted to the researcher. The number of configurations is designed to reach 13 trillion for a 7TM protein ((5 × 3 × 5) ^ 7), which prompted the idea of parallel processing through the general purpose graphics processing unit (GPGPU) paradigm.
More can be read about the SuperBihelix algorithm in the journal article: https://www.pnas.org/doi/pdf/10.1073/pnas.1321233111

Unfourtinely, portions of the code were omitted because the analysis pipeline that SuperBihelix belongs to is pattented by a number of Cal Tech faculty. 

# PyCUDA/CUDA vs GPGPU 

# Structure
The general structure of the code is as follows:


# Running Instructions

Work done under Dr. Raviender Abrol at California State University, Northridge.
