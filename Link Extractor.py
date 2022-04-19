from json import loads
from requests import get

all_links = []
all_links_sort = []


def link_extract():
    content = get('http://web.archive.org/cdx/search/cdx?url=*.{}/*&output=json&collapse=urlkey'.format(domain)).content
    content_json = loads(content)
    for i in content_json:
	    for j in i:
		    if domain in j and j.startswith("http"):
			    if j not in all_links:
				    all_links.append(j)


domain = input("Lütfen Bir Domain Giriniz: ")
if domain.startswith("https") or domain.startswith("http"):
    domain = input("Lütfen Başinda 'http' ve ya 'https' olmadan tekrar girin: ")
    url = domain.split(".")
    link_extract()
else:
    url = domain.split(".")
    link_extract()


for i in all_links:
    if i.startswith('https://'):
        strip = i.replace("https://","")
        all_links_sort.append(strip)
    else:
        strip = i.replace("http://","")
        all_links_sort.append(strip)

all_links_sort.sort()

for j in all_links_sort:
    with open("Link.txt", "a") as file:
        file.write(j+"\n")

