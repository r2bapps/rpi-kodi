import sys, os, datetime, shutil

print "Python version", sys.version
print "Date", datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

search_path = "/media/portable/torrent/descargas"
search_extensions = [".rar"]
parts = [".part01", ".part1"]

compressed_files = []
to_delete_folders = []

# get search_path from command
if len(sys.argv) >= 2:
    search_path = sys.argv[1]

# uncompress and then list to delete folders
for currentpath, folders, files in os.walk(search_path):
    for file in files:
        filename, file_extension = os.path.splitext(file)
        if file_extension.lower() in search_extensions:
            for part in parts:
                if part in filename.lower():
                    found = os.path.join(currentpath, file)
                    compressed_files.append(filename)
                    try:
                        command = "unrar e '" + found + "' " #+ search_path
                        result = os.system(command)
                        if result == 0:
                            folder = os.path.dirname(found)
                            to_delete_folders.append(folder)
                    except:
                        # do nothing
                        print "Failed file", found

# removes to delete folders
#for folder in to_delete_folders:
#    shutil.rmtree(folder)

print "Uncompressing", search_path
print "Files", compressed_files
print "Ok", to_delete_folders
