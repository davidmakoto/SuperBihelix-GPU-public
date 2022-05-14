import pycuda.driver as drv 
import pycuda.gpuarray as gpuarray
import pycuda.driver as cuda
import pycuda.autoinit
import numpy as np
from pycuda.compiler import SourceModule

ker = SourceModule("""
__global__ void parent_kernel_function(float *a, float *outputArray) {
    int idx = blockIdx.x;
    float factorialAnswer = 1;

    for (int localFactorialValue = a[idx]; localFactorialValue > 0; localFactorialValue--)
        factorialAnswer *= localFactorialValue;     // factorial

    //outputArray[idx] = idx;
    outputArray[idx] = sqrtf(factorialAnswer);      // square root
}


__global__ void helix_pair_energy (float *phi1, float *theta1, float *eta1, float *hpc1, float *phi2, float *theta2, float *eta2, float *hpc2, float *out) {
    int idx = blockIdx.x;
    out[idx] = idx;
}


""")
