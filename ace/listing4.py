from listing3 import map
from ace.OpenCL import global_ptr, double, int

@OpenCL.fn
def add5(x):
    return x + 5

A = global_ptr(double); B = global_ptr(int)
map_add5_dbl = map.compile(A, A, add5.ace_type)
map_add5_int = map.compile(B, B, add5.ace_type)
