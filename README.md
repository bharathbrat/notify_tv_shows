# Notifier for TV shows

Script can be used as a cron that runs every x minutes/hours to notify you when a TV show you are following is available on the front page of kat.cr

Pushbullet application and an API key is required to receive notifications. Feel free to change this if any other elegant solution is available. :-)

<b>Insert API key into notifier.py</b>

- shows.txt -> List of TV shows you are interested in.
- sent.json -> Populated to keep track of notifications already sent.

Pusbullet python library can be found [here][l1].

[l1]: https://github.com/myles/pushbullet

