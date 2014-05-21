import subprocess, os, mutagen.flac
import argparse

lame_path = ['bin','lame.exe']
flac_path = ['bin','flac.exe']

lamepath = reduce(os.path.join,lame_path)
flacpath = reduce(os.path.join,flac_path)

def flac2mp3(flacfn,mp3fn,verbose):
	flacData = mutagen.flac.FLAC(flacfn)
	if verbose:
		print "[*] FLAC METADATA:"
		for item in flacData.tags:
			print "\t"+item[0]+"\t:"+item[1]

	subprocess.call([flacpath,'-d',flacfn,'-o','temp.wav',"-s"])
	if verbose:
		print "[+] Decoded FLAC as temp.wav"

	subprocess.call([lamepath,'-V0','temp.wav',mp3fn,"--silent",
		'--tt',flacData['title'][0],
		'--ta',flacData['artist'][0],
		'--tl',flacData['album'][0],
		'--ty',flacData['date'][0],
		'--tn',flacData['tracknumber'][0],
		'--tg',flacData['genre'][0]])
	if verbose:
		print "[+] Encoded as "+mp3fn+"."
	os.remove('temp.wav')
	return 0

if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("flacfn",help="FLAC filename (with extension)")
	parser.add_argument("mp3fn",help="Output filename (with extension)")
	parser.add_argument("-v","--verbose",help="Increase output verbosity",action="store_true")
	args = parser.parse_args()
	flac2mp3(args.flacfn,args.mp3fn,args.verbose)
