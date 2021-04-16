import requests

url_hobbit = r'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
response = requests.get(url_hobbit)
response_dict = response.json()
result = []

for item in response_dict['items']:
    my_dict = {}
    my_dict['id'] = item.get('id', 'id')
    my_dict['title'] = item.get('volumeInfo').get('title', 'title')
    my_dict['authors'] = item.get('volumeInfo').get('authors', 'authors')
    my_dict['publishedDate'] = item.get('volumeInfo').get('publishedDate', 'publish_date')
    my_dict['categories'] = item.get('volumeInfo').get('categories', 'categories')
    my_dict['average_rating'] = item.get('volumeInfo').get('average_rating', 'average_rating')
    my_dict['ratings_count'] = item.get('volumeInfo').get('ratings_count', 'ratings_count')
    my_dict['thumbnail'] = item.get('volumeInfo').get('imageLinks').get('thumbnail', 'thumbnail')

    print(my_dict)
    result.append(my_dict)

print('\n\n')

url_war = r'https://www.googleapis.com/books/v1/volumes?q=war'
response2 = requests.get(url_war)
response_dict = response2.json()
result2 = []

for item in response_dict['items']:
    my_dict2 = {}
    my_dict2['id'] = item.get('id', 'id')
    my_dict2['title'] = item.get('volumeInfo').get('title', 'title')
    my_dict2['authors'] = item.get('volumeInfo').get('authors', 'authors')
    my_dict2['publishedDate'] = item.get('volumeInfo').get('publishedDate', 'publish_date')
    my_dict2['categories'] = item.get('volumeInfo').get('categories', 'categories')
    my_dict2['average_rating'] = item.get('volumeInfo').get('average_rating', 'average_rating')
    my_dict2['ratings_count'] = item.get('volumeInfo').get('ratings_count', 'ratings_count')
    my_dict2['thumbnail'] = item.get('volumeInfo').get('imageLinks').get('thumbnail', 'thumbnail')

    print(my_dict2)
    result2.append(my_dict2)
