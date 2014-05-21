winflac2mp3
===========

Convenient Python script to transcode flac files into mp3.

Requirements:  
FLAC: http://xiph.org/flac/index.html  
LAME: http://lame.sourceforge.net/  

Usage:
Save the FLAC and LAME .exes in some easily accessible folder and set the lame_path and flac_path variables to point to them, respectively (it's bin/lame.exe and bin/flac.exe by default)
Install requirements.txt using pip (pip install -r requirements.txt)

Command line:  
  python flac2mp3.py inputfn ouputfn [-v]

Script:  
  from flac2mp3 import flac2mp3  
  flac2mp3(flacfn,mp3fn,verbose)  
