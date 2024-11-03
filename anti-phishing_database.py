import subprocess

def print_hello_world():
    # Run a simple echo command to print "Hello World" in the terminal
    subprocess.run("echo 'Hello World'", shell=True)

# Execute the function
print_hello_world()
