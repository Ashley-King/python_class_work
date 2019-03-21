'''
    Assignment: 9 - How Fast Benchmark
    Author: Ashley King
    Date: 2019-03-07
    Description: Benchmarking a translation app
'''
from timeit import default_timer as timer

def makeDict(input_file_name):
   with open(input_file_name, 'r', encoding = 'utf-8') as f:
      dict_list = f.readlines()
      index = 0
      while index < len(dict_list):
         dict_list[index] = dict_list[index].rstrip('\n')
         index += 1
   keys = (x for x in range(1, 1001))
   return dict(zip(keys, dict_list))

en_dict = makeDict("1kwords.en.txt")
sp_dict = makeDict("1kwords.sp.txt")
gr_dict = makeDict("1kwords.gr.txt")

dict_language = {"en": en_dict, "sp": sp_dict, "gr": gr_dict}

def translate(fm, to, word):
   if fm not in dict_language.keys():
      return("from is not a valid language code.")
   elif to not in dict_language.keys():
      return("to not a valid language code.")
   else:
      for i in range(1,1001):
         if fm == to:
            return( word )
         if word not in dict_language[fm].values():
            return("The word you want to look up is not in the dictionary.")
         if dict_language[fm][i] == word:
            # remove quotations marks (bug)
            return(dict_language[to][i])

# print(translate("en", "gr", "light"))
# print(translate("en", "sp", "light"))
# print(translate("sp", "en", "momento"))
# print(translate("sp", "gr", "momento"))
# print(translate("gr", "en", "πολλαπλασιάστε"))
# print(translate("gr", "sp", "πολλαπλασιάστε"))
# print(translate("en", "gr", "giraffe"))

def func_to_measure():
    spbee = translate("gr","sp", "μέλισσα")
    translate("sp","en", spbee)
    translate("en","sp", "heart")
    translate("en","gr", "heart")
    translate("en","gr", "diegetic")
    translate("gr", "en", "μέλισσα")
    spneck = translate("en", "sp", "neck")
    translate("en", "gr", "neck")
    translate("sp", "gr", spneck)
    translate("en", "sp", "beauty")
    # spbee = translate("gr", "sp", "μέλισσα")
    # print(translate("sp","en", spbee))
    # print(translate("en","sp", "heart"))
    # print(translate("en","gr", "heart"))
    # print(translate("en","gr", "diegetic"))
    # print(translate("gr", "en", "μέλισσα"))
    # spneck = translate("en", "sp", "neck")
    # print(translate("en", "gr", "neck"))
    # print(translate("en", "sp", "beauty"))


# func_to_measure()



print("starting timer")
start = timer()
for i in range(1000):
    func_to_measure()
end= timer()

elapsed = end - start
print("10,000 words translated in", elapsed, "secs")



'''----------------- Fix bug and confirm answer #2 runs --
φως
luz
moment
στιγμή
multiply
multiplicar
The word you want to look up is not in the dictionary.
-- Fix bug and confirm answer #2 runs -------------------'''


'''------- comment out all print statements and benchmark --
starting timer
10,000 words translated in 89.380125304 secs
-- comment out all print statements and benchmark ----------'''


'''------- comment out other print statements and call func_to_measure() --
bee
corazón
καρδιά
The word you want to look up is not in the dictionary.
bee
λαιμός
belleza
-- comment out print statements and call func_to_measure() ----------'''


'''------ the time difference between the two programs
The output of program #4: 10M words translated in 3.043114749 secs

The output of program #2: 10,000 words translated in 89.380125304 secs

Program #4 uses alias and tuples. This makes the lookups faster and the code 
less verbose. Tuples tend to perform better than lists (used in #2), as they
use a single block of memory while lists require 2 blocks.

Program #2 uses lists and dictionaries that are indexed by numbers rather 
than by dictionary words. It requires linear search, which makes 
it less efficient than a dictionary that uses words for the key:value pairs.

'''