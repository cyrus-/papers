import ace, ace.python as py, examples.fp as fp

def Tree(name, a):
  t = fp.Datatype(name)
  t.cases = {
    'Empty': fp.unit,
    'Leaf': a,
    'Node': fp.tuple(t, t)
  }
  t.close()
  return t

DT = Tree('DT', py.dyn)

@ace.fn(py.Base(trailing_return=True))[[DT]]
def depth_gt_2(t):
  t.case({
    DT.Node(DT.Node(_), _): True,
    DT.Node(_, DT.Node(_)): True,
    _: False
  })

@ace.fn(py.Base(main=True))[[]]
def __main__():
  my_lil_tree = DT.Node(DT.Empty, DT.Empty)
  my_big_tree = DT.Node(my_lil_tree, my_lil_tree)
  assert not depth_gt_2(my_lil_tree)
  assert depth_gt_2(my_big_tree)