import listing1, listing2, examples.clx as clx

T1 = clx.Ptr(clx.global_, clx.float)
T2 = clx.Ptr(clx.global_, clx.cplx(clx.int))
TF = listing2.thresh_dbl.ace_type

map_add5_float = listing1.map[[T1, T1, TF]]
map_add5_c_int = listing1.map[[T2, T2, TF]]
