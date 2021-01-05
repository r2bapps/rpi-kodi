#!/bin/bash

TORRENTLIST=`transmission-remote --list | grep 100% | awk '{print $1}'`

for TORRENTID in $TORRENTLIST
do
  TORRENTID=`echo $TORRENTID | sed 's:*::'`
  echo "Torrent $TORRENTID is completed."
  echo "Removing torrent from list."
  transmission-remote -t $TORRENTID -r
done
