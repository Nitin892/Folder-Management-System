from folderstructure import FolderStructure


a = FolderStructure()
a.create_folder("abid")
a.create_folder("nitin")
a.create_folder("aaman")
a.create_folder("kasif")
a.create_folder("anil")

a.create_subfolder("kasif", "kasif2")
a.create_subfolder("kasif", "kasif4")
a.create_subfolder("kasif", "kasif7")
a.create_subfolder("kasif", "kasif3")
a.create_subfolder("kasif", "kasif1")

a.delete_folder("kasif","kasif7")
a.print_subfolders("kasif")