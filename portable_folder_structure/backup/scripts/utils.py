import urllib, os, shutil

base_url = "https://raw.githubusercontent.com/r2bapps/rpi-kodi/main/"

# download files from url
def download(files, project_path):
    downloaded_files = 0
    for filename in files:
        url = base_url + project_path + filename
        try:
            urllib.urlretrieve(url, filename)
            downloaded_files += 1
        except:
            # do nothing
            print "Failed file", filename
    return downloaded_files

# moves files to folder
def move(files, folder):
    moved_files = 0
    for filename in files:
        try:
            shutil.move(filename, os.path.join(folder, filename))
            moved_files += 1
        except:
            # do nothing
            print "Failed file", filename
    return moved_files
