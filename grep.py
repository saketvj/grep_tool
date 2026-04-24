import sys
import re
from pathlib import Path
import os 
print("0")


# grep "" test.txt | diff test.txt - (when file name is given)
# | grep "aa" (when input comes from std inpt instead of file.) 
# ----
# input layer
# ----

# take input from files as well as std inpt and  capturing it .
# capturing the pattern.
# failure can happend if invalid file name,no std inpt and file given ., no pattern given.
# invalid pattern given ,

file_error = "Error: No file with this name exist.Please give a correct file path or name.\n " \
        "Usage:python3 grep.py <pattern> <file>"
pattern_error = "Error: Please enter a valid pattern.\nUsage: python3 grep.py <pattern> <file>"

print("1")


# give all the files in the path
def recursive_search(path):
    if path.is_file():
        file = os.path.basename(path)
        file_list.append(file)
    else :
        recursive_search(path)
    

def dispatcher(command):
    pass

def find_pattern_in_file(file_name,pattern):
    try:
        with open (file_name,'r',encoding='utf-8',newline='') as f:
            for line in f:
                # print(line)
                if pattern_search(pattern,line):
                    print(line,end="")
                    return line
                    # match_found = True
    except FileNotFoundError:
        sys.exit(file_error)
    except IsADirectoryError:
        sys.exit(file_error)
    

print(2)
def pattern_search(pattern,line):
    return pattern in line 



file_list =[]

path = Path(sys.argv[2])
recursive_search(path)
print(file_list)
# # pattern
# if len(sys.argv) > 1 :
#     pattern = sys.argv[1]
# else:
#     sys.exit(pattern_error)

# # file or std inpt processing while reading.
# match_found = False
# commands = ['-r','-v']


# if len(sys.argv) > 2:
#     if sys.argv[2] in commands:
#         # dispatcher function calls which ever function need to be called.
#         print(sys.argv[2])
#         dispatcher(sys.argv[2])
#     else :
#         if file_list file_name = sys.argv[2]
#         for file in file_list:
#         line = find_pattern _in_file(file_name,pattern,match_found)
#         if line:
#             match_found = True
#             print(line)
        


# else:
#     for line in sys.stdin:
#         # print(line)
#         if pattern_search(pattern,line):
#             print(line,end="")
#             match_found = True
#     if not match_found:
#         sys.exit(1)



# print("Asd")

# ----
# input layer
# ----

# ----
#Processing layer
# ----












# ----
# Processing layer
# ----




# ----
# Output layer
# ----








# ----
# Output layer
# ----