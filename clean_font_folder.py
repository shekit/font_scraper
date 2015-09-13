import sys, os

#give folder as first arguement in command line
# removes dashes and replaces with underscores

path = os.path.dirname(os.path.abspath(__file__))

for dirpath, dirs, files in os.walk(os.path.join(path, sys.argv[1], "zip")):
	for d in dirs:
		print "FOLDER: "+d
		for filename in os.listdir(os.path.join(path, sys.argv[1], "zip", d)):
			if filename.endswith(".txt"):
				print "ignoring download file"
			else:
				splitname = filename.split("-")
				newfilename = "_".join(splitname)
				print newfilename
				os.rename(os.path.join(path, sys.argv[1], "zip", d, filename), os.path.join(path, sys.argv[1], "zip", d, newfilename))

