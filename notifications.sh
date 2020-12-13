#!/bin/sh


amount=$(~/code/i3-status-custom/mail.py)
unchecked=1067
final=$(expr $amount - $unchecked)


echo $final
