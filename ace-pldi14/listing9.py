class Cplx(ace.ActiveType):
  def __init__(self, t):
    if not isinstance(t, Numeric):
      raise ace.InvalidTypeError("<error message>")
    self.t = t

  def type_Attribute(self, context, node):
    if node.attr == 'ni' or node.attr == 'i':
      return self.t
    raise ace.TypeError("<error message>", node)

  def trans_Attribute(self, context, target, node):
    value_x = context.trans(node.value)
    a = 's0' if node.attr == 'ni' else 's1'
    return target.Attribute(value_x, a)

  def type_BinOp_left(self, context, node):
    return self._type_BinOp(context, node.right)

  def type_BinOp_right(self, context, node):
    return self._type_BinOp(context, node.left)

  def _type_BinOp(self, context, other):
    other_t = context.type(other)
    if isinstance(other_t, Numeric):
      return Cplx(c99_binop_t(self.t, other_t))
    elif isinstance(other_t, Cplx):
      return Cplx(c99_binop_t(self.t, other.t))
    raise ace.TypeError("<error message>", other)

  def trans_BinOp(self, context, target, node):
    r_t = context.type(node.right)
    l_x = context.trans(node.left)
    r_x = context.trans(node.right)
    make = lambda a, b: target.VecLit(
      self.trans_type(self, target), a, b)
    binop = lambda a, b: target.BinOp(
      a, node.operator, b)
    si = lambda a, i: target.Attribute(a, 's'+str(i))
    if isinstance(r_t, Numeric):
      return make(binop(si(l_x, 0), r_x), si(r_x, 1))
    elif isinstance(r_t, Cplx):
      return make(binop(si(l_x, 0), si(r_x, 0)),
        binop(si(l_x, 1), si(r_x, 1)))

  @classmethod
  def type_New(cls, context, node):
    if len(node.args) == 2:
      t0 = context.type(node.args[0])
      t1 = context.type(node.args[1])
      return cls(c99_promoted_t(t0, t1))
    raise ace.TypeError("<error message>", node)

  @classmethod
  def trans_New(cls, context, target, node):
    cplx_t = context.type(node)
    x0 = context.trans(node.args[0])
    x1 = context.trans(node.args[1])
    return target.VecLit(cplx_t.trans_type(target), 
      x0, x1)

  def trans_type(self, target):
    return target.VecType(self.t.trans_type(target),2)