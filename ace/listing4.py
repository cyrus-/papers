from listing3 import map
from ace.OpenCL import gptr, double, int

@OpenCL.fn
def add5(x):
    return x + 5

D = gptr(double); I = gptr(int); A = add5.ace_type
map_add5_dbl = map.compile(D, D, A)
map_add5_int = map.compile(I, I, A)
