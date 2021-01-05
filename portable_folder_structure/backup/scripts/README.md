# Raspberry Pi Utils

Tested on:

* Raspberry Pi 3B+
* Libreelec 9.2.x
* Kodi 18.9.x

## Python scripts

Bundled python version of Libreelec 9.2.x is Python 2.7.x

### updater.py
Downloads below files and writes them locally.

### cleaner.py
Cleans trash: .txt, .url and empty folders.

#### How to

Replace [search_path value](https://github.com/r2bapps/raspberry-pi/blob/main/cleaner.py#L6) with your path or execute *python cleaner.py [your_path]*

Replace or add [search_extensions value](https://github.com/r2bapps/raspberry-pi/blob/main/cleaner.py#L7) with files you consider trash.

### unzip.py
Extract and delete .zip and container folder.

**Note**: Extracts any file that follows the [zip file format specification](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT)

#### How to

Replace [search_path value](https://github.com/r2bapps/raspberry-pi/blob/main/unzip.py#L6) with your path or execute *python unzip.py [your_path]*

Replace or add [search_extensions value](https://github.com/r2bapps/raspberry-pi/blob/main/unzip.py#L7) with files you consider.

### unrar.py
Extract and delete .rar multi-part and container folder.

**NOTE**: Requires kodi system tools add-on or similar way to obtain unrar library. Tested with kodi add-on

#### How to

Replace [search_path value](https://github.com/r2bapps/raspberry-pi/blob/main/unrar.py#L6) with your path or execute *python unrar.py [your_path]*

### all-in-one.py
Executes unzip.py, unrar.py and clean.py sequentially.

#### How to

Execute *python all-in-one.py*. It uses default path of previous scripts.

### remove-completed-torrents.sh
Removes completed torrents from transmission torrents list.

#### How to

Execute *./remove-completed-torrents.sh*

### completed-torrents.sh
Executes remove-completed-torrents.sh and all-in-one.py sequentially.

#### How to

Execute *./completed-torrents.sh*. It is called by transmission each time a torrent finishes.