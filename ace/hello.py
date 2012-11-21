from ace.OpenCL import OpenCL, printf
 
print "Hello, compile-time world!"
 
@OpenCL.fn
def main():
    printf("Hello, run-time world!")
main = main.compile()

print "Goodbye, compile-time world!"
