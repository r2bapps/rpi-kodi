import sys, os, datetime, shutil

print "Python version", sys.version
print "Date", datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

search_path = "/media/portable/torrent/descargas"
search_extensions = [".txt", ".url"]
remove_patterns = ["[www", "[hdtv", "[bluray", "[ac3", "[castellano"]
remove_end_pattern = "]"

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
            shutil.move(os.path.join(dir, dir_files[0]), os.path.join(search_path, dir_files[0]))

# delete empty folders again
for currentpath, folders, files in os.walk(search_path):
    for folder in folders:
        dir = os.path.join(currentpath, folder)
        dir_files = os.listdir(dir)
        if len(dir_files) == 0:
            deleted_folders.append(dir)
            os.rmdir(dir)

# renames files
for currentpath, folders, files in os.walk(search_path):
    for file in files:
        filename, file_extension = os.path.splitext(file)
        new_filename = filename
        for pattern in remove_patterns:
            if pattern in new_filename.lower():
                begin = new_filename.lower().find(pattern)
                end = new_filename.lower().find(remove_end_pattern, begin)
                new_filename = new_filename[0 : begin] + new_filename[end + 1 : len(new_filename)]
        os.rename(os.path.join(search_path, file), os.path.join(search_path, new_filename.capitalize() + file_extension))

print "Cleaning", search_path
print "Files", deleted_files
print "Folders", deleted_folders
