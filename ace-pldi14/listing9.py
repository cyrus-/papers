import ace

class Ptr(ace.ActiveType):
  def __init__(self, addr_space, target_t):
    self.addr_space = addr_space
    self.target_t = target_type
        
  def type_Subscript(self, context, node):
    slice_t = context.type(node.slice)
    if isinstance(slice_t, Integer):
      return self.target_t
    else:
      raise ace.TypeError('<error message>', node)
       
  def translate_Subscript(self, context, node):
    value_x = context.translate(node.value)
    slice_x = context.translate(node.slice)
    return context.target.Subscript(value_x, slice_x)

  def type_BinOp(self, context, node):
    if node.op == ast.Add:
      right_t = context.type(node.right)
      if isinstance(right_t, Integer):
        return self
    elif node.op == ast.Sub:
      right_t = context.type(node.right)
      if (isinstance(right_t, Ptr) and 
          right_t.addr_space == self.addr_space):
        return ptrdiff_t
    else: raise ace.TypeError('<error message>', node)

  def translate_BinOp(self, context, node):
    left_x = context.translate(node.left)
    right_x = context.translate(node.right)
    return context.target.BinOp(left_x, 
      node.operator, right_x)