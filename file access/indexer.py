import os

p = 'insert path of the directory you want to index'   #path to explore
t = 'target directory to store the index in'   #folder to store the index file in
filename = 'index.txt'   #name of index file

#i is step of indentation
def makeline(txt, i):
    ind = "    " * i
    txt = ind + txt
    return txt

#i initialises as 0 for parent
def explore(file, path, i=0):
    d={}
    for f in os.scandir(path):
        if f.is_dir():
            d[f.name]='dir'
        else:
            d[f.name]='file'
    for n in d:
        if (n == '.git')or(n=='indices'):
            continue
        if d[n]=='dir':
            name = 'Folder : '+n
            m = makeline(name, i)
            file.write(m+'\n')
            i+=1
            explore(file, path+'/'+n, i)
            i-=1
        elif d[n]=='file':
            name = n.split('.')
            fil = name.pop()
            n = fil+' : '+ ('.'.join(name))
            m = makeline(n, i)
            file.write(m+'\n')

index = open(t+'/'+filename, "w")
explore(index, p)
index.close()