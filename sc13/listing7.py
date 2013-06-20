from ace.OpenCL import OpenCL
import ace.astx as astx

plus = OpenCL.fn.from_str("""
def plus(a, b):
    return a + b
""")

add5_ast = astx.specialize(plus.ast, b=5)
add5 = OpenCL.fn.from_ast(add5_ast)
