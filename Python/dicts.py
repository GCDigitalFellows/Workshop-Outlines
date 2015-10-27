# Dictionaries

# Let's make a phone book

phone_book = {'Alice':199933355555,
              'Bob':14446669999,
              'Rilke':18884321111,
              'Goethe':12223334444}

print(phone_book['Alice'])

def look_up_number(name):
    print(phone_book[name])

look_up_number('Rilke')
look_up_number('Goethe')
