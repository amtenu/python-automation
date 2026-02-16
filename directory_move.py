import os
#low level coding
#check if dir1 exists if not create ir
dest_dir=os.path.join(os.getcwd(),"dir1")
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

#make src and destination
src_file=os.path.join(os.getcwd(),"sample data","README.md")
dest_dir=os.path.join(os.getcwd(),"dir1","README.md")

#move
os.rename(src_file,dest_dir)
