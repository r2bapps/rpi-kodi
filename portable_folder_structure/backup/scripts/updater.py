import urllib, sys, datetime

print "Python version", sys.version
print "Date", datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

base_url = "https://raw.githubusercontent.com/r2bapps/rpi-kodi/main/portable_folder_structure/backup/scripts/"
files = ["updater.py", "unrar.py", "cleaner.py", "unzip.py"]

downloaded_files = []

for filename in files:
    url = base_url + filename
    try:
        urllib.urlretrieve(url, filename)
        downloaded_files.append(filename)
    except:
        # do nothing
        print "Failed file", filename

print "Downloading", base_url
print "Files", files
print "Ok", downloaded_files
