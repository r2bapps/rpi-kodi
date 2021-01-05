#!/bin/bash

# Extract from: https://gist.github.com/ffcruz85/6c9fb792fce4af0c4cb561fd653c86b6

# script to check for complete torrents in transmission folder and delete it from list

# use transmission-remote to get torrent list from transmission-remote list
# use sed to delete first / last line of output, and remove leading spaces
# use cut to get first field from each line
TORRENTLIST=`transmission-remote --list | sed -e '1d;$d;s/^ *//' | cut --only-delimited -d ' ' --fields=1`
# for each torrent in the list
for TORRENTID in $TORRENTLIST
do
  TORRENTID=`echo $TORRENTID | sed 's:*::'`
  # removes asterisk * from torrent ID# which had error associated with it
  echo "* * * * * Operations on torrent ID $TORRENTID starting. * * * * *"
  # check if torrent download is completed
  DL_COMPLETED=`transmission-remote -t $TORRENTID -i | grep "Percent Done: 100%"`
  # check torrent’s current state is "Stopped", "Finished", or "Idle"
  STATE_STOPPED=`transmission-remote -t $TORRENTID -i | grep "State: Stopped\|Finished\|Idle"`
  # if the torrent is "Stopped", "Finished", or "Idle" after downloading 100%…
  if [ "$DL_COMPLETED" != "" ] && [ "$STATE_STOPPED" != "" ]; then
    # move the files and remove the torrent from Transmission
    echo "Torrent $TORRENTID is completed."
    echo "Removing torrent from list."
    transmission-remote -t $TORRENTID -r
  else
    echo "Torrent $TORRENTID is not completed. Ignoring."
  fi
  echo "* * * * * Operations on torrent ID $TORRENTID completed. * * * * *"
done