# GPU Enabled SuperBihelix
is a boilerplate app to run portions of the patented molecular dynamics simulation, SuperBihelix, in parallel on graphics processing units (GPU) using the PyCUDA/CUDA framework.


## Table of contents
* [Motivation](#motivation)
* [Introduction](#introduction)
* [Disclaimer](#disclaimer)
* [Tech Stack](#tech-stack)
* [Project Sturcture](#project-structure)
* [Running Instructions](#running-instructions)
* [References](#references)

# Motivation
This project was created to speed up the current implementation of SuperBihelix via parallization, which is limited by it's intensive time and resource requirements. In addition, the SuperBihelix algorithm can be tweaked to search even more exaustively by searching 360 times per degree of freedom, instead of [3-5 times per degree of freedom](#introduction), but this would contribute exponentialy to the current resource bottleneck.


# Disclaimer
The code is not functional due to a pattent on the parent algorithm. This redacted repo is primarily here to showcase my work. For those interested in joining the project, please send me a message on getting more information.


# Introduction: 
The origional SuperBihelix algorithm is a pattented sturctural bioinformatics algorithm used to determine the stability various conformations (possible orientations) of G coupled protein receptors (GPCR) aka seven transmembrane (7TM) proteins. This is useful for drug researchers investigating cell signaling pathways. The analysis is done by constructing a model of the physical structure of the protein, followed by a brute force stability calculation of every single possible orientation of the protein -- the most stable of which are outputted to the researcher.

<!-- GPCR IMAGE -->
<p align="center">
  <img width="460" 
       src="https://user-images.githubusercontent.com/20344260/168345619-f4063ae9-0310-445e-957b-68390f924bdf.png">
</p>
<!-- caption -->
<p align = "center">
Source: A. Typical seven-helix bundle. B. Nearest-neighbor helix pairs highlighted by double arrows; C. The 12 helix pairs shown explicitly. from Bihelix: Towards de novo structure prediction of an ensemble of G-protein coupled receptor conformations" by Raviender Abrol, Jenelle K Bray, William A Goddard 3rd
</p>

  
  
which prompted the idea of parallel processing through the general purpose graphics processing unit (GPGPU) paradigm. 

The number of configurations analyzed is designed to reach 13 trillion for a 7TM protein, a very high number due to the three degrees of freedom taken into account for each of the 7TM protein's 7 helices (5 × 3 × 5) ^ 7 = 13.35 trillion. Right now, the algorithm is reliant on extreme computing power and days or weeks for calculations (not to mention that not all possible conformations are being examined due to adding to this bottleneck).
More can be read about the SuperBihelix algorithm in the journal article: https://www.pnas.org/doi/pdf/10.1073/pnas.1321233111

<!-- DEGREES OF FREEDOM IMAGE -->
<p align="center">
  <img width="460" 
       src="https://user-images.githubusercontent.com/20344260/168344976-70ea1aa9-042f-4be3-b030-5713ed72eca6.png">
</p>
<!-- caption -->
<p align = "center">
Coordinates specifying the orientation of a TM helix in a membrane [[1]](#1).
</p>





"...the **go to** statement should be abolished..." [[1]](#1).






# Project Sturcture
The general structure of the code is as follows:

##### main driver
superbihelix_GPU.py
##### GPCR and Helix classes
* GPCR.py 
* Helix.py

##### input files
* super.template
* angles_local.txt

##### GPU benchmark helpers
Herlp.py

1) Creates GPCR object
2) Initialites interacting helices (hard coded for now)
3) Parses protein input information
4) Formats protein helix pair input
5) GPU_setup organizes information for PyCUDA framework and sends jobs to gpu  


# Dependancies
* Python 3.7
* PyCUDA (python framework built on NVIDIA's compute unified device architecture (CUDA) framework)
* Numpy
* Pandas 
* NVIDIA GPU


# Running Instructions
Navigate to the parent directory for the project and paste the following lines into a terminal
```bash
git clone https://github.com/dmw01/SuperBihelix-GPU-public.git;
cd SuperBihelix-GPU-public;
python3 SuperBihelix_GPU.py
```

## References
<a id="1">[1]</a> 
Raviender Abrol, Jenelle K Bray, William A Goddard 3rd (2011). 
Bihelix: Towards de novo structure prediction of an ensemble of G-protein coupled receptor conformations
Proteins. 2012 Feb;80(2):505-18.

<br>

Work done under Dr. Raviender Abrol at California State University, Northridge.
