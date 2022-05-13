# GPU Enabled SuperBihelix
is a boilerplate app to run portions of the patented molecular dynamics simulation, SuperBihelix, in parallel on graphics processing units (GPU) using the PyCUDA/CUDA framework.

# Disclaimer
The code is not functional due to a pattent on the parent algorithm, and because the project had it's timeline extended drastically after deep analysis of the project's approach to the problem. This repo is primarily here as a jumping off point for the student picking up the project.

# Introduction: SuperBihelix
is a pattented sturctural bioinformatics algorithm used to determine the stability of G coupled protein receptors (GPCR) or seven transmembrane proteins (7TM) protein's conformations (possible orientations). This is done by constructing a model of the physical structure of the protein, followed by a brute force stability calculation of every single possible orientation of the protein, the most stable of which are outputted to the researcher. The number of configurations is designed to reach 13 trillion for a 7TM protein ((5 × 3 × 5) ^ 7), which prompted the idea of parallel processing through the general purpose graphics processing unit (GPGPU) paradigm.
More can be read about the SuperBihelix algorithm in the journal article: https://www.pnas.org/doi/pdf/10.1073/pnas.1321233111


# Structure
The general structure of the code is as follows:

##### main driver
superbihelix_GPU.py
1) Creates GPCR object
2) Initialites interacting helices (hard coded for now)
3) Parses protein input information
4) Formats protein helix pair input
5) GPU_setup organizes information for PyCUDA framework and sends jobs to gpu  


##### GPCR class
GPCR.py
* 

# Tech stack

### PyCUDA/CUDA
### NumPy/Pandas

# Dependancies
Python 3.7
Numpy
Pandas (code omitted due to pattent)

# Running Instructions
Navigate to the parent directory for the project
```bash
git clone https://github.com/dmw01/SuperBihelix-GPU-public.git;
python3 SuperBihelix_GPU.py # (angles.txt and super.template must be in same dir)
```

Work done under Dr. Raviender Abrol at California State University, Northridge.
