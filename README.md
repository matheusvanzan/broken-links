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
        'channel': 'https://hooks.slack.com/services/first-hook',
        'urls': [
            'https://example.com/',
            'https://example.com/url-one/',
            'https://example.com/url-two/'
        ]
    },
    {
        'channel': 'https://hooks.slack.com/services/second-hook',
        'urls': [
            'https://other.com/',
            'https://other.com/url-one/'
        ]
    },
    ...
]
```

## Configuring Slack issue

Cretate an incoming webhook on Slack [here](https://brokenlinksworkspace.slack.com/apps/A0F7XDUAZ-webhooks-de-entrada?next_id=0)

Just get the provided Url and put in `data.py`

## Crontab config

Add the following line to your crontab with `crontab -e` to run the script 
every day at 6 a.m.

```bash
# m h dom mon dow command
0 6 * * * /path/to/virtualenv/bin/python main.py
```
