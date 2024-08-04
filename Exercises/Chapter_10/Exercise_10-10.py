the_word_count = 0

try:
    with open('millions_of_cats.txt', encoding='UTF-8') as text_to_analyze:
        for line in text_to_analyze:
            the_word_count += line.lower().count(' the ')
        print(f'The word "the" appears {the_word_count} times in the text')
except FileNotFoundError:
    print('File not found')