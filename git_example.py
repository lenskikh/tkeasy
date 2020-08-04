#test
import subprocess

process = subprocess.Popen(["git", "status"], stdout=subprocess.PIPE)
output = process.communicate()[0]
print(output)

process = subprocess.Popen(["git", "add", "."], stdout=subprocess.PIPE)
output = process.communicate()[0]
print(output)

process = subprocess.Popen(["git", "commit","-m 'minor'"], stdout=subprocess.PIPE)
output = process.communicate()[0]
print(output)

process = subprocess.Popen(["git", "push"], stdout=subprocess.PIPE)
output = process.communicate()[0]
print(output)