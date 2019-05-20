import re
f=open('text-file-process/log_files/201811113021.log',encoding='utf8').read()
f.close()
num=re.split(r'[\s,，：:]',f)

dic={"201811113021":0}
for a in num:
    if a in dic:
        dic["201811113021"]+=1

print(dic["201811113021"])