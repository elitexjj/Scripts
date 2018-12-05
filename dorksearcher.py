import sys
import requests
import re
from random import randint
dork = "";
if len(sys.argv) >= 2:
    for arg in sys.argv:
        if arg != ".\dorksearcher.py":
            dork += arg + " ";
else:
    dork = sys.argv[1];

urls = [];
_urls = [];
page = 0;

def search():
    global dork
    global page
    global urls
    global _urls

    search = requests.get("https://www.google.com/search?q=" + dork + "&oq=" + dork.replace(" ","+") + "&sourceid=chrome&ie=UTF-8&start=" + str(page)).text;
    headers = re.findall("(?<=<h3 class=\"r\">)(.*)(?=</h3>)",search);

    for header in headers:
        url = re.findall("(?<=<a href=\")(.*)(?=\")",header);
        if "http://" or "https://" in url:
            urls.append(url[0]);

    for url in urls:
        url = url.replace("/url?q=","").replace("&amp;sa="," &amp;sa=");
        reader = url.split();
        url = reader[0];
        if "/search" in url:
            url = "";
        else:
            _urls.append(url);
            print(url);
    page += 10;

while True:
    try:
        search();
    except KeyboardInterrupt:
        break

f = open("urls.txt","a");
f.write("\n");
for url in _urls:
    f.write(url + "\n");
f.close();