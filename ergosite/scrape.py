import xml.etree.ElementTree as ET, sqlite3 as sq, re, requests as rq


ergocon = sq.connect('ergo.sqlite')
ergocur = ergocon.cursor()


url = 'https://secure.runescape.com/m=adventurers-log/rssfeed?searchName=Ergo'
response = rq.get(url)
data = ET.fromstring(response.text)
feed = data[0].findall('item')
for item in feed:
    title = item.find('title').text
    description = item.find('description').text
    link = item.find('link').text
    date = item.find('pubDate').text
    itemid = re.match('.*[&id=-](?P<id>\d*)',item.find('link').text).group('id')
    ergocur.execute('INSERT INTO Events (id, title, description, link, date) VALUES (itemid, title, description, link, date)')