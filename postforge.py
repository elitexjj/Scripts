import sys
import requests
import json

url = sys.argv[1];
filename = sys.argv[2];

if ".json" not in filename:
    print("[-] Must be a JSON file!");
    exit();

f = open(filename,"r");
packet = json.loads(f.read());
requests.post(url,data=packet);