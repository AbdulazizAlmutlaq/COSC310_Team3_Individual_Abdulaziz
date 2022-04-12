import requests
import re

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"




def getWikiResult(searchpage):
    PARAMS = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": searchpage
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    page_result=[]
    for obj in DATA['query']['search']:
        body=obj['snippet']
        cleantext = re.sub(CLEANR, '', body)
        page_result.append(cleantext)
    return page_result
    

