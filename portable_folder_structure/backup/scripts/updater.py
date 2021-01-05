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

def scriptsUpdater():
    scripts_path = "/media/portable/backup/scripts"
    project_path = "portable_folder_structure/backup/scripts"
    files = ["updater.py", "unrar.py", "cleaner.py", "unzip.py", "README.md", "all-in-one.py", "remove-completed-torrents.sh", "completed-torrents.sh"]

    downloaded_files = download(files, project_path)
    moved_files = move(files, scripts_path)

    if downloaded_files == len(files) and moved_files == len(files):
        print "Updated system: Ok"

def transmissionConfigUpdater():
    scripts_path = "/storage/.kodi/userdata/addon_data/service.transmission"
    project_path = "portable_folder_structure/backup/system/transmission/config"
    files = ["settings.json", "settings.xml"]

    downloaded_files = download(files, project_path)
    moved_files = move(files, scripts_path)

    if downloaded_files == len(files) and moved_files == len(files):
        print "Updated transmission config: Ok"

print "Updating..."

scriptsUpdater()
transmissionConfigUpdater()

print "End"
