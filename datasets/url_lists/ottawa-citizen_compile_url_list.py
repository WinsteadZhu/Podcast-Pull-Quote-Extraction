import requests

#r = requests.get("https://ottawacitizen.com/sitemap.xml")

url_list_file = open('ottawa-citizen_urls.txt', "w")


with open('ottawa-citizen_meta_url_list.txt') as f:
	lines = f.read().split('\n')

	for i, url_str in enumerate(lines):
		print("{}/{}".format(i, len(lines)))
		#url_str = lines[0]
		r = requests.get(url_str)
		xml = r.text

		parts = xml.split('<loc>')[1:]

		urls = [p.split('</loc><')[0] for p in parts]
		print("\n {}".format(len(urls)))
		url_list_file.write('\n'.join(urls)+'\n')

url_list_file.close()