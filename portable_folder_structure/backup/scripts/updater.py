import urllib, os, sys, datetime, shutil

print "Python version", sys.version
print "Date", datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

scripts_path = "/media/portable/backup/scripts"
base_url = "https://raw.githubusercontent.com/r2bapps/rpi-kodi/main/portable_folder_structure/backup/scripts/"
files = ["updater.py", "unrar.py", "cleaner.py", "unzip.py"]

downloaded_files = []

# get scripts_path from command
if len(sys.argv) >= 2:
    scripts_path = sys.argv[1]

for filename in files:
    url = base_url + filename
    try:
        urllib.urlretrieve(url, filename)
        downloaded_files.append(filename)
    except:
        # do nothing
        print "Failed file", filename

# moves downloaded files to scripts folders
for file in files:
    shutil.move(file, os.path.join(scripts_path, file))

print "Downloading", base_url
print "Files", files
print "Ok", downloaded_files
