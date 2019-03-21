# # # ''' Algorithm Part 4B:
# # # # # 1. accept three strings: from language, to language, word to translate (word)
# # # # # 2. standardize case for word
# # # # # 3. instantiate new_word, which will be returned
# # # # # 4. create tuples for each language list of words
# # # # # 5. instantiate dictionaries
# # # # # 6. fill dictionaries using tuples
# # # # # 7. search dictionaries using from and to languages
# # # # # 8. return translation or ' not in dictionary'
# # # # # '''
# # # # #
# # # # # def translate(fm, to, word):
# # # # #     word = word.lower()
# # # # #     new_word = ''
# # # # #     # create tuples
# # # # #     en_words = ('bee', 'iguana', 'scorpion', 'giraffe', 'spider')
# # # # #     sp_words = ('abeja', 'iguana', 'alacrán', 'jirafa', 'araña')
# # # # #     gr_words = ('μέλισσα', 'ιγκουάνα', 'σκορπιός', 'καμηλοπάρδαλη',
# # # # #                 'αράχνη')
# # # # #     # create english to spanish dictionary
# # # # #     en_sp_dict = dict()
# # # # #     en_gr_dict = dict()
# # # # #     gr_sp_dict = dict()
# # # # #     # # create dictionaries assuming same number of words for each tuple
# # # # #     for i in range(len(en_words)):
# # # # #         en_sp_dict[en_words[i]] = sp_words[i]
# # # # #         en_gr_dict[en_words[i]] = gr_words[i]
# # # # #         gr_sp_dict[gr_words[i]] = sp_words[i]
# # # # #     # if fm == eng
# # # # #     if fm == 'en':
# # # # #         if to == 'sp':
# # # # #             try:
# # # # #                 new_word = en_sp_dict[word]
# # # # #             except:
# # # # #                 new_word = ''
# # # # #         elif to == 'gr':
# # # # #             try:
# # # # #                 new_word = en_gr_dict[word]
# # # # #             except:
# # # # #                 new_word = ''
# # # # #         # not sp or gr
# # # # #         else:
# # # # #             new_word = " wrong 'to' string"
# # # # #     # if fm == sp
# # # # #     elif fm == 'sp':
# # # # #         if to == 'en':
# # # # #             for eng, span in en_sp_dict.items():
# # # # #                 if span == word:
# # # # #                     new_word = eng
# # # # #         elif to == 'gr':
# # # # #             for gr, span in gr_sp_dict.items():
# # # # #                 if span == word:
# # # # #                     new_word = gr
# # # # #         # not sp or gr
# # # # #         else:
# # # # #             new_word = " wrong 'to' string"
# # # # #     # if fm == gr or something else
# # # # #     else:
# # # # #         # typed in wrong language string
# # # # #         if fm != 'gr':
# # # # #             new_word = " wrong 'from' string"
# # # # #         else:
# # # # #             if to == 'sp':
# # # # #                 try:
# # # # #                     new_word = gr_sp_dict[word]
# # # # #                 except:
# # # # #                     new_word = ''
# # # # #             elif to == 'en':
# # # # #                 for eng, grk in en_gr_dict.items():
# # # # #                     if grk == word:
# # # # #                         new_word = eng
# # # # #             # not sp or en
# # # # #             else:
# # # # #                 new_word = " wrong 'to' string"
# # # # #     # return new_word
# # # # #     if new_word == '':
# # # # #         return 'not in dictionary'
# # # # #     else:
# # # # #         return new_word
# # # # #
# # # # # # many test cases
# # # # #
# # # # # # english to spanish
# # # # # print('---------------ENGLISH TO SPANISH---------')
# # # # # print(' bee = ' + translate('en', 'sp', 'bee'))
# # # # # print(' iguana = ' + translate('en', 'sp', 'iguana'))
# # # # # print(' scorpion = ' + translate('en', 'sp', 'scorpion'))
# # # # # print(' giraffe = ' + translate('en', 'sp', 'giraffe'))
# # # # # print(' spider = ' + translate('en', 'sp', 'spider'))
# # # # # print(' cat = ' + translate('en', 'sp', 'cat'))
# # # # # print(' cat = ' + translate('en', 'fr', 'cat'))
# # # # #
# # # # # # spanish to english
# # # # # print('---------------SPANISH TO ENGLISH---------')
# # # # # print(' abeja = ' + translate('sp', 'en', 'abeja'))
# # # # # print(' iguana = ' + translate('sp', 'en', 'iguana'))
# # # # # print(' alacrán = ' + translate('sp', 'en', 'alacrán'))
# # # # # print(' jirafa = ' + translate('sp', 'en', 'jirafa'))
# # # # # print(' araña = ' + translate('sp', 'en', 'araña'))
# # # # # print(' gato = ' + translate('sp', 'en', 'gato'))
# # # # # print(' gato = ' + translate('sp', 'fr', 'gato'))
# # # # # # english to greek
# # # # # print('---------------ENGLISH TO GREEK---------')
# # # # # print(' bee = ' + translate('en', 'gr', 'bee'))
# # # # # print(' iguana = ' + translate('en', 'gr', 'iguana'))
# # # # # print(' scorpion = ' + translate('en', 'gr', 'scorpion'))
# # # # # print(' giraffe = ' + translate('en', 'gr', 'giraffe'))
# # # # # print(' spider = ' + translate('en', 'gr', 'spider'))
# # # # # print(' cat = ' + translate('en', 'gr', 'cat'))
# # # # # print(' cat = ' + translate('en', 'fr', 'cat'))
# # # # # # greek to english
# # # # # print('---------------GREEK TO ENGLISH---------')
# # # # # print(' μέλισσα = ' + translate('gr', 'en', 'μέλισσα'))
# # # # # print(' ιγκουάνα = ' + translate('gr', 'en', 'ιγκουάνα'))
# # # # # print(' σκορπιός = ' + translate('gr', 'en', 'σκορπιός'))
# # # # # print(' καμηλοπάρδαλη = ' + translate('gr', 'en', 'καμηλοπάρδαλη'))
# # # # # print(' αράχνη = ' + translate('gr', 'en', 'αράχνη'))
# # # # # print(' Γάτα = ' + translate('gr', 'en', 'Γάτα'))
# # # # # print(' Γάτα = ' + translate('gr', 'fr', 'Γάτα'))
# # # # # # spanish to greek
# # # # # print('---------------SPANISH TO GREEK---------')
# # # # # print(' abeja = ' + translate('sp', 'gr', 'abeja'))
# # # # # print(' iguana = ' + translate('sp', 'gr', 'iguana'))
# # # # # print(' alacrán = ' + translate('sp', 'gr', 'alacrán'))
# # # # # print(' jirafa = ' + translate('sp', 'gr', 'jirafa'))
# # # # # print(' araña = ' + translate('sp', 'gr', 'araña'))
# # # # # print(' gato = ' + translate('sp', 'gr', 'gato'))
# # # # # print(' gato = ' + translate('sp', 'fr', 'gato'))
# # # # # # greek to spanish
# # # # # print('---------------GREEK TO SPANISH---------')
# # # # # print(' μέλισσα = ' + translate('gr', 'sp', 'μέλισσα'))
# # # # # print(' ιγκουάνα = ' + translate('gr', 'sp', 'ιγκουάνα'))
# # # # # print(' σκορπιός = ' + translate('gr', 'sp', 'σκορπιός'))
# # # # # print(' καμηλοπάρδαλη = ' + translate('gr', 'sp', 'καμηλοπάρδαλη'))
# # # # # print(' αράχνη = ' + translate('gr', 'sp', 'αράχνη'))
# # # # # print(' Γάτα = ' + translate('gr', 'sp', 'Γάτα'))
# # # # # print(' Γάτα = ' + translate('gr', 'fr', 'Γάτα'))
# # # # # print(' Γάτα = ' + translate('fr', 'sp', 'Γάτα'))
# #
# # # import random mpodule
# # import random
# #
# #
# # # gets bet from user; $0 to $50; returns user input
# # # gets input until legal input obtained
# # def get_bet():
# #     bet = -1
# #     bet_question = "Please place a bet between 0 and 50 dollars, 0 to quit: "
# #     while bet < 0 or bet > 50:
# #         print(bet_question, end = ' ')
# #         bet = input()
# #         try:
# #             bet = int(bet)
# #         except:
# #             bet = -1
# #     return bet
# #
# # # TripleString
# # class TripleString:
# #     """ encapsulates a 3-string object """
# #
# #     # intended class constants ------------------------------------
# #     MIN_LEN = 1
# #     MAX_LEN = 50
# #     DEFAULT_STRING = "(undefined)"
# #
# #     # constructor method ------------------------------------
# #     def __init__(self, string1 = DEFAULT_STRING, string2 = DEFAULT_STRING,
# #                  string3 = DEFAULT_STRING ):
# #         # instance attributes
# #         self.string1 = string1
# #         self.string2 = string2
# #         self.string3= string3
# #
# #     # mutator ("set") methods -------------------------------
# #     def set_string1(self, new_string):
# #         if self.valid_string(new_string):
# #             self.string1 = new_string
# #             return True
# #         else:
# #             return False
# #
# #     def set_string2(self, new_string):
# #         if self.valid_string(new_string):
# #             self.string2 = new_string
# #             return True
# #         else:
# #             return False
# #
# #     def set_string3(self, new_string):
# #         if self.valid_string(new_string):
# #             self.string3 = new_string
# #             return True
# #         else:
# #             return False
# #
# #     # accessor ("get") methods -------------------------------
# #     def get_string1(self):
# #         return self.string1
# #
# #     def get_string2(self):
# #         return self.string2
# #
# #     def get_string3(self):
# #         return self.string3
# #
# #     # helper methods for entire class -----------------
# #     def valid_string(self, a_string):
# #         if(len(a_string) >= TripleString.MIN_LEN and len(a_string) <=
# #             TripleString.MAX_LEN):
# #             return True
# #         else:
# #             return False
# #
# # def rand_string():
# #         num =  random.randrange(1, 101,1)
# #         if num <= 40:
# #             return 'CHERRIES'
# #         elif num > 40 and num <= 78:
# #             return 'BAR'
# #         elif num > 78 and num <= 93:
# #             return '7'
# #         else:
# #             return 'SPACE'
# #
# # def pull():
# #     reels = TripleString()
# #     str1 = rand_string()
# #     reels.set_string1(str1)
# #     str2 = rand_string()
# #     reels.set_string2(str2)
# #     str3 = rand_string()
# #     reels.set_string3(str3)
# #     return reels
# #
# #
# #
# # newpull = pull()
# # flag_50_seen_counter = 1
# # flag_30_seen_counter = 2
# # print('''
# #         GAME OVER. Thanks for playing!
# #         CHERRIES CHERRIES CHERRIES was seen at run number: '''
# #         + str(flag_30_seen_counter) +
# #       '''
# #         BAR BAR BAR was seen at run number: '''
# #         + str(flag_50_seen_counter)
# #         )
#
# ''' translate the 1000 most common words into English, Spanish, Greek,  PvdL, Nov 2017'''
#
# from timeit import default_timer as timer
#
# with open('1kwords.en.txt', encoding='utf-8') as f:
#     enl = f.read().splitlines()
#
# with open('1kwords.sp.txt', encoding='utf-8') as f:
#     spl = f.read().splitlines()
#
# with open('1kwords.gr.txt', encoding='utf-8') as f:
#     grl = f.read().splitlines()
#
#
# def translate(fm, to, word):
#     if   fm == "en": d = den
#     elif fm == "sp": d = dsp
#     else           : d = dgr
#
#     if   to == "en": inx = 0
#     elif to == "sp": inx = 1
#     else           : inx = 2
#     try:
#         translation = d[word][inx]
#     except KeyError:
#         translation = ""   # "<no word>"
#     return translation
#
# def func_to_measure():
#     spbee = translate("gr","sp", "μέλισσα")
#     translate("sp","en", spbee)
#     translate("en","sp", "heart")
#     translate("en","gr", "heart")
#     translate("en","gr", "diegetic")
#     translate("gr", "en", "μέλισσα")
#     spneck = translate("en", "sp", "neck")
#     translate("en", "gr", "neck")
#     translate("sp", "gr", spneck)
#     translate("en", "sp", "beauty")
#
# wlist = list(zip(enl, spl, grl))
#
# den = { } # empty dict
# dsp = { }
# dgr = { }
#
# #  you look it up in English to get the key
# #  when you have the key, look it up in the dict for that lang.
#
# for t in wlist:
#     den[t[0]] = ("", t[1], t[2])
#     dsp[t[1]] = (t[0], "", t[2])
#     dgr[t[2]] = (t[0],t[1], "")
#
# print("starting timer")
# start = timer()
# for i in range(1000000):
#     func_to_measure()
# end= timer()
#
# elapsed = end - start
# print("10M words translated in", elapsed, "secs")# # ''' Algorithm Part 4B:
# # # # # # 1. accept three strings: from language, to language, word to translate (word)
# # # # # # 2. standardize case for word
# # # # # # 3. instantiate new_word, which will be returned
# # # # # # 4. create tuples for each language list of words
# # # # # # 5. instantiate dictionaries
# # # # # # 6. fill dictionaries using tuples
# # # # # # 7. search dictionaries using from and to languages
# # # # # # 8. return translation or ' not in dictionary'
# # # # # # '''
# # # # # #
# # # # # # def translate(fm, to, word):
# # # # # #     word = word.lower()
# # # # # #     new_word = ''
# # # # # #     # create tuples
# # # # # #     en_words = ('bee', 'iguana', 'scorpion', 'giraffe', 'spider')
# # # # # #     sp_words = ('abeja', 'iguana', 'alacrán', 'jirafa', 'araña')
# # # # # #     gr_words = ('μέλισσα', 'ιγκουάνα', 'σκορπιός', 'καμηλοπάρδαλη',
# # # # # #                 'αράχνη')
# # # # # #     # create english to spanish dictionary
# # # # # #     en_sp_dict = dict()
# # # # # #     en_gr_dict = dict()
# # # # # #     gr_sp_dict = dict()
# # # # # #     # # create dictionaries assuming same number of words for each tuple
# # # # # #     for i in range(len(en_words)):
# # # # # #         en_sp_dict[en_words[i]] = sp_words[i]
# # # # # #         en_gr_dict[en_words[i]] = gr_words[i]
# # # # # #         gr_sp_dict[gr_words[i]] = sp_words[i]
# # # # # #     # if fm == eng
# # # # # #     if fm == 'en':
# # # # # #         if to == 'sp':
# # # # # #             try:
# # # # # #                 new_word = en_sp_dict[word]
# # # # # #             except:
# # # # # #                 new_word = ''
# # # # # #         elif to == 'gr':
# # # # # #             try:
# # # # # #                 new_word = en_gr_dict[word]
# # # # # #             except:
# # # # # #                 new_word = ''
# # # # # #         # not sp or gr
# # # # # #         else:
# # # # # #             new_word = " wrong 'to' string"
# # # # # #     # if fm == sp
# # # # # #     elif fm == 'sp':
# # # # # #         if to == 'en':
# # # # # #             for eng, span in en_sp_dict.items():
# # # # # #                 if span == word:
# # # # # #                     new_word = eng
# # # # # #         elif to == 'gr':
# # # # # #             for gr, span in gr_sp_dict.items():
# # # # # #                 if span == word:
# # # # # #                     new_word = gr
# # # # # #         # not sp or gr
# # # # # #         else:
# # # # # #             new_word = " wrong 'to' string"
# # # # # #     # if fm == gr or something else
# # # # # #     else:
# # # # # #         # typed in wrong language string
# # # # # #         if fm != 'gr':
# # # # # #             new_word = " wrong 'from' string"
# # # # # #         else:
# # # # # #             if to == 'sp':
# # # # # #                 try:
# # # # # #                     new_word = gr_sp_dict[word]
# # # # # #                 except:
# # # # # #                     new_word = ''
# # # # # #             elif to == 'en':
# # # # # #                 for eng, grk in en_gr_dict.items():
# # # # # #                     if grk == word:
# # # # # #                         new_word = eng
# # # # # #             # not sp or en
# # # # # #             else:
# # # # # #                 new_word = " wrong 'to' string"
# # # # # #     # return new_word
# # # # # #     if new_word == '':
# # # # # #         return 'not in dictionary'
# # # # # #     else:
# # # # # #         return new_word
# # # # # #
# # # # # # # many test cases
# # # # # #
# # # # # # # english to spanish
# # # # # # print('---------------ENGLISH TO SPANISH---------')
# # # # # # print(' bee = ' + translate('en', 'sp', 'bee'))
# # # # # # print(' iguana = ' + translate('en', 'sp', 'iguana'))
# # # # # # print(' scorpion = ' + translate('en', 'sp', 'scorpion'))
# # # # # # print(' giraffe = ' + translate('en', 'sp', 'giraffe'))
# # # # # # print(' spider = ' + translate('en', 'sp', 'spider'))
# # # # # # print(' cat = ' + translate('en', 'sp', 'cat'))
# # # # # # print(' cat = ' + translate('en', 'fr', 'cat'))
# # # # # #
# # # # # # # spanish to english
# # # # # # print('---------------SPANISH TO ENGLISH---------')
# # # # # # print(' abeja = ' + translate('sp', 'en', 'abeja'))
# # # # # # print(' iguana = ' + translate('sp', 'en', 'iguana'))
# # # # # # print(' alacrán = ' + translate('sp', 'en', 'alacrán'))
# # # # # # print(' jirafa = ' + translate('sp', 'en', 'jirafa'))
# # # # # # print(' araña = ' + translate('sp', 'en', 'araña'))
# # # # # # print(' gato = ' + translate('sp', 'en', 'gato'))
# # # # # # print(' gato = ' + translate('sp', 'fr', 'gato'))
# # # # # # # english to greek
# # # # # # print('---------------ENGLISH TO GREEK---------')
# # # # # # print(' bee = ' + translate('en', 'gr', 'bee'))
# # # # # # print(' iguana = ' + translate('en', 'gr', 'iguana'))
# # # # # # print(' scorpion = ' + translate('en', 'gr', 'scorpion'))
# # # # # # print(' giraffe = ' + translate('en', 'gr', 'giraffe'))
# # # # # # print(' spider = ' + translate('en', 'gr', 'spider'))
# # # # # # print(' cat = ' + translate('en', 'gr', 'cat'))
# # # # # # print(' cat = ' + translate('en', 'fr', 'cat'))
# # # # # # # greek to english
# # # # # # print('---------------GREEK TO ENGLISH---------')
# # # # # # print(' μέλισσα = ' + translate('gr', 'en', 'μέλισσα'))
# # # # # # print(' ιγκουάνα = ' + translate('gr', 'en', 'ιγκουάνα'))
# # # # # # print(' σκορπιός = ' + translate('gr', 'en', 'σκορπιός'))
# # # # # # print(' καμηλοπάρδαλη = ' + translate('gr', 'en', 'καμηλοπάρδαλη'))
# # # # # # print(' αράχνη = ' + translate('gr', 'en', 'αράχνη'))
# # # # # # print(' Γάτα = ' + translate('gr', 'en', 'Γάτα'))
# # # # # # print(' Γάτα = ' + translate('gr', 'fr', 'Γάτα'))
# # # # # # # spanish to greek
# # # # # # print('---------------SPANISH TO GREEK---------')
# # # # # # print(' abeja = ' + translate('sp', 'gr', 'abeja'))
# # # # # # print(' iguana = ' + translate('sp', 'gr', 'iguana'))
# # # # # # print(' alacrán = ' + translate('sp', 'gr', 'alacrán'))
# # # # # # print(' jirafa = ' + translate('sp', 'gr', 'jirafa'))
# # # # # # print(' araña = ' + translate('sp', 'gr', 'araña'))
# # # # # # print(' gato = ' + translate('sp', 'gr', 'gato'))
# # # # # # print(' gato = ' + translate('sp', 'fr', 'gato'))
# # # # # # # greek to spanish
# # # # # # print('---------------GREEK TO SPANISH---------')
# # # # # # print(' μέλισσα = ' + translate('gr', 'sp', 'μέλισσα'))
# # # # # # print(' ιγκουάνα = ' + translate('gr', 'sp', 'ιγκουάνα'))
# # # # # # print(' σκορπιός = ' + translate('gr', 'sp', 'σκορπιός'))
# # # # # # print(' καμηλοπάρδαλη = ' + translate('gr', 'sp', 'καμηλοπάρδαλη'))
# # # # # # print(' αράχνη = ' + translate('gr', 'sp', 'αράχνη'))
# # # # # # print(' Γάτα = ' + translate('gr', 'sp', 'Γάτα'))
# # # # # # print(' Γάτα = ' + translate('gr', 'fr', 'Γάτα'))
# # # # # # print(' Γάτα = ' + translate('fr', 'sp', 'Γάτα'))
# # #
# # # # import random mpodule
# # # import random
# # #
# # #
# # # # gets bet from user; $0 to $50; returns user input
# # # # gets input until legal input obtained
# # # def get_bet():
# # #     bet = -1
# # #     bet_question = "Please place a bet between 0 and 50 dollars, 0 to quit: "
# # #     while bet < 0 or bet > 50:
# # #         print(bet_question, end = ' ')
# # #         bet = input()
# # #         try:
# # #             bet = int(bet)
# # #         except:
# # #             bet = -1
# # #     return bet
# # #
# # # # TripleString
# # # class TripleString:
# # #     """ encapsulates a 3-string object """
# # #
# # #     # intended class constants ------------------------------------
# # #     MIN_LEN = 1
# # #     MAX_LEN = 50
# # #     DEFAULT_STRING = "(undefined)"
# # #
# # #     # constructor method ------------------------------------
# # #     def __init__(self, string1 = DEFAULT_STRING, string2 = DEFAULT_STRING,
# # #                  string3 = DEFAULT_STRING ):
# # #         # instance attributes
# # #         self.string1 = string1
# # #         self.string2 = string2
# # #         self.string3= string3
# # #
# # #     # mutator ("set") methods -------------------------------
# # #     def set_string1(self, new_string):
# # #         if self.valid_string(new_string):
# # #             self.string1 = new_string
# # #             return True
# # #         else:
# # #             return False
# # #
# # #     def set_string2(self, new_string):
# # #         if self.valid_string(new_string):
# # #             self.string2 = new_string
# # #             return True
# # #         else:
# # #             return False
# # #
# # #     def set_string3(self, new_string):
# # #         if self.valid_string(new_string):
# # #             self.string3 = new_string
# # #             return True
# # #         else:
# # #             return False
# # #
# # #     # accessor ("get") methods -------------------------------
# # #     def get_string1(self):
# # #         return self.string1
# # #
# # #     def get_string2(self):
# # #         return self.string2
# # #
# # #     def get_string3(self):
# # #         return self.string3
# # #
# # #     # helper methods for entire class -----------------
# # #     def valid_string(self, a_string):
# # #         if(len(a_string) >= TripleString.MIN_LEN and len(a_string) <=
# # #             TripleString.MAX_LEN):
# # #             return True
# # #         else:
# # #             return False
# # #
# # # def rand_string():
# # #         num =  random.randrange(1, 101,1)
# # #         if num <= 40:
# # #             return 'CHERRIES'
# # #         elif num > 40 and num <= 78:
# # #             return 'BAR'
# # #         elif num > 78 and num <= 93:
# # #             return '7'
# # #         else:
# # #             return 'SPACE'
# # #
# # # def pull():
# # #     reels = TripleString()
# # #     str1 = rand_string()
# # #     reels.set_string1(str1)
# # #     str2 = rand_string()
# # #     reels.set_string2(str2)
# # #     str3 = rand_string()
# # #     reels.set_string3(str3)
# # #     return reels
# # #
# # #
# # #
# # # newpull = pull()
# # # flag_50_seen_counter = 1
# # # flag_30_seen_counter = 2
# # # print('''
# # #         GAME OVER. Thanks for playing!
# # #         CHERRIES CHERRIES CHERRIES was seen at run number: '''
# # #         + str(flag_30_seen_counter) +
# # #       '''
# # #         BAR BAR BAR was seen at run number: '''
# # #         + str(flag_50_seen_counter)
# # #         )
# #
# # ''' translate the 1000 most common words into English, Spanish, Greek,  PvdL, Nov 2017'''
# #
# # from timeit import default_timer as timer
# #
# # with open('1kwords.en.txt', encoding='utf-8') as f:
# #     enl = f.read().splitlines()
# #
# # with open('1kwords.sp.txt', encoding='utf-8') as f:
# #     spl = f.read().splitlines()
# #
# # with open('1kwords.gr.txt', encoding='utf-8') as f:
# #     grl = f.read().splitlines()
# #
# #
# # def translate(fm, to, word):
# #     if   fm == "en": d = den
# #     elif fm == "sp": d = dsp
# #     else           : d = dgr
# #
# #     if   to == "en": inx = 0
# #     elif to == "sp": inx = 1
# #     else           : inx = 2
# #     try:
# #         translation = d[word][inx]
# #     except KeyError:
# #         translation = ""   # "<no word>"
# #     return translation
# #
# # def func_to_measure():
# #     spbee = translate("gr","sp", "μέλισσα")
# #     translate("sp","en", spbee)
# #     translate("en","sp", "heart")
# #     translate("en","gr", "heart")
# #     translate("en","gr", "diegetic")
# #     translate("gr", "en", "μέλισσα")
# #     spneck = translate("en", "sp", "neck")
# #     translate("en", "gr", "neck")
# #     translate("sp", "gr", spneck)
# #     translate("en", "sp", "beauty")
# #
# # wlist = list(zip(enl, spl, grl))
# #
# # den = { } # empty dict
# # dsp = { }
# # dgr = { }
# #
# # #  you look it up in English to get the key
# # #  when you have the key, look it up in the dict for that lang.
# #
# # for t in wlist:
# #     den[t[0]] = ("", t[1], t[2])
# #     dsp[t[1]] = (t[0], "", t[2])
# #     dgr[t[2]] = (t[0],t[1], "")
# #
# # print("starting timer")
# # start = timer()
# # for i in range(1000000):
# #     func_to_measure()
# # end= timer()
# #
# # elapsed = end - start
# # print("10M words translated in", elapsed, "secs")
# # # print("1000 words takes", elapsed/10000, "secs")
# # print("1000 words takes", elapsed/10000, "secs")




