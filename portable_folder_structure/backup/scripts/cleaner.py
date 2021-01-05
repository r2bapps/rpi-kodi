import sys, os, datetime, shutil

print "Python version", sys.version
print "Date", datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

search_path = "/media/portable/torrent/descargas"
search_extensions = [".txt", ".url"]

deleted_files = []
deleted_folders = []

# get search_path from command
if len(sys.argv) >= 2:
    search_path = sys.argv[1]

# delete files with extension
for currentpath, folders, files in os.walk(search_path):
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file_extension.lower() in search_extensions:
            found = os.path.join(currentpath, file)
            deleted_files.append(found)
            os.remove(found)

# move alone file on folders
for currentpath, folders, files in os.walk(search_path):
    for folder in folders:
        dir = os.path.join(currentpath, folder)
        dir_files = os.listdir(dir)
        if len(dir_files) == 1:
            shutil.move(dir_files[0], search_path)

# delete empty folders again
for currentpath, folders, files in os.walk(search_path):
    for folder in folders:
        dir = os.path.join(currentpath, folder)
        dir_files = os.listdir(dir)
        if len(dir_files) == 0:
            deleted_folders.append(dir)
            os.rmdir(dir)

print "Cleaning", search_path
print "Files", deleted_files
print "Folders", deleted_folders
