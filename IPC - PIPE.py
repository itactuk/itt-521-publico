import os
from subprocess import Popen, PIPE

fout = open("borrar.txt","w")

cmd = "python"
if os.name == "posix":
    cmd += "3"
# Inicia el nuevo proceso
p = Popen([cmd], stdin=PIPE,stdout=fout,universal_newlines=True)
# Escribe la data
for name in ["print('Hello')", "print(5+4)", "result = 100 + 20"]:
    p.stdin.write(name+"\n")
p.stdin.write('exit(result)\n\n')
p.stdin.close()
return_code = p.wait()
print(return_code)
fout.close()
