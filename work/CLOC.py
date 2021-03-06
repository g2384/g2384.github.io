import glob
from os.path import isfile
import os, sys
import re

global includedFileType, currentPath
global codeLine, emptyLine, commentLine, nonCodeLine, totalLine, charLength, nonWhiteSpaceLength
global excludedFolder, excludedFileType
global doPrintFileName,doCountNonCount

def findAllFiles(path,all_file): # get all files in this dir, including subfolders
    global excludedFolder, excludedFileType
    for fn in glob.glob( path + os.sep + '*' ):
        fn2 = fn.replace(currentPath, "")
        if os.path.isdir( fn ):
            excluded = False
            for s in excludedFolder:
                if(s in fn2):
                    excluded = True
                    break
            if excluded:
                return all_file
            all_file = findAllFiles( fn , all_file)
        else:
            excluded = False
            for s in excludedFolder:
                if(s in fn2):
                    excluded = True
                    break
            if excluded:
                return all_file
            filename, file_extension = os.path.splitext(fn2)
            if(file_extension not in excludedFileType):
                all_file.append(fn)
    return all_file

def start(includedFileType, exclude_file, excludeFileName):
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
    if doPrintFileName:
        print("=======\nFILE:")    
    if len(includedFileType)>0:
        for f in all_file:
            excluded = False
            f_name, f_ext = os.path.splitext(f)
            if SubstringIsInList(exclude_file, f):
                break
            if SubstringIsInList(excludeFileName, f_name):
                continue
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
    print("found "+str(n)+" files")

def SubstringIsInList(arr, string):
    if len(arr) == 0:
        return False
    for s in arr:
        if len(s) == 0:
            continue
        if string.find(s) >= 0:
            return True
    return False

def count(arr):
    global codeLine, emptyLine, commentLine, nonCodeLine, totalLine, charLength, nonWhiteSpaceLength
    totalLine+=len(arr)
    for i in arr:
        try:
            charLength += len(i)
            s = i.decode('utf-8')
            chars = re.sub(r'[ \t\r\n]+','',s)
            nonWhiteSpaceLength += len(chars)
            if(len(chars) == 0):
                emptyLine += 1
                continue
            if(chars.startswith('//') or chars.startswith('/*')):
                commentLine += 1
                continue
            chars = re.sub(r'[^0-9a-zA-Z]', '', chars)
            if(len(chars) == 0):
                nonCodeLine += 1
                continue
            codeLine += 1
        except:
            print("cannot analyse line:")
            print(i)
            return

def CalculatePercentage(a, b, r):
    return round(a/b * 100, r)

def printResult():
    global doCountNonCount, codeLine, emptyLine, commentLine, nonCodeLine, totalLine
    if not doCountNonCount:
        codeLine += nonCodeLine
    print("code: " + str(codeLine) + "(" + str(CalculatePercentage(codeLine, totalLine, 2)) + "%)")
    print("empty: " + str(emptyLine) + "(" + str(CalculatePercentage(emptyLine, totalLine, 2)) + "%)")
    print("comment: " + str(commentLine) + "(" + str(CalculatePercentage(commentLine, totalLine, 2)) + "%)")

    if doCountNonCount:
        print("non-code: " + str(nonCodeLine) + "(" + str(CalculatePercentage(nonCodeLine, totalLine, 2)) + "%)")
    print("total: " + str(totalLine))
    print("total chars: " + str(charLength))
    print("total non-whitespace: " + str(nonWhiteSpaceLength) + "(" + str(CalculatePercentage(nonWhiteSpaceLength, charLength, 2)) + "%)")

if __name__ == "__main__":
    """ cmd:
     -t: specify the type of target files. (Optional)
          e.g. -t[cpp,h] will find all keywords in .cpp file and .h file
          acceptable syntax: -t[cpp,h], -t[cpp, h], -t[.cpp, .h]
          
     -x: exclude types of target files.
     
     -i: ignore file names
         e.g. -i[ing] will ignore all files which have 'ing'
     
     -if: ignore folders
     
     -p: print info.
         Parameters:
             file: file path
             nonCode: separate code and non-code
         e.g.: -p[file]

    example of non-code lines:
        '{'
        '});'
        '[{'

    TODO: support /* */, multi line comments, but exclude string "/* */"
          
    in Linux, place this file in your code folder,
    type the following line in terminal
      python CLOC.py -t[cs] -p[nonCode]
    """

    # in windows, place this file in your code folder.
    # use Python IDLE to open this file.
    # use the following line to give commands.
    # sys.argv = ["anything.py", '-m', "-f[detectcolor]", '-i', "-t[cpp,h]"]
    sys.argv = ["anything.py",
                "-t[cs]",
                "-x[g.cs g.i.cs]",
                "-if[Debug, Resources, Properties, Release]",
                "-p[nonCode]"]
    global includedFileType, excludedFolder, doPrintFileName, doCountNonCount
    global codeLine, emptyLine, commentLine, nonCodeLine, totalLine, charLength, nonWhiteSpaceLength
    codeLine = 0
    emptyLine = 0
    commentLine = 0
    nonCodeLine = 0
    totalLine = 0
    charLength = 0
    nonWhiteSpaceLength = 0
    doPrintFileName = True
    doCountNonCount = False
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
        a = s.find('-i[')
        excludeFileName = []
        if a >= 0:
            b = s.find(']', a)
            i = s[a+3: b]
            excludeFileName = re.split('[^a-z0-9A-Z]+', i)
            for i in range(len(excludeFileName)):
                    excludeFileName[i] = excludeFileName[i]
            print("excluded files if name contains: " + ", ".join(excludeFileName))
        a = s.find('-if[')
        excludedFolder = []
        if a >= 0:
            b = s.find(']', a)
            i = s[a+4: b]
            excludedFolder = re.split('[^a-z0-9A-Z\\\/\.]+', i)
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
            if "noncode" in print_setting:
                doCountNonCount = True
        start(includedFileType, excludedFileType, excludeFileName)
    printResult()
