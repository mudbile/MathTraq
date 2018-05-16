import os
import subprocess
import mathtraq

# commands = ['python', 'mathtraq.py', '500#0(1)1000{+/-}-50(2)60?3000(2)']

# print("starting")
# p = subprocess.Popen(commands, stdout=subprocess.PIPE, universal_newlines=True)
# for line in iter(p.stdout.readline, b''):
#     print('>>> {}'.format(line.rstrip()))
# print("done")

def printExtra(text):
    print("fart and " + text)

mathtraq.run_as_module('500#0(1)1000{+/-}-50(2)60?3000(2)', observers=[printExtra])