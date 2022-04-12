import requests

FLICKR_KEY="ff0fa4efb379af58de43bf1c8da3a7cc"






def getImage(photo):
    url = f"https://farm{photo['farm']}.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}"
    url+='.jpg'
    return url






def getFlickrResult(tag):
  parameters = {
  'method': 'flickr.photos.search',
  'api_key': FLICKR_KEY,
  'text': tag, 
  'sort': 'interestingness-desc',
  'per_page': 12,
  'license': '4',
  'extras': 'owner_name,license',
  'format': 'json',
  'nojsoncallback': 1,
}

  URL="https://api.flickr.com/services/rest"
  r=requests.get(url=URL,params=parameters)
  data=r.json()
  imgsUrl=map(getImage,data['photos']['photo'])
  url_list=[]
  for url in imgsUrl:
    url_list.append(url)
  return url_list
  
