import subprocess

def run_command(command):
    """
    Run a shell command on the Linux terminal.
    
    :param command: str, the shell command to run
    :return: str, the output of the command
    """
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode == 0:
        return result.stdout
    else:
        print("Error:", result.stderr)
        return None

# Example automated tasks
def automate_tasks():
    print("Updating package lists...")
    run_command("sudo apt update")

    print("Upgrading installed packages...")
    run_command("sudo apt upgrade -y")

    print("Listing all files in the home directory...")
    output = run_command("ls ~")
    if output:
        print("Home Directory Files:\n", output)

    print("Checking disk usage...")
    output = run_command("df -h")
    if output:
        print("Disk Usage:\n", output)

# Run the automation
automate_tasks()
