class Ptr(ace.ActiveType):
  def __init__(self, addr_space, t):
    self.addr_space = addr_space
    self.t = t

  def translate_type(self, context):
    t_x = self.t.translate_type(context)
    return target.Ptr(self.addr_space, t_x)
        
  def type_Subscript(self, context, node):
    slice_t = context.type(node.slice)
    if isinstance(slice_t, Integer):
      return self.t
    else:
      raise ace.TypeError('<error message>', node)
       
  def translate_Subscript(self, context, node):
    value_x = context.translate(node.value)
    slice_x = context.translate(node.slice)
    return context.target.Subscript(value_x, slice_x)

  def type_BinOp_left(self, context, node):
    if isinstance(node.operator, ast.Add):
      right_t = context.type(node.right)
      if isinstance(right_t, Integer):
        return self
    elif isinstance(node.operator, ast.Sub):
      right_t = context.type(node.right)
      if self == right_t:
        return ptrdiff_t
    raise ace.TypeError('<error message>', node)

  def translate_BinOp_left(self, context, node):
    left_x = context.translate(node.left)
    right_x = context.translate(node.right)
    return context.target.BinOp(left_x, 
      node.operator, right_x)

  # type_BinOp_right and translate_BinOp_right 
  # (not shown) are symmetric