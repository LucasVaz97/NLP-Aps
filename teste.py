import re
import urllib.request


with urllib.request.urlopen("https://myanimelist.net/anime/49721/Karakai_Jouzu_no_Takagi-san_3") as url:
    s = url.read()
    # I'm guessing this would output the html source code ?
    image_tag = re.compile(r'<img.*?/>').search(s).group()
    s.replace(image_tag, '')
    print(s)
