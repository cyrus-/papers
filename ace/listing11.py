class ReduceLIF(ModelNode):
  """Base class for spiking neuron models."""
  def in_model_code(self, g): # g is the code generator
    "idx_state = idx_model + count*" << g
    "(realization_n - realization_start)" << g
    self.insert_hook("read_incoming", g)
    self.insert_hook("read_state", g)
    self.insert_hook("calculate_inputs", g)
    self.insert_hook("state_calculations", g)
    self.insert_hook("spike_processing", g)
  # ...
