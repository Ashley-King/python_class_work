'''
    Assignment: 6 - All Greek To Me
    Author: Ashley King
    Date: 2019-02-13
    Description: Using functions, tuples and dictionaries
'''

# Part 1 - Game Physics

''' Algorithm Part 1:
1. pass in two tuples with format x coordinate, y coordinate, radius (x, y, r)
2. sum of radii = tuple_1[r] + tuple_2[r]
3. save x and y coordinates of each ball to variables for clarity
4. distance = square root of (((X2-X1)** 2) + ((Y2-Y1)** 2))
5. if distance less than or equal to sum of radii, the balls are colliding
6. if distance greater than sum of radii, the balls are not colliding
'''

def isColliding(ball_1, ball_2):
    # add radii
    sum_of_radii = ball_1[2] + ball_2[2]
    # save coordinates to variables
    x_ball_1 = ball_1[0]
    y_ball_1 = ball_1[1]
    x_ball_2 = ball_2[0]
    y_ball_2 = ball_2[1]
    # calculate distance between balls
    distance = (((x_ball_2 - x_ball_1) **2 ) + (y_ball_2 - y_ball_1) ** 2 ) \
               ** (1/2)
    # decide if they are colliding
    if distance <= sum_of_radii:
        return True
    else:
        return False

# test it - should be true because (9 + 3) > 8.062
tuple_1 = (3, -4, 9)
tuple_2 = (-1, 3, 3)
variable = isColliding(tuple_1, tuple_2)
print(variable)

'''------------------ OUTPUT PART 1
True
OUTPUT PART 1------------------ '''

# Part 2 - Shopping for cheese
# copy/pasted code:

myCheeseList = [ "Apple", "Asiago", "Brie", "Caerphilly", "Emmental", "Gloucester", "Gouda",]

for i in range(len(myCheeseList)) :
     if  i==2 :
         del (myCheeseList[4])
     print( i, myCheeseList[i] )

'''
the runtime error alerts you that the index is out of range
 it happens on line 54 when i = 6; there isn't an i=6th (7th) element because
 we deleted an element when i = 2. There are no longer 7 items in the list.
'''


'''------------------ OUTPUT PART 2
0 Apple
1 Asiago
2 Brie
3 Caerphilly
4 Gloucester
5 Gouda
Traceback (most recent call last):
  File "assignment_6_Ashley_King_winter_2019.py", line 53, in <module>
    print( i, myCheeseList[i] )
IndexError: list index out of range
OUTPUT PART 2------------------ '''

# solutions
'''
Possible Solution 1: obviously, don't remove the item while you are iterating
  over the list. Remove it before, then iterate over the list and print.
Possible Solution 2: use a list comprehension to create a new list excluding
  the item you want to remove. Iterate over the new list and print the
  elements.
Possible Solution 3: create a dictionary i:cheese; print out all the
  key:value pairs unless key = 4 or value = Emmental
'''

# Part 3 - Facts about files, dictionaries and tuples
'''
Files: 
    1. The open function does not read the whole file, as it might be 
    exceptionally large. Opening the file returns a handle vs the data in the 
    file.
    2. String methods allow us to read and process only certain pieces of a 
    file.
Dictionaries:
    1. The indices in a dictionary can be almost any type. They don't have to 
    be integers.
    2. Dictionaries can be used to count the occurrence of words in a file, 
    which I thought was a pretty handy use for them.
Tuples:
    1. I thought that a tuple was a key-value pair (a pair, like a two-ple) 
    before this course. Tuples are actually a type of immutable list.
    2. I love this aspect of tuple assignment: 
       m = ['one', 'two']
       (x,y) = m
       which means:
       x = one
       y = two
    
'''

# Part 4 - Dictionaries

# Part 4A - English to Spanish Dictionary:
''' Algorithm Part 4A:
1. create lists of dictionary words
2. instantiate dictionary
3. for each word in list of english words, add key-value pair to dictionary.
   using english words as keys and spanish words as values
4. try to look up key passed into function; if it exists return the value; 
   if it doesn't exist return an empty string
'''

def translate(word):
    # create lists
    en_words = ['bee', 'iguana', 'scorpion', 'giraffe', 'spider']
    sp_words = ['abeja', 'iguana', 'alacrán', 'jirafa', 'araña']
    # create english to spanish dictionary
    sp_en_dict = dict()
    # # create dictionaries
    for i in range(len(en_words)):
        sp_en_dict[en_words[i]] = sp_words[i]
    # return spanish translation or empty string
    try:
        return sp_en_dict[word]
    except:
        return ''

# test cases
print('The Spanish word for bee is: ' + translate('bee'))
print('The Spanish word for iguana is: ' + translate('iguana'))
print('The Spanish word for giraffe is: ' + translate('giraffe'))
print('The Spanish word for spider is: ' + translate('spider'))
print('The Spanish word for flea is: ' + translate('flea'))


'''------------------ OUTPUT PART 4A
The Spanish word for bee is: abeja
The Spanish word for iguana is: iguana
The Spanish word for giraffe is: jirafa
The Spanish word for spider is: araña
The Spanish word for flea is: 
OUTPUT PART 4A------------------ '''


# Part 4B - English to Spanish or Greek Dictionary:

''' Algorithm Part 4B:
1. accept three strings: from language, to language, word to translate (word)
2. standardize case for word
3. instantiate new_word, which will be returned
4. create tuples for each language list of words
5. instantiate dictionaries
6. fill dictionaries using tuples
7. search dictionaries using from and to languages
8. return translation or ' not in dictionary'
'''

def translate(fm, to, word):
    word = word.lower()
    new_word = ''
    # create tuples
    en_words = ('bee', 'iguana', 'scorpion', 'giraffe', 'spider')
    sp_words = ('abeja', 'iguana', 'alacrán', 'jirafa', 'araña')
    gr_words = ('μέλισσα', 'ιγκουάνα', 'σκορπιός', 'καμηλοπάρδαλη',
                'αράχνη')
    # create english to spanish dictionary
    en_sp_dict = dict()
    en_gr_dict = dict()
    gr_sp_dict = dict()
    # # create dictionaries assuming same number of words for each tuple
    for i in range(len(en_words)):
        en_sp_dict[en_words[i]] = sp_words[i]
        en_gr_dict[en_words[i]] = gr_words[i]
        gr_sp_dict[gr_words[i]] = sp_words[i]
    # if fm == eng
    if fm == 'en':
        if to == 'sp':
            try:
                new_word = en_sp_dict[word]
            except:
                new_word = ''
        elif to == 'gr':
            try:
                new_word = en_gr_dict[word]
            except:
                new_word = ''
        # not sp or gr
        else:
            new_word = " wrong 'to' string"
    # if fm == sp
    elif fm == 'sp':
        if to == 'en':
            for eng, span in en_sp_dict.items():
                if span == word:
                    new_word = eng
        elif to == 'gr':
            for gr, span in gr_sp_dict.items():
                if span == word:
                    new_word = gr
        # not sp or gr
        else:
            new_word = " wrong 'to' string"
    # if fm == gr or something else
    else:
        # typed in wrong language string
        if fm != 'gr':
            new_word = " wrong 'from' string"
        else:
            if to == 'sp':
                try:
                    new_word = gr_sp_dict[word]
                except:
                    new_word = ''
            elif to == 'en':
                for eng, grk in en_gr_dict.items():
                    if grk == word:
                        new_word = eng
            # not sp or en
            else:
                new_word = " wrong 'to' string"
    # return new_word
    if new_word == '':
        return 'not in dictionary'
    else:
        return new_word

# many test cases

# english to spanish
print('---------------ENGLISH TO SPANISH---------')
print(' bee = ' + translate('en', 'sp', 'bee'))
print(' iguana = ' + translate('en', 'sp', 'iguana'))
print(' scorpion = ' + translate('en', 'sp', 'scorpion'))
print(' giraffe = ' + translate('en', 'sp', 'giraffe'))
print(' spider = ' + translate('en', 'sp', 'spider'))
print(' cat = ' + translate('en', 'sp', 'cat'))
print(' cat = ' + translate('en', 'fr', 'cat'))

# spanish to english
print('---------------SPANISH TO ENGLISH---------')
print(' abeja = ' + translate('sp', 'en', 'abeja'))
print(' iguana = ' + translate('sp', 'en', 'iguana'))
print(' alacrán = ' + translate('sp', 'en', 'alacrán'))
print(' jirafa = ' + translate('sp', 'en', 'jirafa'))
print(' araña = ' + translate('sp', 'en', 'araña'))
print(' gato = ' + translate('sp', 'en', 'gato'))
print(' gato = ' + translate('sp', 'fr', 'gato'))
# english to greek
print('---------------ENGLISH TO GREEK---------')
print(' bee = ' + translate('en', 'gr', 'bee'))
print(' iguana = ' + translate('en', 'gr', 'iguana'))
print(' scorpion = ' + translate('en', 'gr', 'scorpion'))
print(' giraffe = ' + translate('en', 'gr', 'giraffe'))
print(' spider = ' + translate('en', 'gr', 'spider'))
print(' cat = ' + translate('en', 'gr', 'cat'))
print(' cat = ' + translate('en', 'fr', 'cat'))
# greek to english
print('---------------GREEK TO ENGLISH---------')
print(' μέλισσα = ' + translate('gr', 'en', 'μέλισσα'))
print(' ιγκουάνα = ' + translate('gr', 'en', 'ιγκουάνα'))
print(' σκορπιός = ' + translate('gr', 'en', 'σκορπιός'))
print(' καμηλοπάρδαλη = ' + translate('gr', 'en', 'καμηλοπάρδαλη'))
print(' αράχνη = ' + translate('gr', 'en', 'αράχνη'))
print(' Γάτα = ' + translate('gr', 'en', 'Γάτα'))
print(' Γάτα = ' + translate('gr', 'fr', 'Γάτα'))
# spanish to greek
print('---------------SPANISH TO GREEK---------')
print(' abeja = ' + translate('sp', 'gr', 'abeja'))
print(' iguana = ' + translate('sp', 'gr', 'iguana'))
print(' alacrán = ' + translate('sp', 'gr', 'alacrán'))
print(' jirafa = ' + translate('sp', 'gr', 'jirafa'))
print(' araña = ' + translate('sp', 'gr', 'araña'))
print(' gato = ' + translate('sp', 'gr', 'gato'))
print(' gato = ' + translate('sp', 'fr', 'gato'))
# greek to spanish
print('---------------GREEK TO SPANISH---------')
print(' μέλισσα = ' + translate('gr', 'sp', 'μέλισσα'))
print(' ιγκουάνα = ' + translate('gr', 'sp', 'ιγκουάνα'))
print(' σκορπιός = ' + translate('gr', 'sp', 'σκορπιός'))
print(' καμηλοπάρδαλη = ' + translate('gr', 'sp', 'καμηλοπάρδαλη'))
print(' αράχνη = ' + translate('gr', 'sp', 'αράχνη'))
print(' Γάτα = ' + translate('gr', 'sp', 'Γάτα'))
print(' Γάτα = ' + translate('gr', 'fr', 'Γάτα'))
print(' Γάτα = ' + translate('fr', 'sp', 'Γάτα'))



'''------------------ OUTPUT PART 4B
---------------ENGLISH TO SPANISH---------
 bee = abeja
 iguana = iguana
 scorpion = alacrán
 giraffe = jirafa
 spider = araña
 cat = not in dictionary
 cat =  wrong 'to' string
---------------SPANISH TO ENGLISH---------
 abeja = bee
 iguana = iguana
 alacrán = scorpion
 jirafa = giraffe
 araña = spider
 gato = not in dictionary
 gato =  wrong 'to' string
---------------ENGLISH TO GREEK---------
 bee = μέλισσα
 iguana = ιγκουάνα
 scorpion = σκορπιός
 giraffe = καμηλοπάρδαλη
 spider = αράχνη
 cat = not in dictionary
 cat =  wrong 'to' string
---------------GREEK TO ENGLISH---------
 μέλισσα = bee
 ιγκουάνα = iguana
 σκορπιός = scorpion
 καμηλοπάρδαλη = giraffe
 αράχνη = spider
 Γάτα = not in dictionary
 Γάτα =  wrong 'to' string
---------------SPANISH TO GREEK---------
 abeja = μέλισσα
 iguana = ιγκουάνα
 alacrán = σκορπιός
 jirafa = καμηλοπάρδαλη
 araña = αράχνη
 gato = not in dictionary
 gato =  wrong 'to' string
---------------GREEK TO SPANISH---------
 μέλισσα = abeja
 ιγκουάνα = iguana
 σκορπιός = alacrán
 καμηλοπάρδαλη = jirafa
 αράχνη = araña
 Γάτα = not in dictionary
 Γάτα =  wrong 'to' string
 Γάτα =  wrong 'from' string
OUTPUT PART 4B------------------ '''