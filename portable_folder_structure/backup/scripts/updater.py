import urllib, os, shutil
from utils import download
from utils import move

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
