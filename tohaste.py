def hasteme(txt):
    import requests
    import json
    req = requests.post('https://hastebin.com/documents',data=txt)
    key = json.loads(req.content)
    return 'https://hastebin.com/' + key['key']
