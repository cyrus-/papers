import ace, examples.clx as clx, ast, astx

_fn = ace.fn(clx.base, clx.opencl)

scale = _fn(ast.parse("""def scale(x, s): 
	return x * s""")

negate = _fn(astx.specialize(scale.ast, "negate", 
	s=astx.parse_exp("-1"))