import requests 

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

if (response.status_code != requests.codes.ok):
    print('Something went wrong.')
else:
    print(response.json())

response = requests.get('https://jsonplaceholder.typicode.com/posts/101')

if (response.status_code != requests.codes.ok):
    print('Something went wrong.')
else:
    print(response.json())

requestBody = {
    'title': 'Our title',
    'body': 'Content of json',  
    'userId': 1
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=requestBody)

if (response.status_code != requests.codes.created):
    print('Something went wrong.')
else:
    print(response.json())