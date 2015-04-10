import subprocess, os, mutagen.flac
import argparse

lame_path = ['bin','lame.exe']
flac_path = ['bin','flac.exe']

lamepath = reduce(os.path.join,lame_path)
flacpath = reduce(os.path.join,flac_path)

def flac2mp3(flacfn,mp3fn,verbose):
	if not os.path.exists(lamepath):
		if(verbose):
			print "[-] Cannot find lame encoder."
		return 1
	if not os.path.exists(flacpath):
		if verbose:
			print "[-] Cannot find flac decoder."
		return 1

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
	parser.add_argument("--flac-binary",help="Specify FLAC binary")
	parser.add_argument("--lame-binary",help="Specify LAME binary")
	args = parser.parse_args()
	if args.flac_binary:
		if os.path.exists(args.flac_binary):
			flacpath=args.flac_binary
		else:
			print "[-] Cannot find flac decoder."

	if args.lame_binary:
		if os.path.exists(args.lame_binary):
			lamepath=args.lame_binary
		else:
			print "[-] Cannot find lame encoder."

	flac2mp3(args.flacfn,args.mp3fn,args.verbose)
