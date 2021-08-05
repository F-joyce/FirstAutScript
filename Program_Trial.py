import os

DIRECTORY = os.getcwd()

###The script start and use the process chosen on each file in a chosen folder,
###Default is current folder



def ConvertIterator(process, FOLDER_PATH):
    """First argument is a string of the complete process name (example.py)
    the second is the string of the absolute or relative path"""
    for file in os.listdir(FOLDER_PATH):
        filename = os.fsdecode(file)
        os.system(f'python {process} {filename}')


def CreateList8BitFiles(FOLDER_PATH):
    """Creates a list of file names with 8 bit in name"""
    List = []
    for file in os.listdir(FOLDER_PATH):
        filename = os.fsdecode(file)
        if "8bit" in filename:
            List.append(filename)

    return List

def CreateListTuplesToMerge(LIST):
    ListTuples = []
    for name in range(len(LIST)):
        for name2 in range(name+1, len(LIST)):
            if LIST[name][:27] == LIST[name2][:27]:
                ListTuples.append((LIST[name], LIST[name2]))

    return ListTuples

def MergeIterator(LIST, process = 'merge.py', FOLDER_PATH = os.getcwd()):
    """First argument is a string of the complete process name (example.py)
    the second is the string of the absolute or relative path"""
    for couple in LIST:
        os.system(f'python {process} {couple[0]} {couple[1]}')



ConvertIterator("flat_bandpass_clean2.py", DIRECTORY)

L = CreateList8BitFiles(DIRECTORY)

ListTuples = CreateListTuplesToMerge(L)

MergeIterator(ListTuples, 'merge.py', DIRECTORY)

