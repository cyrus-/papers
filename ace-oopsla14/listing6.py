from ace.OpenCL import OpenCL, int, double, long

@OpenCL.fn
def threshold_scale(x, scale):
    if x <= 0:
        y = 0
    else:
        y = scale * x
    return y

f = threshold_scale.compile(int, double)
g = threshold_scale.compile(int, long)
assert f.return_type == double
assert g.return_type == long
