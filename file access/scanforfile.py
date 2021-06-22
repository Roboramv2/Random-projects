import os

p = 'Projects'   #path to explore
filename = 'index.txt'   #name of index file

def checkgit(p):
    repos = []
    pname = p.split('/')
    pname = pname[-1]
    for f2 in os.scandir(p):
        if f2.name == ".git":
            repos.append(pname)
        else:
            if f2.is_dir():
                checkgit(p+'/'+f2.name, repos)
    return repos

def checkfull(repos, name):        
    rep = []
    for n in repos:
        try:
            for f in os.scandir(p+"/"+n):
                nam = f.name
                nam = nam.lower()
                if nam == name:
                    rep.append(n)
        except:
            for f in os.scandir(p):
                if f.is_dir():
                    for f2 in os.scandir(p+"/"+f.name):
                        if f2.name == n:
                            nam = f.name
                            nam = nam.lower()
                            if nam == name:
                                rep.append(n)
    return rep

for f1 in os.scandir(p):
    if f1.is_dir():
        repos = checkgit(p+"/"+f1.name, repos)
rep = checkfull(repos, 'readme.md')
r = list(set(repos) - set(rep))
print(r)

# index = open(t+'/'+filename, "w")
# explore(index, p)
# index.close()