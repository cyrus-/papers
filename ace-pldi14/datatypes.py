class DT(object):
	pass

class DT_Empty(DT):
	def __init__(self, data):
		pass

class DT_Leaf(DT):
	def __init__(self, data):
		self.data = data

class DT_Node(DT):
	def __init__(self, data):
		self.data = data

def depth_gt_2(x):
	if isinstance(x, DT_Node):
		if isinstance(x.data[0], DT_Node):
			return True
		if isinstance(x.data[1], DT_Node):
			return True
	return False

if __name__ == "__main__":
	my_lil_tree = DT_Node(DT_Empty(), DT_Empty())
	my_big_tree = DT_Node(my_lil_tree, my_lil_tree)
	assert not depth_gt_2(my_lil_tree)
	assert depth_gt_2(my_big_tree)