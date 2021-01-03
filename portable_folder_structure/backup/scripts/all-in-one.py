import sys, os, zipfile, datetime, shutil

# scripts path: /media/portable/backup/scripts

default_search_path = "/media/portable/torrent/descargas"
default_unzip_search_extensions = [".zip"]
default_unrar_search_extensions = [".rar"]
default_parts_extensions = [".part01", ".part1"]
default_clean_search_extensions = [".txt", ".url"]

# shows env info
def showEnvInfo():
    print ""
    print "**************"
    print "Python version", sys.version
    print "Date", datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print "**************"
    print ""

# uncompress .zip files and delete them
def unzip(search_path, search_extensions):
    compressed_files = []
    to_delete_folders = []
    for currentpath, folders, files in os.walk(search_path):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension.lower() in search_extensions:
                found = os.path.join(currentpath, file)
                compressed_files.append(found)
                try:
                    with zipfile.ZipFile(found, 'r') as zip_ref:
                        zip_ref.extractall(search_path)
                    folder = os.path.dirname(found)
                    to_delete_folders.append(folder)
                except:
                    # do nothing
                    print "Failed file", found
    # removes to delete folders
    for folder in to_delete_folders:
        shutil.rmtree(folder)
    #print "Compressed files", compressed_files
    #print "Uncompressed files correctly", to_delete_folders

# uncompress .rar files and delete them
def unrar(search_path, search_extensions, parts_extensions):
    compressed_files = []
    to_delete_folders = []
    for currentpath, folders, files in os.walk(search_path):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension.lower() in search_extensions:
                for part in parts_extensions:
                    if part in filename.lower():
                        found = os.path.join(currentpath, file)
                        compressed_files.append(filename)
                        try:
                            command = "unrar e '" + found + "' " + search_path
                            result = os.system(command)
                            if result == 0:
                                folder = os.path.dirname(found)
                                to_delete_folders.append(folder)
                        except:
                            # do nothing
                            print "Failed file", found
    # removes to delete folders
    for folder in to_delete_folders:
        shutil.rmtree(folder)
    #print "Compressed files", compressed_files
    #print "Uncompressed files correctly", to_delete_folders

# delete files with extension
def cleanExtensions(search_path, search_extensions):
    deleted_files = []
    for currentpath, folders, files in os.walk(search_path):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension.lower() in search_extensions:
                found = os.path.join(currentpath, file)
                deleted_files.append(found)
                os.remove(found)
    #print "Deleted files", deleted_files

# delete empty folders
def cleanEmptyFolders(search_path):
    deleted_folders = []
    for currentpath, folders, files in os.walk(search_path):
        for folder in folders:
            dir = os.path.join(currentpath, folder)
            dir_files = os.listdir(dir)
            if len(dir_files) == 0:
                deleted_folders.append(dir)
                os.rmdir(dir)
    #print "Deleted folders", deleted_folders

def clean(search_path, search_extensions):
    #print "Cleaning...", search_path
    cleanExtensions(search_path, search_extensions)
    cleanEmptyFolders(search_path)

def execute():
    showEnvInfo()
    unzip(default_search_path, default_unzip_search_extensions)
    unrar(default_search_path, default_unrar_search_extensions, default_parts_extensions)
    clean(default_search_path, default_clean_search_extensions)
    
execute()
