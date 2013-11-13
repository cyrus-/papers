import ace, examples.clx as clx

@ace.fn(clx.std_base)
def map(input, output, f):
    thread_idx = get_global_id()
    output[thread_idx] = f(input[thread_idx])
    if thread_idx == 0:
    	printf("Hello, run-time world!")

print "Hello, compile-time world!"
