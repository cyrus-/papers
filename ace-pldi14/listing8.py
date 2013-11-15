import listing1, listing2, examples.clx as clx, numpy

clx.opencl.ctx = clx.Context.for_device(0, 0)

input = numpy.ones((1024,))
d_input = clx.to_device(input)
d_output = clx.alloc(like=input)

listing1.map(d_input, d_output, listing2.negate, 
  global_size=d_in.shape)

assert (cl.from_device(d_out) == input * -1).all()