def make_album(artist_name: str, album_title: str, number_of_songs = None):
    dictionary = {
        'artist_name': artist_name,
        'album_title': album_title
    }

    if number_of_songs:
        dictionary['number_of_songs'] = number_of_songs

    return dictionary


repeat = 'Yes'

while repeat != 'No':
    artist_name = input('Enter artist name: ')
    album_title = input('Enter album title: ')
    dictionary = make_album(artist_name, album_title)

    for key, value in dictionary.items():
        print(f'{key}: {value}')
    
    repeat = input('Would you like to repeat? ')