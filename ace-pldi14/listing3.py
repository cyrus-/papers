from ace.OpenCL import OpenCL, get_global_id

@OpenCL.fn
def map(input, output, f):
    gid = get_global_id(0)
    output[gid] = f(input[gid])
