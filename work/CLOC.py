import glob
from os.path import isfile
import os, sys
import re

global includedFileType, currentPath
global codeLine, emptyLine, commentLine, nonCodeLine, totalLine
global excludedFolder
global doPrintFileName

def findAllFiles(path,all_file): # get all files in this dir, including subfolders
    global excludedFolder
    for fn in glob.glob( path + os.sep + '*' ):
        fn2 = fn.replace(currentPath, "")
        if os.path.isdir( fn ):
            excluded = False
            for s in excludedFolder:
                if(s in fn2):
                    excluded = True
                    #print(fn)
                    break
            if excluded:
                return all_file
            all_file = findAllFiles( fn , all_file)
        else:
            #print fn
            excluded = False
            
            for s in excludedFolder:
                if(s in fn2):
                    excluded = True
                    #print(fn)
                    break
            if excluded:
                return all_file
            all_file.append(fn)
    return all_file

def start(includedFileType, exclude_file):
    global totalLine, currentPath
    file_name =  os.path.basename(sys.argv[0])
    currentPath = os.path.dirname(os.path.realpath(__file__))
    path = os.getcwd()
    all_file = []
    all_file = findAllFiles(path,all_file)
    # print len(all_file)

    for i in range(len(all_file)):
        all_file[i] = all_file[i].replace(path, '')
        all_file[i] = all_file[i][1:]

    n=0
    print("=======\nFILE:")    
    if len(includedFileType)>0:
        for f in all_file:
            excluded = False
            f_name, f_ext = os.path.splitext(f)
            for s in exclude_file:
                if s in f:
                    excluded = True
                    break
            if excluded:
                break
            if(f!=file_name and f_ext in includedFileType):
                if doPrintFileName:
                    print(f)
                n +=1
                with open(f, "rb") as infile:
                    content = infile.readlines()
                    count(content)
    else:
        for f in all_file:
            if(f!=file_name):
                n +=1
                with open(f, "rb") as infile:
                    content = infile.readlines()
                    count(content)
        if doPrintFileName:
            for f in all_file:
                print(f)
    print("=======\n")   
    print("read "+str(n)+" files")

def count(arr):
    global codeLine, emptyLine, commentLine, nonCodeLine, totalLine
    totalLine+=len(arr)
    for i in arr:
        chars = re.sub(r'[ \t\r\n]+','',i)
        if(len(chars) == 0):
            emptyLine += 1
            continue
        commentPos = chars.find('//')
        if(commentPos == 0):
            commentLine += 1
            continue
        chars = re.sub(r'[^0-9a-zA-Z]', '', chars)
        if(len(chars) == 0):
            nonCodeLine += 1
            continue
        
        codeLine += 1

def printResult():
    print("code: " + str(codeLine))
    print("empty: " + str(emptyLine))
    print("comment: " + str(commentLine))
    print("non-code: " + str(nonCodeLine))
    print("total: " + str(totalLine))

if __name__ == "__main__":
    """ cmd:
     -t: specify the type of target files. (Optional)
          e.g. -t[cpp,h] will find all keywords in .cpp file and .h file
          acceptable syntax: -t[cpp,h], -t[cpp, h], -t[.cpp, .h]
          
     -x: exclude types of target files.
     
     -i: ignore file names
     
     -if: ignore folders
     
     -p: print info. Parameters:
         file: file path
         
         e.g.: -p[file]

    example of non-code lines:
        '{'
        '});'
        '[{'
          
    in Linux, place this file in your code folder,
    type the following line in terminal
      python merge.py -m -f[void] -t[cpp,h]
    """

    # in windows, place this file in your code folder.
    # use Python IDLE to open this file.
    # the following line to give commands.
    # sys.argv = ["anything.py", '-m', "-f[detectcolor]", '-i', "-t[cpp,h]"]
    sys.argv = ["anything.py", "-t[cs]", "-x[g.cs g.i.cs]", "-if[Debug, Resources, Properties, Interface, Interfaces, Triangle]","-p[file]"]
    global includedFileType, excludedFolder, doPrintFileName
    global codeLine, emptyLine, commentLine, nonCodeLine, totalLine
    codeLine = 0
    emptyLine = 0
    commentLine = 0
    nonCodeLine = 0
    totalLine = 0
    doPrintFileName = False
    f = ''
    includedFileType = []
    if len(sys.argv) > 1:
        s = ' '+(' ').join(sys.argv)+' '
        a = s.find('-t[')
        if a >= 0:
            b = s.find(']', a)
            i = s[a+3: b]
            
            includedFileType = re.split('[^a-z0-9A-Z]+', i)
            for i in range(len(includedFileType)):
                includedFileType[i] = '.'+includedFileType[i]
            print("files types: " + ", ".join(includedFileType))
        a = s.find('-x[')
        excludedFileType = []
        if a >= 0:
            b = s.find(']', a)
            i = s[a+3: b]
            excludedFileType = re.split('[^a-z0-9A-Z\.]+', i)
            for i in range(len(excludedFileType)):
                if(excludedFileType[i].find('.') != 0):
                    excludedFileType[i] = '.'+excludedFileType[i]
            print("excluded files types: " + ", ".join(excludedFileType))
        a = s.find('-if[')
        excludedFolder = []
        if a >= 0:
            b = s.find(']', a)
            i = s[a+4: b]
            excludedFolder = re.split('[^a-z0-9A-Z\\\/]+', i)
            for i in range(len(excludedFolder)):
                if(excludedFolder[i].find('\\') != 0):
                    excludedFolder[i] = '\\'+excludedFolder[i] + "\\"
            print("excluded folders: " + ", ".join(excludedFolder))
        a = s.find('-p[')
        print_setting = []
        if a >= 0:
            b = s.find(']', a)
            i = s[a+3: b]
            print_setting = re.split('[^a-z0-9A-Z]+', i)
            for i in range(len(print_setting)):
                print_setting[i] = print_setting[i].lower()
            if "file" in print_setting:
                doPrintFileName = True
            print("excluded folders: " + ", ".join(print_setting))
        start(includedFileType, excludedFileType)
    printResult()
