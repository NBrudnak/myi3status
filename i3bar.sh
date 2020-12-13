#!/bin/zsh

bg_bar_color="#ffffff"


# Send the header so that i3bar knows we want to use JSON:
echo '{ "version": 1, "click_events": true }'

# Begin the endless array.
echo '['

# We send an empty first array of blocks to make the loop simpler:
echo '[]'

# Now send blocks with information forever:
(while :;
do
  echo -n ",["


  #notifications
  echo -n "{\"name\":\"id_notifications\",\"background\":\"#14524a\",\"full_text\":\"$(/home/merl/code/i3-status-custom/notifications.sh)\"},"
  #volume display
  echo -n "{\"name\":\"id_volume\",\"background\":\"#14524a\",\"full_text\":\"Vol: $(/home/merl/code/i3-status-custom/volume.sh)\"},"
  #cpu display
  echo -n "{\"name\":\"id_cpu\",\"background\":\"#14524a\",\"full_text\":\"$(/home/merl/code/i3-status-custom/cpu.py)%\"},"
  #date and time
	echo -n "{\"name\":\"id_time\",\"background\":\"#14524a\",\"full_text\":\"$(date)\"}"
  
  echo -n "]"
	sleep 1
done) &

while read line;
  do
    #click event: notification -> email view
    if [[ $line == *"name"*"id_notifications"* ]]; then
      alacritty -e /home/merl/code/i3-status-custom/mail.py v &
    #click event: cpu -> htop view
    elif [[ $line == *"name"*"id_cpu"* ]]; then
      alacritty -e htop &
    elif [[ $line == *"name"*"id_volume"* ]]; then
      alacritty -e alsamixer
    fi
  done
