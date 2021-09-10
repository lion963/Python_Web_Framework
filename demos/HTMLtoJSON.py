import json
import urllib
from urllib import request

import html_to_json

link = "https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99"

# try:
#     with request.urlopen(link) as data:
#         print(data.read())
# except urllib.error.URLError as e:
#     print(e.reason)

data1 = request.urlopen(link)
data2 = data1.read().decode('utf-8')
data3 = html_to_json.convert(data2)
a=2