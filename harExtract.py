import json
from haralyzer import HarParser
import urllib.request


# parsing HAR file:
with open('HarFilePath.har', 'r') as f:
    har_parser = HarParser(json.loads(f.read()))

data = har_parser.har_data

links = []

# Getting needed links: (here all png files)
for i in range(len(har_parser.har_data['entries'])):
    links.append(har_parser.har_data['entries'][i]['request']['url'])

# Saving all png files
for link in links:
    urllib.request.urlretrieve(link, 'destination_folder/' + link.split('/')[-1])
