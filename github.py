from datetime import datetime
import os
import requests
import json


class Github:
    
    username = 'matheusvanzan'
    token = os.environ['GITHUB_TOKEN']
    
    @classmethod
    def create_issue(cls, repository, title, body):
        '''
        
        '''
        repository = repository.replace('https://github.com/', '')
        repo_owner = repository.split('/')[0]
        repo_name = repository.split('/')[1]
        url = 'https://api.github.com/repos/{}/{}/import/issues'.format(repo_owner, repo_name)
        
        # Headers
        headers = {
            "Authorization": "token {}".format(cls.token),
            "Accept": "application/vnd.github.golden-comet-preview+json"
        }
        
        # Create our issue
        data = {
            'issue': {
                'title': title,
                    'body': body,
                    'created_at': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
                    'assignee': cls.username
            }
        }
    
        payload = json.dumps(data)
    
        # Add the issue to our repository
        response = requests.request("POST", url, data=payload, headers=headers)
        if response.status_code == 202:
            print('Successfully created Issue', title)
        else:
            print('Could not create Issue', title)
            print('Response:', response.content)