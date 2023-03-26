from folderstructure import FolderStructure


a = FolderStructure()
# for creating a folder at root level it is necessary to use create_folder() 
# which takes folder name as a argument which you want to create.
a.create_folder("abid")
a.create_folder("nitin")
a.create_folder("aaman")
a.create_folder("kasif")
a.create_folder("anil")

#Given an absolute folder path and a subfolder name, it creates a new subfolder
#node and inserts it into the binary search tree structure as a child of the
#targeted folder node.
a.create_subfolder("kasif", "kasif2")
a.create_subfolder("kasif", "kasif4")
a.create_subfolder("kasif", "kasif7")
a.create_subfolder("kasif", "kasif3")
a.create_subfolder("kasif", "kasif1")

# for deleting folder of root level we use delete_folder function with one argument which is folder name
# for deleting folder within folder we use delete_folder function with two arguments one is absolute path of folder and another is folder name.
a.delete_folder("kasif","kasif7")
a.print_subfolders("kasif")
