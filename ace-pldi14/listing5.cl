float add_5__0_(float x) {
  return x + 5;
}

kernel void map_add5_float(global float* in, 
	global float* out) {
  size_t thread_idx = get_global_id();
  out[thread_idx] = add_5__0_(in[thread_idx]);
  if (thread_idx == 0) {
  	printf("Hello, run-time world!");
  }
}

int2 add_5__1_(int2 x) {
  return (int2)(x.s0 + 5, x.s1);
}

kernel void map_add5_c_int(global int2* in, 
	global int2* out) {
  size_t thread_idx = get_global_id();
  out[thread_idx] = add_5__1_(in[thread_idx]);
  if (thread_idx == 0) {
  	printf("Hello, run-time world!");
  }
}