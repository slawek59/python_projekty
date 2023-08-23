import requests

print('Book name (format: name+chapter:verse)')
book_name = input('Title: ')
print('Possible translations: cherokee, bbe, kjv, web, oeb-cw, webbe, oeb-us, clementine, almeida')
translation = input('Translation: ')

response = requests.get(f'https://bible-api.com/{book_name}?translation={translation}')

if (response.status_code != requests.codes.ok):
    print('Something went wrong.')
else:
    print(response.json())

print(response.status_code)