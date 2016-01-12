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
global file_type

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
    
        if len(file_type)>0:
            for f in all_file:
                f_name, f_ext = os.path.splitext(f)
            
                if(f!=file_name and f_ext in file_type):
                    print(f)
                    count +=1
                    outfile.write("\r\n#UnIquE$tR|ng::"+f+"\r\n")
                    with open(f, "rb") as infile:
                        outfile.write(infile.read())
        
        else:
            for f in all_file:
                if(f!=file_name):
                    #print(f)
                    count +=1
                    outfile.write("\r\n#UnIquE$tR|ng::"+f+"\r\n")
                    with open(f, "rb") as infile:
                        outfile.write(infile.read())
             
    print 'Merged '+str(count) + ' files'

def search(a, reg, reg2=''): # search the string a
    exact_search = False
    found_something = False
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
                    print('\n\n===========\n Found in file "' + lines[0]+'"') 
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
    return re.compile(first_reg +   inp  + last_reg)

def find(tempfile, inp, exact_search = True, ignore_case = False):
    with open(tempfile, 'r') as f:
        try:
            s = f.read()
            a = s.split('#UnIquE$tR|ng::')
            if ignore_case:
                reg = re.compile(r"""[^a-zA-Z0-9_]""" +inp + r"""[^a-zA-Z0-9_]""", re.I)
            else:
                reg = re.compile(r"""[^a-zA-Z0-9_]""" +inp + r"""[^a-zA-Z0-9_]""")
            print 'Searching "' + inp + '"'
            if exact_search == False:
                found_something = search(a, reg, reg2 = vague_reg(inp))
            else:
                found_something = search(a, reg)
            if found_something == False:
                print 'Cannot find "' + inp + '"'
        except:
            print 'please execute "python merge.py -m" first'


if __name__ == "__main__":
    """ cmd:
      -m: merge all files and update the temp file.
          This command must be used when merge.py is used first time in a folder.
          It is not necessary to use this command if merge.py is not used first time. 
      -f: find string, match case. 
          e.g. -f{Test}, 
               'Test' gives true,
               'Test()' gives true, 
               'AddTest' gives false, 
               '_Test' gives false, 
               'test' gives false
      -a: find string, match case, can appear in a part of a string. 
          e.g. 'python merge.py -m -f{Test} -a -t{cpp,h}', 
               'Test' gives true,
               'Test()' gives true,
               'AddTest' gives true, 
               '_Test' gives true
               'test' gives false
      -i: ignore case. 
          e.g. 'python merge.py -m -f{void} -i -t{cpp,h}', 
               'Test' gives true,
               'test' gives true
      -t: specify the type of target files. (Optional)
          e.g. -t{cpp,h} will find all keywords in .cpp file and .h file
          acceptable syntax: -t{cpp,h}, -t{cpp, h}, -t{.cpp, .h}
          
    in Linux, place this file in your code folder,
    type the following line in terminal
      python merge.py -m -f{void} -t{cpp,h}
    """

    # in windows, place this file in your code folder.
    # use Python IDLE to open this file.
    # the following line to give commands.
    #sys.argv = ["anything.py", '-m', "-f{detectcolor}", '-i', "-t{cpp,h}"]
    #sys.argv = ["anything.py", '-m', "-f{Detector}", "-a", "-t{cpp,h}"]
    global file_type
    f = ''
    file_type = []
    if len(sys.argv) > 1:
        s = ' '+(' ').join(sys.argv)+' '
        a = s.find('-f{')
        if a >= 0:
            b = s.find('}', a)
            inp = s[a+3:b]
            f = 'f'
        a = s.find('-t{')
        if a >= 0:
            b = s.find('}', a)
            i = s[a+3: b]
            file_type = re.split('[^a-z0-9A-Z]+', i)
            for i in range(len(file_type)):
                file_type[i] = '.'+file_type[i]
        exact_search = True
        if s.find(' -a ') >= 0:
            exact_search = False
        ignore_case = False
        if s.find(' -i ') >= 0:
            ignore_case = True
        if s.find(' -m ') >= 0:
            merge(tempfile, file_type)
        if f == 'f':
            find(tempfile, inp, exact_search, ignore_case)
            
