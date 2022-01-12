import urllib
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

# dictionary to hold extra headers
HEADERS = {"X-API_Key": ''}

# make request for Gjallarhorn
r = requests.get("https://www.bungie.net/platform/Destiny/Manifest/InventoryItem/1274330687/", headers=HEADERS)

# convert the json object we received into a Python dictionary object
# and print the name of the item
inventoryItem = r.json()
print(inventoryItem['Response']['data']['inventoryItem']['itemName'])


class DestinyGuardians:

    def __init__(self):
        self.name = "데스티니 가디언즈"
        self.names = ["destiny", "d2", "dg", "데가", "데스티니2"]
        self.patch = {"title": None, "url": None, "desc": None, "image": None}
        self.color = 1752220
        self.thumbnail = "https://i.imgur.com/FfgGn8f.png"

    def get_patch_note(self):

        # Gets source of DestinyGuardians patch page.
        try:
            request = Request("https://www.bungie.net/ko/News/Index?tag=news-updates",
                              headers={'User-Agent': 'Mozilla/5.0'})
            source = urlopen(request).read()
        except:
            raise Exception(self.name + "웹사이트에 연결할 수 없습니다.")

        try:
            patch_update_divs = soup(source, "html.parser"). \
                findAll("div", {"class": "news-items grid-col-8 grid-col-7-medium grid-col-12-mobile"})
        except:
            raise Exception("patch_update_divs를 가져오는데 실패했습니다.")

        # Gets source of DestinyGuardians patch url.
        try:
            self.patch["url"] = "https://www.bungie.net" + patch_update_divs[0].a["href"]
            if self.patch["url"] is None:
                raise Exception(self.name + "url을 찾을 수 없습니다.")
        except:
            raise Exception(self.name + "URL 가져오기 실패")

        # Gets source of DestinyGuardians patch title.
        try:
            self.patch["title"] = patch_update_divs[0].a["title"]
            if self.patch["url"] is None:
                raise Exception(self.name + "제목을 찾을 수 없습니다.")
        except:
            raise Exception(self.name + "제목 가져오기 실패")

        # Gets source of DestinyGuardians patch image.
        try:
            self.patch["image"] = "https://www.bungie.net" + patch_update_divs[0].div.div.img["src"]
            if self.patch["image"] is None:
                raise Exception(self.name + "이미지를 찾을 수 없습니다.")
        except:
            raise Exception(self.name + "이미지 가져오기 실패")

        # Gets source of DesitnyGuardians patch description.
        try:
            pass
        except:
            pass
