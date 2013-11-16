import ace, ace.python as py, examples.fp as fp

def Tree(a):
	t = fp.Datatype()
	t.cases = {
		'empty': fp.unit,
		'leaf': a,
		'node': fp.tuple(t, t)
	}
	t.close()
	return t

DT = Tree(py.dyn)

@ace.fn(py.Base(trailing_return=True))[[DT]]
def depth_gt_2(t):
	t.case({
		dt.node(dt.node(_), _): True,
		dt.node(_, dt.node(_)): True,
		_: False
	})

@ace.fn(py.Base(main=True))[[]]
def __main__():
	my_lil_tree = dt.node(dt.empty, dt.empty)
	my_big_tree = dt.node(my_lil_tree, my_lil_tree)
	assert not depth_gt_2(my_lil_tree)
	assert depth_gt_2(my_big_tree)