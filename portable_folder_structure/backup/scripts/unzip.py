import sys, os, zipfile, datetime, shutil

print "Python version", sys.version
print "Date", datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

search_path = "/media/portable/torrent/descargas"
search_extensions = [".zip"]

compressed_files = []
to_delete_folders = []

# get search_path from command
if len(sys.argv) >= 2:
    search_path = sys.argv[1]

# uncompress and then delete files
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

print "Uncompressing", search_path
print "Files", compressed_files
print "Ok", to_delete_folders
