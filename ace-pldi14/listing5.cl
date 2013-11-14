float abs__0_(float x) {
  return (x >= 0) ? x : -1*x;
}

kernel void map_add5_float(global float* in, 
	global float* out) {
  size_t thread_idx = get_global_id();
  out[thread_idx] = abs__0_(in[thread_idx]);
  if (thread_idx == 0) {
  	printf("Hello, run-time world!");
  }
}

int2 abs__1_(int2 x) {
  return (x.s0 >= 0) ? x : (int2)(-x.s0, x.s1);
}

kernel void map_add5_c_int(global int2* in, 
	global int2* out) {
  size_t thread_idx = get_global_id();
  out[thread_idx] = abs__1_(in[thread_idx]);
  if (thread_idx == 0) {
  	printf("Hello, run-time world!");
  }
}