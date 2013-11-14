float negate__0_(float x) {
  return x * -1;
}

kernel void map_neg_f32(global float* input, 
	global float* output) {
  size_t thread_idx = get_global_id(0);
  output[thread_idx] = negate__0_(input[thread_idx]);
  if (thread_idx == 0) {
  	printf("Hello, run-time world!");
  }
}

int2 negate__1_(int2 x) {
  return (int2)(x.s0 * -1, x.s1);
}

kernel void map_neg_ci32(global int2* input, 
	global int2* output) {
  size_t thread_idx = get_global_id(0);
  output[thread_idx] = negate__1_(input[thread_idx]);
  if (thread_idx == 0) {
  	printf("Hello, run-time world!");
  }
}