# -*- coding: utf-8 -*-
#support Chinese
#format the file by replacing ([，。：“”‘’（）《》！、；？]) with \r\n
dictionary={}
c=0
threshold=10#minimum number of duplicates
max_length=7#maximum length of word
min_length=2
string = open('input.txt','r').read()
string=unicode(string,"utf-8")
print('read file finished')
arr=string.split()

for n in range(min_length,max_length):
    for i in arr:
        for k in range (0,n):
            array=[i[u:u+n] for u in range(k, len(i), n)]
            for j in array:
                if(len(j)>=n):
                    if not j in dictionary:  
                        dictionary[j]=0
                    dictionary[j]+=1
print('lenth of dict: '+ str(len(dictionary)))

for i in dictionary.keys():
    if (dictionary[i]<threshold):
        dictionary.pop(i, None)
print('lenth of filtered dict: '+ str(len(dictionary)))

#if "abc" has 2 counts, and "abcdef" has 2 counts
#they actually refer to the same word, i.e. "abc" is in "abcdef"
#the duplicate word is "abcdef", "abc" is reduntant
for i in dictionary.keys():
    for j in dictionary.keys():
        if not i in dictionary:
            break
        if (j in i) and len(i)>len(j) and dictionary[j]==dictionary[i]:
            print ('"'+j+'"('+str(dictionary[j])+') is merged into "'+i+'"('+str(dictionary[i])+')')
            c+=1
            dictionary.pop(j, None)
print('number of merged entries: '+str(c))
print('lenth of merged dict: '+str(len(dictionary)))
f=open('result.txt','w')            
for i in dictionary.keys():
    if(dictionary[i]>=threshold):
        f.write (i.encode('utf-8')+'\t'+str(dictionary[i])+'\n')
        print(i+'\t'+str(dictionary[i]))
f.close()  
