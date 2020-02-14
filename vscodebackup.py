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
dst_path = dst_path[0:3]

copytree(full_path, dst_path)
make_archive("vscodebackup.zip", 'zip', "dst_path\.vscode")
rmtree("dst_path\.vscode")