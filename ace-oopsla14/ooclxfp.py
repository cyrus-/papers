import examples.clx as clx, examples.fp as fp, 
  examples.oo as oo

A = clx.Struct('A', {'x': clx.int})
B = fp.Record('B', {'y': clx.float})
C = oo.Prototypic('C', A, B)

@ace.fn(clx.base, clx.c99)
def test(input : C):
  return input.x + input.y