import json
import requests

from data import *
from url import Url


for url_to_check in urls_to_check:
    
    for i, url in enumerate( url_to_check['urls'] ):
        print(url)

        for j, child in enumerate( Url(url).get_children() ):
            print(f'{i}.{j} - Checking {child}')
            
            if child.response_status() != 200 or j==3:
                    
                body = \
                    f'You have a broken link at {url}\n' + \
                    f'- Link: {child}\n' + \
                    '\n\n' + \
                    'This message was automatically created by <https://github.com/matheusvanzan/broken-links-monitor|broken-links-monitor>'
                
                response = requests.post(
                    url_to_check['channel'], 
                    json.dumps({ 'text': body })
                )
                    
                print(response)
