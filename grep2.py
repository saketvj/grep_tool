from ast import pattern
from pathlib import Path
import sys
import re





def get_files(path,files):
    
    # print(type (path))
   

    if path.is_file() and not path.is_symlink():
        files.append(path)
        

    elif path.is_dir():
        if path.name.startswith('.'):
            return
        if path.is_symlink():
            return
        for x in path.iterdir():
            get_files(x,files)




def get_arguments():
    file_error = "Error: No file with this name exist.Please give a correct file path or name.\n " \
        "Usage:python3 grep.py <flags (optional)> <pattern> <file>"
    pattern_error = "Error: Please enter a valid pattern.\nUsage: python3 grep.py <flags (optional)>  <pattern> <file>"


    known_flags = ['-r','-i','-v']
    used_flag = []
    pattern = ''
    path = ''
    args = sys.argv
    i = 1
    while i< len(args) and args[i].startswith('-') and args[i] in known_flags:
        used_flag.append(args[i])
        i+=1
    if i< len(args):
        pattern = args[i]
        i+=1
    elif i >= len(args):
        sys.exit(pattern_error)
    if i < len(args):
        path = args[i]

        # path will be returned as non so that we read from std in as no file is provided:
        
    
    return (used_flag,pattern,path)


def check_for_pattern(pattern,line,used_flags):
    selected = False

    
    if '-i' in used_flags:
        pattern = pattern.lower()
        line = line.lower()

    if pattern in line:
            selected = True

    if '-v' in used_flags:
        selected = not selected
        

    return selected


def check_for_pattern_2(pattern,line,used_flags):
    selected = False

    # print("ads")
    
    try:
        if '-i' in used_flags:
            selected = bool(re.search(pattern,line,re.IGNORECASE))
            
        elif re.search(pattern,line):
            selected = bool(re.search(pattern,line)) 
    except re.error:
        sys.exit("Error: Please enter a valid pattern.\nUsage: python3 grep.py <flags (optional)>  <pattern> <file>")

    if '-v' in used_flags:
        selected = not selected
        

    return selected


def main():
    # all your script logic here
    used_flag,pattern,path = get_arguments()
    print("Flags :" ,used_flag,"Pattern :",pattern, "Path: ",path)
    # print(len(pattern))

    # now lets get all files in path.
    if path:
        # convert the path string to path object.
        path_object = Path(path)
        files = []
        if '-r' in used_flag:
            get_files(path_object,files)
            used_flag.remove('-r')
        else :
            files.append(path_object)
        

        print(files)
        for file in files:
            try:
                with file.open('r',errors = 'ignore') as f:
                    
                    for line in f:
                        # print("N") 
                        if check_for_pattern_2(pattern,line,used_flag):
                            print(f"{file.name}+: +{line}",end = "")
            except (FileNotFoundError, IsADirectoryError):
                sys.exit("Error: No file with this name exist.Please give a correct file path or name.\n " \
        "Usage:python3 grep.py <flags (optional)> <pattern> <file>")
    else:
        # read from std input
        for line in sys.stdin:
            if check_for_pattern_2(pattern,line,used_flag):
                print(line,end="")              




if __name__ == "__main__":
    main()