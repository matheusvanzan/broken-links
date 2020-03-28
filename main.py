from data import *
from github import Github
from url import Url


for url_to_check in urls_to_check:
    
    for i, url in enumerate( url_to_check['urls'] ):
        print(url)

        for j, child in enumerate( Url(url).get_children() ):
            print('{}.{} - Checking {}'.format(i+1, j+1, child))
            
            if child.response_status() != 200 or j==3:
                
                Github.create_issue(
                    repository = url_to_check['repository'],
                    title = 'Broken link: {}'.format(child),
                    
                    body = \
                        'You have a broken link at {}\n'.format(url) + \
                        '- Link: {}\n'.format(child) + \
                        '\n\n' + \
                        'This issue was automatically created by [broken-links-monitor](https://github.com/matheusvanzan/broken-links-monitor)'
                )
