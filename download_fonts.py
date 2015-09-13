import sys, requests, bs4, urllib, os

# Call in command line with 2 parameters: link_of_site - folder_to_download_to

res = requests.get(sys.argv[1])
res.raise_for_status()

path = os.path.dirname(os.path.abspath(__file__))

soup = bs4.BeautifulSoup(res.text)

download_btns = soup.select('.download_arrow a')

download_links = []
for a in download_btns:
	href = "http://www.fontsquirrel.com"
	href += a.get('href')
	download_links.append(href)

for a in download_links:
	file_name = a.split("/")[-1].lower()
	folder_name = sys.argv[2]
	os.makedirs(os.path.join(path, sys.argv[2], "zip", file_name))
	download_location = os.path.join(path, sys.argv[2], "zip", file_name, file_name+".zip" )
	#download_location = folder_name+"/zip/"+file_name+"/"+file_name+".zip"
	urllib.urlretrieve(a, download_location)
	f = open(os.path.join(path, sys.argv[2], "zip", file_name, "download_link.txt"),"w")
	f.write(a)
	f.close()
	print "Downloaded: "+file_name

