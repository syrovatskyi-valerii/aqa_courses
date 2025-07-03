'''
Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON про фото зробленi ровером “Curiosity” на Марсi.
Серед цих даних є посилання на фото якi потрiбно розпарсити i потiм за допомогою додаткових запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg , mars_photo2.jpg .
Завдання потрiбно зробити використовуючи модуль requests.
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
'''

import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000,
          'camera': 'fhaz',
          'api_key': 'DEMO_KEY'}


response = requests.get(url=url, params=params)

data = response.json()
photos = data.get('photos')

for i, photo in enumerate(photos):
    img_url = photo['img_src']
    img_data = requests.get(img_url).content

    with open(f'mars_photo{i+1}.jpg', 'wb') as f:
        f.write(img_data)
