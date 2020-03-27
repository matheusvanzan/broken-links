import requests
from bs4 import BeautifulSoup

same_origin_only = True

class Url:
    
    def __init__(self, raw):
        if not 'http://' in raw and not 'https://' in raw:
            raise Exception('Url method must be http or https')
            
        self.raw = raw
        self.method = ''
        self.domain = ''
        
    def check_same_domain(self, other):
        return self.domain == other.domain
        

url = Url('https://umcodigo.com/cloud9-porque-usar-uma-cloud-ide/')
response = requests.get(url.raw)
soup = BeautifulSoup(response.text, features='html.parser')

urls = set()

for a in soup.find_all('a'):
    if a.has_attr('href'):
        print(a['href'])