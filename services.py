import psutil
c=0
for process in psutil.process_iter ():
    c=c+1
    ID = process.pid # ID of the process
    Name = process.name () # Name of the process
    Status = process.status()
    print ("Process ID =", ID ,",","Process name =", Name ,",","Status = ", Status)
print ("\nTotal number of running process are ", c)