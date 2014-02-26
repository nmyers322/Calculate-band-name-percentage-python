#this file takes the list of bands from 
# http://www.invisibleoranges.com/2014/02/the-100-most-overused-metal-band-name-words-according-to-metal-archives/
# and calculates the percentage compared to all known metal bands.

from __future__ import division
import re

totalbands = 95547 #from metal-archives.com

#example line: 100. Dragon  108 entries
#(note the ascii representation for "-" is different here than
#  on the source website, hence it does not exist in the line.)
# also, I removed the a,b,c from the 100 lines.

with open("bands.txt", "r") as bandfile:
    for band in bandfile:
        m = re.match(r'^(\d*)([^\d]*)(\d*)(.*)$', band, re.I)
        print band,".... ", ("%.4f" % ((int(m.group(3))/totalbands)*100)), "% frequency"

