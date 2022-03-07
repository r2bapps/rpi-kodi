import sys, os, zipfile, datetime, shutil, time

# scripts path: /media/portable/backup/scripts

default_lock_file_path = "/storage/.config"
default_lock_file_name = "scripts.lock"
default_wait = 60
default_search_path = "/media/portable/torrent/descargas"
default_unzip_search_extensions = [".zip"]
default_unrar_search_extensions = [".rar"]
default_parts_extensions = [".part01", ".part1"]
default_clean_search_extensions = [".txt", ".url"]
default_remove_patterns = ["[www", "[hdtv", "[bluray", "[ac3", "[castellano", "[dvdrip", "[spanish", "[1080p"]
default_remove_end_pattern = "]"

def lock():
    # requires that /storage/.config/autostart.sh with "rm /storage/.config/scripts.lock" line
    absPath = os.path.join(default_lock_file_path, default_lock_file_name)
    file = open(absPath, "w")
    file.write("")
    file.close()

def unlock():
    absPath = os.path.join(default_lock_file_path, default_lock_file_name)
    os.remove(absPath)

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
                            command = "unrar e -y -inul '" + found + "' " + search_path
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

# move alone file on folders
def moveAloneFiles(search_path):
    for currentpath, folders, files in os.walk(search_path):
        for folder in folders:
            dir = os.path.join(currentpath, folder)
            dir_files = os.listdir(dir)
            if len(dir_files) == 1:
                shutil.move(os.path.join(dir, dir_files[0]), os.path.join(search_path, dir_files[0]))

def removeFilenamePatterns(search_path, patterns, end_pattern):
    for currentpath, folders, files in os.walk(search_path):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            new_filename = filename
            for pattern in patterns:
                if pattern in new_filename.lower():
                    begin = new_filename.lower().find(pattern)
                    end = new_filename.lower().find(end_pattern, begin)
                    new_filename = new_filename[0 : begin] + new_filename[end + 1 : len(new_filename)]
            os.rename(os.path.join(search_path, file), os.path.join(search_path, new_filename.capitalize() + file_extension))

def clean(search_path, search_extensions):
    #print "Cleaning...", search_path
    cleanExtensions(search_path, search_extensions)
    moveAloneFiles(search_path)
    cleanEmptyFolders(search_path)
    removeFilenamePatterns(search_path, default_remove_patterns, default_remove_end_pattern)

def execute():
    showEnvInfo()
    unzip(default_search_path, default_unzip_search_extensions)
    unrar(default_search_path, default_unrar_search_extensions, default_parts_extensions)
    clean(default_search_path, default_clean_search_extensions)
    print "Finish!!"

while os.path.exists(default_lock_file_name):
    time.sleep(default_wait)

lock()
execute()
unlock()
