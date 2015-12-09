import requests
from BeautifulSoup import BeautifulSoup
from pushbullet.pushbullet import Pushbullet
import json

pb = Pushbullet(api_key="API KEY HERE")
device_iden = pb.list_devices()['devices'][0]['iden']

# Read list of shows interested in.
f = open("shows.txt")
shows = f.read().split("\n")
shows.pop()
print shows
f.close()

# Get HTML of kat.cr and extract all anchor tags
r=requests.get("https://kat.cr",verify=False)
soup = BeautifulSoup(r.text)
links = soup.findAll("a")
text_list = []
# Get text of all anchor tags
for i in links: 
  text_list.append(i.text)
  pass
# From layout of kat.cr, the list of tv shows lie between these two strings
# Horrible hack
text_list = text_list[text_list.index("TV Shows Torrents"):text_list.index("Music Torrents")]


# Fetch the list of shows that match with yours
match = [ text for text in text_list for show in shows if show in text]
print match

# Keep a record of the notification you already sent
# if notification not already sent, send it.
f=open("sent.json")
sent = json.loads(f.read())
f.close()
for i in match:
  if i not in sent:
    sent.append(i)
    pb.bullet_note(device_iden, title="TV Show", body=i+" is available.")
f=open("sent.json","w")
f.write(json.dumps(sent))
