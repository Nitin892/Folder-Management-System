class FolderNode:
    def __init__(self, name):
        self.left = None
        self.password = None
        self.folder_name = name
        self.subfolders = None
        self.files = None
        self.right = None


class FileNode:
    def __init__(self, file_name):
        self.left = None
        self.file_name = file_name
        self.right = None


class FolderStructure:
    def __init__(self):
        self.__root = None

    def __set_password(self, NodeFolder):
        query = input("Do you wish to set password? (y or n):")
        if(query == 'y' or query == 'Yes'):
            password = input("Enter password")
            NodeFolder.password = password

    def __get_folder(self, path, name):
        """
        Given a path and a folder name, it searches for the corresponding
        folder node in the binary search tree structure.
        """
        temp = path
        while(temp):
            if(temp.folder_name == name):
                return temp
            elif(name < temp.folder_name):
                temp = temp.left
            else:
                temp = temp.right
        return None

    def __search_folder(self, folder_name):
        """
        Given a folder name, it searches for the corresponding
        folder node in the binary search tree structure.
        """
        temp = self.__root
        while(temp):
            if(temp.folder_name == folder_name):
                return temp
            elif(folder_name < temp.folder_name):
                temp = temp.left
            else:
                temp = temp.right
        return None

    def __traverse_sub_folders(self, start):
        """
        Helper function to traverse and print the names of all subfolders
        within a given starting folder node.
        """

        if(start != None):
            self.__traverse_folders(start.left)
            print(start.folder_name)
            self.__traverse_folders(start.right)

    def __traverse_folders(self, start):
        """
        Helper function to traverse and print the names of all folders
        within a given starting folder node.
        """

        if(start != None):
            self.__traverse_folders(start.left)
            print(start.folder_name)
            self.__traverse_folders(start.right)

    def create_folder(self, name):
        """
        Creates a new folder node with the given name and inserts it into
        the binary search tree structure.
        """
        new_folder = FolderNode(name)
        if(self.__root == None):
            self.__root = new_folder
        else:
            parent_node = None
            temp = self.__root
            while(temp):
                parent_node = temp
                if(name < temp.folder_name):
                    temp = temp.left
                elif(name > temp.folder_name):
                    temp = temp.right
                else:
                    print("Folder already exists")
                    return None

            if(name < parent_node.folder_name):
                parent_node.left = new_folder
            else:
                parent_node.right = new_folder
        self.__set_password(new_folder)
        print(f"{new_folder.folder_name} folder is created successfully")
        return new_folder

    def print_folders(self, folder_path):
        """
        Given an absolute folder path, it traverses and prints the names of all
        folders within the targeted folder node.
        This function is best applicable for root folders only.
        """
        if(folder_path == '/'):
            folder = self.__root
            self.__traverse_folders(folder)
        else:
            print("Invalid")

    def create_subfolder(self, absolute_path, name):
        """
        Given an absolute folder path and a subfolder name, it creates a new subfolder
        node and inserts it into the binary search tree structure as a child of the
        targeted folder node.
        """
        # # Split the absolute path into individual folder names
        folders = absolute_path.split('/')

        # Search for the targeted folder
        targeted_folder = self.__search_folder(folders[0])
        if targeted_folder is None:
            print(f"{folders[0]} folder not found")
            return None

        # Iterate over the remaining folder names in the path
        for index in range(1, len(folders)):
            targeted_folder = targeted_folder.subfolders
            targeted_folder = self.__get_folder(
                targeted_folder, folders[index])
            if targeted_folder is None:
                print(f"{folders[index]} folder not found")
                return None

        # Create a new folder node
        new_subfolder = FolderNode(name)

        # Insert the new folder node
        if targeted_folder.subfolders is None:
            targeted_folder.subfolders = new_subfolder
        else:
            temp = targeted_folder.subfolders
            parent_folder = None
            while temp:
                parent_folder = temp
                if name < temp.folder_name:
                    temp = temp.left
                elif name > temp.folder_name:
                    temp = temp.right
                else:
                    print("Duplicates are not allowed")
                    return None

            if name < parent_folder.folder_name:
                parent_folder.left = new_subfolder
            else:
                parent_folder.right = new_subfolder

        self.__set_password(new_subfolder)
        print(f"{new_subfolder.folder_name} folder is created successfully")
        return new_subfolder

    def print_subfolders(self, absolute_path):
        """Given an absolute folder path, it traverses and prints the names of all
        folders within the targeted folder node.
        """
        # Split the absolute path into individual folder names
        folders = absolute_path.split('/')

        # Search for the targeted folder
        targeted_folder = self.__search_folder(folders[0])
        if targeted_folder is None:
            print(f"{folders[0]} folder not found")
            return None

        # Traverse the subfolders of the targeted folder
        for index in range(1, len(folders)):
            targeted_folder = targeted_folder.subfolders
            targeted_folder = self.__get_folder(
                targeted_folder, folders[index])
            if targeted_folder is None:
                print(f"{folders[index]} folder not found")
                return None

        if targeted_folder.subfolders is None:
            print("No subfolders found")
        else:
            self.__traverse_sub_folders(targeted_folder.subfolders)

    def create_file(self, absolute_path, file_name):
        """
        Creates a new folder node with the given name and inserts it into
        the binary search tree structure.
        """
        folders = absolute_path.split('/')
        targeted_folder = self.__search_folder(folders[0])
        if targeted_folder is None:
            print(f"{folders[0]} folder not found")
            return None

        # Traverse the subfolders of the targeted folder
        for index in range(1, len(folders)):
            targeted_folder = targeted_folder.subfolders
            targeted_folder = self.__get_folder(
                targeted_folder, folders[index])
            if targeted_folder is None:
                print(f"{folders[index]} folder not found")
                return None

        newFile = FileNode(file_name)
        if(targeted_folder.files is None):
            targeted_folder.files = newFile
        else:
            temp = targeted_folder.files
            parenFile = None
            while(temp):
                parenFile = temp
                if(file_name < temp.file_name):
                    temp = temp.left
                elif(file_name > temp.file_name):
                    temp = temp.right

                else:
                    print("Duplicates are not allowed")
                    return None

            if(file_name < parenFile.file_name):
                parenFile.left = newFile
            else:
                parenFile.right = newFile
        return newFile

    def __traverse_files(self, file_node):
        if(file_node is not None):
            self.__traverse_files(file_node.left)
            print(file_node.file_name)
            self.__traverse_files(file_node.right)

    def print_files(self, absolute_path):
        # Split the absolute path into individual folder names
        folders = absolute_path.split('/')

        # Search for the targeted folder
        targeted_folder = self.__search_folder(folders[0])
        if targeted_folder is None:
            print(f"{folders[0]} folder not found")
            return None

        # Traverse the subfolders of the targeted folder
        for index in range(1, len(folders)):
            targeted_folder = targeted_folder.subfolders
            targeted_folder = self.__get_folder(
                targeted_folder, folders[index])
            if targeted_folder is None:
                print(f"{folders[index]} folder not found")
                return None

        if targeted_folder.files is None:
            print("No files found")
        else:
            temp = targeted_folder.files
            self.__traverse_files(temp)

    def __delete_(self, destination):
        if(destination.left is not None and destination.right is not None):
            successor = destination.right
            while(successor.left):
                successor = successor.left
            destination.folder_name = successor.folder_name
            destination.right = self.__delete(
                destination.right, successor.folder_name)
        else:

            if(destination.left is not None):  # only left child
                destination = destination.left
            elif(destination.right is not None):  # only right child
                destination = destination.right
            else:  # no child
                destination = None
        return destination

    def __delete(self, destination, folder_name):
        successor = None
        if(destination is None):
            print(f"{folder_name} Not Found")
            return None
        if(folder_name < destination.folder_name):
            destination.left = self.__delete(destination.left, folder_name)
        elif(folder_name > destination.folder_name):
            destination.right = self.__delete(destination.right, folder_name)
        else:
            # folder to be deleted is found
            if(destination.password is not None):
                query = input("Enter password: ")
                if(query == destination.password):
                    name = destination.folder_name
                    destination = self.__delete_(destination)
                    print(f"{name} is deleted successfully")
                else:
                    print("Invalid password")
                    print("folder is not deleted")
            else:
                destination = self.__delete_(destination)
        return destination

    def delete_folder(self, absolute_path, folder_name=None):

        # Split the absolute path into individual folder names
        folders = absolute_path.split('/')

        if(len(folders) == 1 and folder_name == None):
            searched_folder = self.__root

            self.__root = self.__delete(searched_folder, folders[0])

        else:

            # Search for the targeted folder
            targeted_folder = self.__search_folder(folders[0])
            if targeted_folder is None:
                print(f"{folders[0]} folder not found")
                return None

            # Traverse the subfolders of the targeted folder
            for index in range(1, len(folders)):
                targeted_folder = targeted_folder.subfolders
                targeted_folder = self.__get_folder(
                    targeted_folder, folders[index])
                if targeted_folder is None:
                    print(f"{folders[index]} folder not found")
                    return None

            targeted_folder.subfolders = self.__delete(
                targeted_folder.subfolders, folder_name)

    def __delete_file(self, destination, file_name):
        successor = None
        if(destination is None):
            print(f"{file_name} file  not found")
            return None
        if(file_name < destination.file_name):
            destination.left = self.__delete_file(destination.left, file_name)
        elif(file_name > destination.file_name):
            destination.right = self.__delete_file(
                destination.right, file_name)
        else:
            # folder to be deleted is found
            if(destination.left is not None and destination.right is not None):
                successor = destination.right
                while(successor.left):
                    successor = successor.left
                destination.file_name = successor.file_name
                destination.right = self.__delete_file(
                    destination.right, successor.file_name)
            else:

                if(destination.left is not None):  # only left child
                    destination = destination.left
                elif(destination.right is not None):  # only right child
                    destination = destination.right
                else:  # no child
                    destination = None
        return destination

    def delete_file(self, absolute_path, file_name):
        folders = absolute_path.split('/')
        if(len(folders) == 1):
            root_folder = self.__search_folder(folders[0])
            if root_folder is None:
                print(f"{folders[0]} folder not found")
                return None
            root_folder.files = self.__delete_file(
                root_folder.files, file_name)
            return None
        else:
            # Traverse the subfolders of the targeted folder
            targeted_folder = self.__search_folder(folders[0])
            for index in range(1, len(folders)):
                targeted_folder = targeted_folder.subfolders
                targeted_folder = self.__get_folder(
                    targeted_folder, folders[index])
                if targeted_folder is None:
                    print(f"{folders[index]} folder not found")
                    return None
            targeted_folder.files = self.__delete_file(
                targeted_folder.files, file_name)
