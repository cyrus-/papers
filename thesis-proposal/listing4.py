from ace.OpenCL import OpenCL, get_global_id, 
  global_ptr, double, int

@OpenCL.fn
def map(input, output, f):
    gid = get_global_id(0)
    output[gid] = f(input[gid])

@OpenCL.fn
def add5(x):
    return x + 5

A = GlobalPtrType(double); B = GlobalPtrType(int)
map_add5_dbl = map.compile(A, A, add5.ace_type)
map_add5_int = map.compile(B, B, add5.ace_type)
