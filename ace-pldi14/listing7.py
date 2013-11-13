import astx, ace, examples.clx as clx

plus = ace.fn(clx.std_base)("""def plus(a, b):
    return a + b""")
add_5_ast = astx.specialize(plus.ast, b=5)
add_5 = ace.fn(clx.std_base)(add5_ast)