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
    response = requests.get('https://api.dehashed.com/search', headers=headers, params=params, auth=('y0ronhere@gmail.com', '42345c3e9ba92e9d82987619e65951c9'))
    
    return response.content