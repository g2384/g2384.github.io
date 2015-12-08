import glob
from os.path import isfile
import os, sys
import re

def fun(path,all_file): # get all files in this dir, including subfolders
    for fn in glob.glob( path + os.sep + '*' ):
        if os.path.isdir( fn ):
            all_file = fun( fn , all_file)
        else:
            #print fn
            all_file.append(fn)
    return all_file


tempfile="~TempFile.txt~"
file_type = ['.cpp', '.h']

def merge(tempfile, file_type): # merge all files
    file_name =  os.path.basename(sys.argv[0])
    path = os.getcwd()
    all_file = []
    all_file = fun(path,all_file)
    # print len(all_file)

    for i in range(len(all_file)):
        all_file[i] = all_file[i].replace(path, '')
        all_file[i] = all_file[i][1:]

    count=0
    with open(tempfile, "wb") as outfile:
        for f in all_file:
            f_name, f_ext = os.path.splitext(f)
            if(f!=file_name and f_ext in file_type):
                print(f)
                count +=1
                outfile.write("\r\n#UnIquE$tR|ng::"+f+"\r\n")
                with open(f, "rb") as infile:
                    outfile.write(infile.read())
    print 'merged '+str(count) + ' files'

def search(a, reg, reg2=''): # search the string a
    exact_search = False
    if reg2=='':
        exact_search = True
    for i in range(1,len(a)):
        found = False
        file_len = len(a[i])
        lines = a[i].split('\n')
        for l in range(1, len(lines)):
            pos = re.search(reg, lines[l])
            if pos <0:
                if exact_search == False:
                    pos = re.search(reg2, lines[l])
            if pos >0:
                if found == False:
                    print('\n\n===========\nFound in file "' + lines[0]+'"') 
                found = True
                found_something = True
                print('\n\n\nline '+str(l)+': ')
                if l == 1:
                    print(lines[l])
                    print(lines[l+1])
                elif l == len(lines)-1:
                    print(lines[l-1])
                    print(lines[l])
                else:
                    print(lines[l-1])
                    print(lines[l])
                    print(lines[l+1])
            
                
    return found_something

def vague_reg(inp):
    initial = ''
    endding = ''
    first = inp[0:1]
    last = inp[-1:]
    first_reg = ''
    last_reg = ''
    if(first.isdigit()):
        initial = 'num'
        first_reg = '[^0-9]'
    elif('qwertyuiopasdfghjklzxcvbnm'.find(first)>=0):
        initial = 'let'
        first_reg = '[^a-z]'
    elif('QWERTYUIOPASDFGHJKLZXCVBNM'.find(first)>=0):
        initial = 'LET'
        first_reg = '[^A-Z]'
    if('qwertyuiopasdfghjklzxcvbnm'.find(last)>=0):
        endding = 'let'
        last_reg = '[^a-z]'
    elif(last.isdigit()):
        endding = 'num'
        last_reg = '[^0-9]'
    elif('QWERTYUIOPASDFGHJKLZXCVBNM'.find(last)>=0):
        endding = 'LET'
        last_reg = '[^A-Z]'
    #print(initial, endding, first_reg, last_reg)
    return re.compile(first_reg +   inp  + last_reg)

def find(tempfile, inp, exact_search=True):
    f = open(tempfile, "r")
    s = f.read()
    a = s.split('#UnIquE$tR|ng::')
    reg = re.compile(r"""[^a-zA-Z0-9_]""" +inp + r"""[^a-zA-Z0-9_]""")
    found_something = False
    print 'looking for "' + inp + '"'
    if exact_search == False:
        search(a, reg, reg2 = vague_reg(inp))
    else:
        search(a, reg)


if __name__ == "__main__":
    """ cmd:
      -m: merge all files all update the temp file
      -f: find string, match case. 
          e.g. -f(Test), 
               'Test' gives true, 
               'AddTest' gives false, 
               '_Test' gives false, 
               'test' gives false
      -fa: find string, match case, can appear in a part of a string. 
          e.g. -fa(Test), 
               'Test' gives true, 
               'AddTest' gives true, 
               '_Test' gives true
               'test' gives false
    """
    #sys.argv = ["wordcount.py", '-m', "-f(Detector)"]
    
    sys.argv = ["wordcount.py", '-m', "-fa(Detector)", "-t(cpp,h)"]
    global file_type
    s = ''
    f = ''
    if len(sys.argv) > 1:
        for i in range(len(sys.argv)):
            if i > 0:                    
                s += sys.argv[i]
        a = s.find('-f(')
        if a >= 0:
            b = s.find(')', a)
            inp = s[a+3:b]
            f = 'f'
        a = s.find('-fa(')
        if a >= 0:
            b = s.find(')', a)
            inp = s[a+4:b]
            f = 'fa'
        a = s.find('-t(')
        if a>=0:
            b = s.find(')', a)
            i = s[a+3: b]
            file_type = re.split('[^a-z0-9A-Z]', i)
            for i in range(len(file_type)):
                file_type[i] = '.'+file_type[i]
        if s.find('-m')>=0:
            merge(tempfile, file_type)
        if f == 'f':
            find(tempfile, inp)
        elif f == 'fa':
            find(tempfile, inp, exact_search=False)
