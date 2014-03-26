tree = lambda name, a: fp.data(name, 
  lambda tree: {
    'Empty': fp.unit,
    'Leaf': a,
    'Node': fp.tuple(tree, tree)
  })

dyntree = tree(dyn)

@py
def depth_gt_2(x):
  {x : dyntree}
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