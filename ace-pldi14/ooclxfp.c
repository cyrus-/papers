typedef struct {
	int x;
} A;

typedef struct {
	float y;
} B;

typedef struct {
	A self;
	B proto;
} C;

float test(C input) {
	return C.self.x + C.proto.y;
}