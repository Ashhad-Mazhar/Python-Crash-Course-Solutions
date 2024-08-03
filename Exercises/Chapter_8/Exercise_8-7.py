def make_album(artist_name: str, album_title: str, number_of_songs = None):
    dictionary = {
        'artist_name': artist_name,
        'album_title': album_title
    }

    if number_of_songs:
        dictionary['number_of_songs'] = number_of_songs

    return dictionary

new_list = []
new_list.append(make_album('abc', 'efg'))
new_list.append(make_album('hij', 'klm'))
new_list.append(make_album('nop', 'qrs', 4))

for dictionary in new_list:
    for key, value in dictionary.items():
        print(f'{key}: {value}')