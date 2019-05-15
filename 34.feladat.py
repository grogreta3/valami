import sys
filename= sys.argv[1]
source=open(filename,'').read()+'\n'
compile(source,filename,'exec')
print('Syntax is valid')
