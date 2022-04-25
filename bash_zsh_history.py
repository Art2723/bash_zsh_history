# import history from bash to zsh
import os
import datetime
with open(f'{os.environ.get("HOME")}/.bash_history') as f:
    s=f.read()
s=s.split(sep='\n')
total=''
t=round(datetime.datetime.timestamp(datetime.datetime.now()))
for i in s:
    t +=1
    total += f": {t}:0;{i}\n"
with open(f'{os.environ.get("HOME")}/.histfile', "w") as f: # or .zsh_history
    f.write(total)
