http = urllib3.PoolManager()
response = http.request('GET', 'http://ipinfo.io/json')
city = json.loads(response.data.decode('utf-8'))['city']
print(city)
