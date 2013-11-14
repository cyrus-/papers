import ace, examples.clx as clx, ast, astx

cl_fn = ace.fn(clx.base, clx.opencl)
thresh_scale = cl_fn(ast.parse("""
def thresh_scale(x, s):
	return x * s if x >= 0 else 0"""))

thresh_dbl = cl_fn(astx.specialize(thresh_scale.ast, 
	"thresh_dbl", s=ast.parse("2.0"))