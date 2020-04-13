import requests
from bs4 import BeautifulSoup


class Url:
    
    def __init__(self, raw, domain_url=None):
        self.raw = raw
        
        if '://' in raw: # absolute url
            raw_split = raw.split('://')
            self.method = raw_split[0]
            
            if '/' in raw_split[1]:
                self.domain = raw_split[1].split('/')[0]
            else:
                self.domain = raw_split[1]
            
        elif domain_url: # relative url
            self.method = domain_url.method
            self.domain = domain_url.domain
            
        else:
            raise Exception('Url must have HTTP method or provide a domain_url.')
            
        self.path = raw.replace('://', '').replace(self.method, '').replace(self.domain, '')
            
    @property
    def domain_url(self):
        return Url(f'{self.method}://{self.domain}')
        
    def __str__(self):
        return f'{self.method}://{self.domain}{self.path}'
            
    def __repr__(self):
        return f'<Url method:{self.method} domain:{self.domain} path:{self.path}>'
        
    def response_status(self):
        response = requests.get(self.__str__())
        return response.status_code
        
    def check_same_domain(self, other):
        return self.domain == other.domain
        
    def get_children(self):
        response = requests.get(self.__str__())
        soup = BeautifulSoup(response.text, features='html.parser')
        
        urls = set()
        for a in soup.find_all('a'):
            if a.has_attr('href'):
                
                if a['href'][:4] == 'http':
                    urls.add(Url(a['href']))
                    
                elif a['href'][0] == '/':
                    urls.add(Url(a['href'], domain_url=self.domain_url))
                    
        return list(urls)
        