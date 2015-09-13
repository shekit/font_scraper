#extract zip files in a given directory - place directory name as first parameter in command line
# also deletes extra files and lowercases the file names

import glob, os, zipfile, sys

"""os.chdir(sys.argv[1])

for f in glob.glob("*.zip"):
	with zipfile.ZipFile(f, 'r') as z:
		z.extractall(sys.argv[2])"""

path = os.path.dirname(os.path.abspath(__file__))

# extract zip files
for dirpath, dirs, files in os.walk(os.path.join(path, sys.argv[1], "zip")):
	for d in dirs:
		os.chdir(os.path.join(path,sys.argv[1],"zip",d))
		for f in glob.glob("*.zip"):
			with zipfile.ZipFile(f, 'r') as z:
				z.extractall(os.path.join(path,sys.argv[1],"zip",d))

#delete unnecessary files
for dirpath, dirs, files in os.walk(os.path.join(path, sys.argv[1], "zip")):
	for d in dirs:
		print "FOLDER: " + d
		for filename in os.listdir(os.path.join(path, sys.argv[1], "zip", d)):
			if filename.endswith(".otf") or filename.endswith(".ttf"):
				os.rename(os.path.join(path, sys.argv[1],"zip",d,filename), os.path.join(path, sys.argv[1],"zip",d,filename.lower()))
				print "ITS A FONT"
			elif filename.startswith("download_link"):
				print "DOWNLOAD CLASS"
			else:
				os.remove(os.path.join(path,sys.argv[1],"zip", d, filename))
				print "NOT A FONT"