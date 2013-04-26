from ace.OpenCL import OpenCL, printf
 
print "Hello, compile-time world!"
 
@OpenCL.fn
def main():
	hello = "Hello, run-time world!"
    printf(hello)
main = main.compile()

print "Goodbye, compile-time world!"
