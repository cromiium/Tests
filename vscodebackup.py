import os
from shutil import copytree
from shutil import make_archive
from shutil import rmtree
from shutil import which 
#copyfile()
dirpath = which("cmd")
harddrive = dirpath[0:3] + "Users\\"   #* Narrows down the search for the for loop; In case there are multiple hard drives and ignores things outside of "\Users\"
#print(dirpath)
#print(harddrive)
temp_list = []
for root, dirs, files in os.walk(harddrive):
    for name in dirs:
        if name == ".vscode":
            temp_list.append(os.path.abspath(os.path.join(root, name)))
        
full_path = temp_list[0]
dst_path = os.getcwd()
dst_path = dst_path[0:3] + "\\vscodebackup" #TODO: I think I need to clean up the formatting of the dst but it works for now

#TODO: Add a check for if the file exists and rm tree the old file to make room for the new file. (or maybe add a date at the end)
copytree(full_path, dst_path)
print("Copy Successful")
'''
make_archive("E:\\vscodebackup", 'zip', "dst_path\\vscodebackup") #TODO: no archive is made. not sure what to do about that
print("Archive Successful")
rmtree("dst_path\.vscode") #TODO: since the make_archive() doesn't go through, I don't think this goes through either
print("Cleanup Successful")
'''