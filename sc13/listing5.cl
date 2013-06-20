#pragma OPENCL EXTENSION cl_khr_fp64 : enable

double add5(double x) {
    return x + 5;
}

__kernel void map_add5_dbl(
  __global double* input, 
  __global double* output) 
{
    size_t gid;
    gid = get_global_id(0);
    output[gid] = add5(input[gid]);
}

int add5__1(int x) {
    return x + 5;
}

__kernel void map_add5_int(
  __global int* input,
  __global int* output)
{
    size_t = gid;
    gid = get_global_id(0);
    output[gid] = add5__1(input[gid]);
}
