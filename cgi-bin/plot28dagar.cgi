#!/bin/sh

#timestamp=`date -R`
#days=$1

# Here's the Content-type line to tell the browser that this reply
# is a png image.
echo Content-type: image/png 

# Here's the header/content blank separation line required by Apache
echo

./gnuplotx.sh
