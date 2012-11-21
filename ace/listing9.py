import ace, ace.astx as astx

class PtrType(ace.Type):
  def __init__(self, T, addr_space):
    self.target_type = T
    self.addr_space = addr_space
        
  def resolve_Subscript(self, context, node):
    slice_type = context.resolve(node.slice)
    if isinstance(slice_type, IntegerType):
      return self.target_type
    else:
      raise TypeError('<error message>', node)
       
  def translate_Subscript(self, context, node):
    value = context.translate(node.value)
    slice = context.translate(node.slice)
    return astx.copy_node(node, 
      value=value, slice=slice,    
      code=value.code + '[' + slice.code + ']')
      
  # ...
   
class GlobalPtrType(PtrType):
  def __init__(self, T):
    PtrType.__init__(self, T, '__global')
