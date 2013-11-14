import listing1, listing2, ace, examples.clx as clx

T1 = clx.Ptr(clx.global_, clx.float)
T2 = clx.Ptr(clx.global_, clx.cplx(clx.int))
TF = listing2.negate.ace_type

try: map_neg_f32 = listing1.map[[TF, T1, T1]]
except ace.TypeError as e: print e.full_msg
map_neg_f32 = listing1.map[[T1, T1, TF]]
map_neg_ci32 = listing1.map[[T2, T2, TF]]