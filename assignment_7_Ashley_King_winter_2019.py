'''
    Assignment: 7 - A Triple String
    Author: Ashley King
    Date: 2019-02-20
    Description: A Simple Class: Triple String
'''
# ---------------- SOURCE ----------------------------------------
class TripleString:
    """ encapsulates a 3-string object """

    # intended class constants ------------------------------------
    MIN_LEN = 1
    MAX_LEN = 50
    DEFAULT_STRING = "(undefined)"

    # constructor method ------------------------------------
    def __init__(self, string1 = DEFAULT_STRING, string2 = DEFAULT_STRING,
                 string3 = DEFAULT_STRING ):
        # instance attributes
        self.string1 = string1
        self.string2 = string2
        self.string3= string3

    # mutator ("set") methods -------------------------------
    def set_string1(self, new_string):
        if self.valid_string(new_string):
            self.string1 = new_string
            return True
        else:
            return False

    def set_string2(self, new_string):
        if self.valid_string(new_string):
            self.string2 = new_string
            return True
        else:
            return False

    def set_string3(self, new_string):
        if self.valid_string(new_string):
            self.string3 = new_string
            return True
        else:
            return False

    # accessor ("get") methods -------------------------------
    def get_string1(self):
        return self.string1

    def get_string2(self):
        return self.string2

    def get_string3(self):
        return self.string3

    # helper methods for entire class -----------------
    def valid_string(self, a_string):
        if(len(a_string) >= TripleString.MIN_LEN and len(a_string) <=
            TripleString.MAX_LEN):
            return True
        else:
            return False


# client --------------------------------------------

one = TripleString("that string")
two = TripleString()
three = TripleString("here's a string", "here's another string")
four = TripleString("Powderville is small.", "I can barely "
                                             "program.", "What's an API?")

# show the strings
# that string, undefined, undefined
print( ("Object 1 immediately after instantiation:"
              + "\n    string1: {}"
              + "\n    string2: {}"
              + "\n    string3: {}").
              format(one.get_string1(), one.get_string2(), one.get_string3()) )
# undefined, undefined, undefined
print( ("Object 2 immediately after instantiation:"
       + "\n    string1: {}"
       + "\n    string2: {}"
       + "\n    string3: {}").
       format(two.get_string1(), two.get_string2(), two.get_string3()) )
# here's a string, here's another string, undefined
print( ("Object 3 immediately after instantiation:"
       + "\n    string1: {}"
       + "\n    string2: {}"
       + "\n    string3: {}").
       format(three.get_string1(), three.get_string2(), three.get_string3()) )
# Powdersville is very small., I can barely program., What's an API?
print( ("Object 4 immediately after instantiation:"
       + "\n    string1: {}"
       + "\n    string2: {}"
       + "\n    string3: {}").
       format(four.get_string1(), four.get_string2(), four.get_string3()) )

'''------------------ OUTPUT PART 1: Object Instantiation
Object 1 immediately after instantiation:
    string1: that string
    string2: (undefined)
    string3: (undefined)
Object 2 immediately after instantiation:
    string1: (undefined)
    string2: (undefined)
    string3: (undefined)
Object 3 immediately after instantiation:
    string1: here's a string
    string2: here's another string
    string3: (undefined)
Object 4 immediately after instantiation:
    string1: Powderville is small.
    string2: I can barely program.
    string3: What's an API?
OUTPUT PART 1------------------ '''



# mutate them
one.set_string1("A brand new string!")
two.set_string2("A brand new day!")
three.set_string3("A brand new puppy!")
four.set_string1("A brand new assignment!")

# show the strings again
# A brand new string!, undefined, undefined
print( ("\nObject 1 after mutation:"
              + "\n    string1: {}"
              + "\n    string2: {}"
              + "\n    string3: {}").
              format(one.get_string1(), one.get_string2(), one.get_string3()) )
# undefined, A brand new day!, undefined
print( ("Object 2 after mutation:"
       + "\n    string1: {}"
       + "\n    string2: {}"
       + "\n    string3: {}").
       format(two.get_string1(), two.get_string2(), two.get_string3()) )
# here's a string, here's another string, A brand new puppy!
print( ("Object 3 after mutation:"
       + "\n    string1: {}"
       + "\n    string2: {}"
       + "\n    string3: {}").
       format(three.get_string1(), three.get_string2(), three.get_string3()) )
# A brand new assignment!, I can barely program., What's an API?
print( ("Object 4 after mutation:"
       + "\n    string1: {}"
       + "\n    string2: {}"
       + "\n    string3: {}").
       format(four.get_string1(), four.get_string2(), four.get_string3()) )
print()

'''------------------ OUTPUT PART 2: Mutation

Object 1 after mutation:
    string1: A brand new string!
    string2: (undefined)
    string3: (undefined)
Object 2 after mutation:
    string1: (undefined)
    string2: A brand new day!
    string3: (undefined)
Object 3 after mutation:
    string1: here's a string
    string2: here's another string
    string3: A brand new puppy!
Object 4 after mutation:
    string1: A brand new assignment!
    string2: I can barely program.
    string3: What's an API?
    
OUTPUT PART 2------------------ '''


# mutator test 1
# The string was changed! Test 1 successful!
if one.set_string1("The test worked"):
    print("The string was changed! Test 1 successful!")
else:
    print("The string was NOT changed Test 1 unsuccessful!")

# mutator test 2
# The string was NOT changed! Test 2 unsuccessful!
if one.set_string2(""):
    print("The string was changed! Test 2 successful!")
else:
    print("The string was NOT changed! Test 2 unsuccessful!")

print()

'''------------------ OUTPUT PART 3: Mutator Test
The string was changed! Test 1 successful!
The string was NOT changed! Test 2 unsuccessful!

OUTPUT PART 3------------------ '''

# accessor calls
# The test worked
print("Accessor call for Object 1, string1: " + one.get_string1())
# here's a string
print("Accessor call for Object 3, string1: " + three.get_string1())

'''------------------ OUTPUT PART 4: Accessor Test
Accessor call for Object 1, string1: The test worked
Accessor call for Object 3, string1: here's a string
OUTPUT PART 4------------------ '''