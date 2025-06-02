from subprocess import run
print(run(["df", "-h"],capture_output=True,text=True))