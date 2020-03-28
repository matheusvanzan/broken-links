# Broken links monitor

This project parses a website to find broken links. If one is found it creates
an issue at specified github repository.

## Install

```bash
pip install -r requirements.txt
```

## Configuring urls

The urls can be configured in `data.py` file.

```python
urls_to_check = [
    {
        'repository': 'https://github.com/someuser/first-repo',
        'urls': [
            'https://example.com/',
            'https://example.com/url-one/',
            'https://example.com/url-two/'
        ]
    },
    {
        'repository': 'https://github.com/otheruser/second-repo',
        'urls': [
            'https://other.com/',
            'https://other.com/url-one/'
        ]
    },
    ...
]
```

## Configuring Github issue

Fisrt, get an [API token](https://github.com/settings/tokens) from github.

Set the `GITHUB_TOKEN` environment variable to your token as the `Github` class 
has class variables you must provide

```python
class Github:
    
    username = 'your_github_username'
    token = os.environ['GITHUB_TOKEN']
    
    ...
```

## Crontab config

Add the following line to your crontab with `crontab -e` to run the script 
every day at 6 a.m.

```bash
# m h dom mon dow command
0 6 * * * /path/to/virtualenv/bin/python main.py
```
