import pyttsx3

f=open('1.txt','r')
line=f.readline()
engine=pyttsx3.init()
while line:
    line=f.readline()
    print(line,end=' ')
    engine.say(line)
engine.runAndWait()
f.close()