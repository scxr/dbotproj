def fromapi(inp):
    import requests
    from tohaste import hasteme

    headers = {
        'Accept': 'application/json',
    }
    topass = "username:"+'"'+inp+'"'
    params = (
        ('query', topass),
        ('page','1'),
    )
    print(topass)
    response = requests.get('https://api.dehashed.com/search', headers=headers, params=params, auth=('<redacted>', '<redacted>'))
    
    return response.content
