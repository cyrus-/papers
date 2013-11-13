import listing1, ace, examples.clx as clx

@ace.fn(clx.std_base)
def add_5(x):
    return x + 5

F = clx.Ptr(clx.global_, clx.float)
C = clx.Ptr(clx.global_, clx.cplx(clx.int))
A = add_5.ace_type

map_add5_float = listing1.map[[F, F, A]]
map_add5_c_int = listing1.map[[C, C, A]]
