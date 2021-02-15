import requests
import json
from bs4 import BeautifulSoup

class Scp():
    def __init__(self, ID = "", name = "", containment = "", tags = []):
        self.ID = ID
        self.name = name
        self.containment = containment
        self.tags = tags

def fetchSCPs():
    url = "https://the-scp.foundation/object/scp-"
    spcs = []

    for i in range(1, 101):                        #After testing, set range upper bound to 4000
        if i < 10:
            currUrl = url + "00" + str(i)
        elif i >= 10 and i < 100:
            currUrl = url + "0" + str(i)
        else:
            currUrl = url + str(i)

        print("Fetching : " + str(i))
        response = requests.get(currUrl)
        if response.status_code == 200:
            newScp = Scp("", "", "", [])
            soup = BeautifulSoup(response.content, 'html.parser')
            newScp.ID = soup.find(id = 'item-number').get_text()
            newScp.name = soup.find(class_ = 'scp-nickname').get_text()
            currContainment = soup.select_one(".scp-tag")
            if currContainment is not None: newScp.containment = currContainment.get_text().replace("\n", "")
            scpRawTags = soup.find_all(class_ = 'scp-tag')
            if len(scpRawTags) > 0: scpRawTags.pop(0)
            for tag in scpRawTags: scpTagsArr = newScp.tags.append(tag.find('span').get_text().replace("\n", ""))
            #print(newScp.ID, newScp.name, newScp.containment, newScp.tags)
            spcs.append(newScp)
            
    return spcs;


spcsArray = fetchSCPs()
with open("PythonCode/SCP-Database/scps.json", "w") as jsonFile:
    for scp in spcsArray:
        print("Dumping " + str(scp.__dict__))
        json.dump(str(scp.__dict__), jsonFile)
        json.dump("\n", jsonFile)