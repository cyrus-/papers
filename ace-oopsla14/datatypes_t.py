import examples.fp
__ace_base__ = fp

@datatype
def tree(a): [
  Empty,
  Node : (tree[a], tree[a]),
  Leaf : a
]

def pair_trees(x, y):
  {x, y : tree[a]]}
  with (x, y).cases:
    if Empty, Empty: 
      Empty [:m,:p]
    elif Node(x, y), Node(y): 
      Node((x, y))
    elif Leaf(x), Leaf(y): 
      Leaf((x, y))
    else:
      raise




@fp.datatype
def x(a):
  {'B': fp.unit,
   'R': y}

@fp.datatype
def y(a):
  {'B': fp.unit,
   'R': x}

@cl.struct
def hello(): {
  a : A,
  b : B
}

@cl.struct
def hello(): [
  a : A,
  b : B
]


   'Node': tuple(tree(a), tree(a))}
@fp.datatype()

@py
def depth_gt_2(x):
  {x : tree[dyn]}
  return x.case({
    DT.Node(DT.Node(_), _): True,
    DT.Node(_, DT.Node(_)): True,
    _: False
  })

@py
def __toplevel__():
  my_lil_tree = dyntree.Node(dyntree.Empty, dyntree.Empty)
  my_big_tree = dyntree.Node(my_lil_tree, my_lil_tree)
  assert not depth_gt_2(my_lil_tree)
  assert depth_gt_2(my_big_tree)