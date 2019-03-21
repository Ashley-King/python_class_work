'''
    Assignment: 11 - Changing Sort Keys
    Author: Ashley King
    Date: 2019-03-21
    Description: Use different keys for sorting and find median
'''


# beginning of class Student definition -------------------------
class Student:
    # class ("static") members and intended constants
    DEFAULT_NAME = "zz-error"
    DEFAULT_POINTS = 0
    MAX_POINTS = 30

    # new constants
    SORT_BY_FIRST = 88
    SORT_BY_LAST = 98
    SORT_BY_POINTS = 108
    sort_key = SORT_BY_LAST


    # initializer ("constructor") method -------------------
    def __init__(self,
                 last = DEFAULT_NAME,
                 first = DEFAULT_NAME,
                 points = DEFAULT_POINTS):
        # instance attributes
        if (not self.set_last_name(last)):
            self.last_name = Student.DEFAULT_NAME
        if (not self.set_first_name(first)):
            self.first_name = Student.DEFAULT_NAME
        if (not self.set_points(points)):
            self.total_points = Student.DEFAULT_POINTS

    # mutator ("set") methods -------------------------------
    def set_last_name(self, last):
        if not self.valid_string(last):
            return False
        # else
        self.last_name = last
        return True

    def set_first_name(self, first):
        if not self.valid_string(first):
            return False
        # else
        self.first_name = first
        return True

    def set_points(self, points):
        if not self.valid_points(points):
            return False
        # else
        self.total_points = points
        return True

    @classmethod
    def set_sort_key(cls, key):
        cls.sort_key = key
        return True


    # accessor ("get") methods -------------------------------
    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name

    def get_total_points(self):
        return self.total_points

    @classmethod
    def get_sort_key(cls):
        return cls.sort_key

    # output method  ----------------------------------------
    def display(self, client_intro_str = "--- STUDENT DATA ---"):
        print(client_intro_str + str(self))

    # standard python stringizer ------------------------
    def __str__(self):
        return self.to_string()

    # instance helpers -------------------------------
    def to_string(self, optional_title = " ---------- "):
        ret_str = ((optional_title
                    + "\n    name: {}, {}"
                    + "\n    total points: {}.").
                   format(self.last_name, self.first_name,
                          self.total_points))
        return ret_str

    # static/class methods -----------------------------------
    @staticmethod
    def valid_string(test_str):
        if (len(test_str) > 0) and test_str[0].isalpha():
            return True
        return False

    @classmethod
    def valid_points(cls, test_points):
        if 0 <= test_points <= cls.MAX_POINTS:
            return False
        else:
            return True

    @classmethod
    def compare_two_students(cls, first_stud, second_stud):
        if cls.sort_key == cls.SORT_BY_FIRST :
            return cls.compare_strings_ignore_case(first_stud.get_first_name(),
                                                   second_stud.get_first_name())
        elif cls.sort_key == cls.SORT_BY_LAST:
            return cls.compare_strings_ignore_case(first_stud.get_last_name(),
                                                   second_stud.get_last_name())
        else:
            # sort by points
            return first_stud.get_total_points() - second_stud.get_total_points()



    @staticmethod
    def compare_strings_ignore_case(first_string, second_string):
        """ returns -1 if first < second, lexicographically,
            +1 if first > second, and 0 if same
            this particular version based on last name only
            (case insensitive) """

        fst_upper = first_string.upper()
        scnd_upper = second_string.upper()
        if fst_upper < scnd_upper:
            return -1
        # else if
        if fst_upper > scnd_upper:
            return 1
        # else
        return 0


# beginning of class StudentArrayUtilities definition ---------------
class StudentArrayUtilities:
    @classmethod
    def to_string(cls, stud_array,
                        optional_title="--- The Students -----------:\n"):
            return(cls.to_string(stud_array, optional_title))

    @classmethod
    def array_sort(cls, data, array_size):
        for k in range(array_size):
            if not cls.float_largest_to_top(data, array_size - k):
                return

                # class stringizers ----------------------------------

    @classmethod
    def get_median_destructive(cls, array, array_size):
        # bad array_size
        if array_size < 1:
            return 0
        # save sort key and use total points sort key
        old_key = Student.get_sort_key()
        Student.set_sort_key(Student.SORT_BY_POINTS)
        # return element if there's only 1
        if array_size == 1:
            Student.set_sort_key(old_key)
            return array[0].get_total_points()
        # even num of elements
        elif array_size % 2 == 0:
            cls.array_sort(array, array_size)
            # get one of the 2 middle indices
            mid = array_size // 2
            avg = (array[mid].get_total_points() + array[mid-1].get_total_points()) / 2
            Student.set_sort_key(old_key)
            return avg
        # array_size is odd and greater than 1 element
        else:
            cls.array_sort(array, array_size)
            # find index of center value
            mid = array_size // 2
            Student.set_sort_key(old_key)
            return array[mid].get_total_points()


    @staticmethod
    def to_string(stud_array,
                  optional_title = "--- The Students -----------:\n"):
        ret_val = optional_title + "\n"
        for student in stud_array:
            ret_val = ret_val + str(student) + "\n"
        return ret_val

    @staticmethod
    def float_largest_to_top(data, array_size):

        changed = False

        # notice we stop at array_size - 2 because of expr. k + 1 in loop
        for k in range(array_size - 1):
            if Student.compare_two_students(
                data[k], data[k + 1]
            ) > 0:
                data[k], data[k + 1] = data[k + 1], data[k]
                changed = True

        return changed

# client --------------------------------------------

# instantiate some students, one with and illegal name ...
# Even number of students (16)
# median = 123.5
students_1 = \
         [
            Student("smith","freda", 95),
            Student("bauer","jackie",123),
            Student("jacobs","caroline", 194),
            Student("renquist","abbie",173),
            Student("jackson","trent", 108),
            Student("perry","tom",225),
            Student("lewis","franny", 44),
            Student("stollings","pat",552),
            Student("smote","freda", 92),
            Student("bar","jackie",133),
            Student("jacoy","caroline", 124),
            Student("renquist","abbie",173),
            Student("jacks","tradd", 118),
            Student("jerry","tom",235),
            Student("lewis","franny", 44),
            Student("stoll","patty",62)
         ]
# odd number of students (15)
# median = 143
students_2 = \
         [
            Student("king","ashley", 49),
            Student("john","youngblood",143),
            Student("jacob","dylan", 205),
            Student("rentol","abbot",158),
            Student("nan","treme", 38),
            Student("polt","ted",225),
            Student("lenny","bob", 44),
            Student("stahl","pamela",452),
            Student("jordy","elizabeth",420),
            Student("kacoy","carol", 124),
            Student("henq","abe",183),
            Student("mack","tray", 118),
            Student("jernigan","tommy",225),
            Student("laws","brian", 44),
            Student("roll","marie",102)
         ]
# single student
# median = 197
students_3 = \
         [
            Student("jed","tennessee", 197)
         ]

#-------sorting array of 16 students
array_size = len(students_1)
# default sort
before_default_sort = StudentArrayUtilities.to_string(students_1, "Before "
                                                                "default "
                                                         "sort: ")
StudentArrayUtilities.array_sort(students_1, array_size)
after_default_sort = StudentArrayUtilities.to_string(students_1, "After "
                                                                 "default "
                                                                 "sort: ")
print(before_default_sort)
print(after_default_sort)


'''------------- RUN: before & after default sort
Before default sort: 
 ---------- 
    name: smith, freda
    total points: 95.
 ---------- 
    name: bauer, jackie
    total points: 123.
 ---------- 
    name: jacobs, caroline
    total points: 194.
 ---------- 
    name: renquist, abbie
    total points: 173.
 ---------- 
    name: jackson, trent
    total points: 108.
 ---------- 
    name: perry, tom
    total points: 225.
 ---------- 
    name: lewis, franny
    total points: 44.
 ---------- 
    name: stollings, pat
    total points: 552.
 ---------- 
    name: smote, freda
    total points: 92.
 ---------- 
    name: bar, jackie
    total points: 133.
 ---------- 
    name: jacoy, caroline
    total points: 124.
 ---------- 
    name: renquist, abbie
    total points: 173.
 ---------- 
    name: jacks, tradd
    total points: 118.
 ---------- 
    name: jerry, tom
    total points: 235.
 ---------- 
    name: lewis, franny
    total points: 44.
 ---------- 
    name: stoll, patty
    total points: 62.

After default sort: 
 ---------- 
    name: bar, jackie
    total points: 133.
 ---------- 
    name: bauer, jackie
    total points: 123.
 ---------- 
    name: jacks, tradd
    total points: 118.
 ---------- 
    name: jackson, trent
    total points: 108.
 ---------- 
    name: jacobs, caroline
    total points: 194.
 ---------- 
    name: jacoy, caroline
    total points: 124.
 ---------- 
    name: jerry, tom
    total points: 235.
 ---------- 
    name: lewis, franny
    total points: 44.
 ---------- 
    name: lewis, franny
    total points: 44.
 ---------- 
    name: perry, tom
    total points: 225.
 ---------- 
    name: renquist, abbie
    total points: 173.
 ---------- 
    name: renquist, abbie
    total points: 173.
 ---------- 
    name: smith, freda
    total points: 95.
 ---------- 
    name: smote, freda
    total points: 92.
 ---------- 
    name: stoll, patty
    total points: 62.
 ---------- 
    name: stollings, pat
    total points: 552.

'''

# sort key = first name
Student.set_sort_key(Student.SORT_BY_FIRST)
StudentArrayUtilities.array_sort(students_1, array_size)
after_fname_sort = StudentArrayUtilities.to_string(students_1, "After first "
                                                               "name sort: ")
print(after_fname_sort)

'''------------- RUN: after first name sort
After first name sort: 
 ---------- 
    name: renquist, abbie
    total points: 173.
 ---------- 
    name: renquist, abbie
    total points: 173.
 ---------- 
    name: jacobs, caroline
    total points: 194.
 ---------- 
    name: jacoy, caroline
    total points: 124.
 ---------- 
    name: lewis, franny
    total points: 44.
 ---------- 
    name: lewis, franny
    total points: 44.
 ---------- 
    name: smith, freda
    total points: 95.
 ---------- 
    name: smote, freda
    total points: 92.
 ---------- 
    name: bar, jackie
    total points: 133.
 ---------- 
    name: bauer, jackie
    total points: 123.
 ---------- 
    name: stollings, pat
    total points: 552.
 ---------- 
    name: stoll, patty
    total points: 62.
 ---------- 
    name: jerry, tom
    total points: 235.
 ---------- 
    name: perry, tom
    total points: 225.
 ---------- 
    name: jacks, tradd
    total points: 118.
 ---------- 
    name: jackson, trent
    total points: 108.
'''

# sort key = total points
Student.set_sort_key(Student.SORT_BY_POINTS)
StudentArrayUtilities.array_sort(students_1, array_size)
after_points_sort = StudentArrayUtilities.to_string(students_1, "After total "
                                                               "points sort: ")
print(after_points_sort)

'''------------- RUN: after total points sort
After total points sort: 
 ---------- 
    name: lewis, franny
    total points: 44.
 ---------- 
    name: lewis, franny
    total points: 44.
 ---------- 
    name: stoll, patty
    total points: 62.
 ---------- 
    name: smote, freda
    total points: 92.
 ---------- 
    name: smith, freda
    total points: 95.
 ---------- 
    name: jackson, trent
    total points: 108.
 ---------- 
    name: jacks, tradd
    total points: 118.
 ---------- 
    name: bauer, jackie
    total points: 123.
 ---------- 
    name: jacoy, caroline
    total points: 124.
 ---------- 
    name: bar, jackie
    total points: 133.
 ---------- 
    name: renquist, abbie
    total points: 173.
 ---------- 
    name: renquist, abbie
    total points: 173.
 ---------- 
    name: jacobs, caroline
    total points: 194.
 ---------- 
    name: perry, tom
    total points: 225.
 ---------- 
    name: jerry, tom
    total points: 235.
 ---------- 
    name: stollings, pat
    total points: 552.
'''

# sort key = first name
# get median
Student.set_sort_key(Student.SORT_BY_FIRST)
get_median = StudentArrayUtilities.get_median_destructive(students_1,array_size)
print('The median score for students_1 is: ' + str(get_median))

'''------------- RUN: after total points sort
The median score for students_1 is: 123.5
'''

# get sort_key
# should be 88 (first name)
current_key = Student.get_sort_key()
print('The current sort key is: ' + str(current_key))

'''------------- RUN: after destructice median
The current sort key is: 88
'''

# get median for odd list and single list
students_2_size = len(students_2)
get_median_2 = StudentArrayUtilities.get_median_destructive(students_2,
                                                          students_2_size)
print('The median score for students_2 (odd number of students) is: ' + str(
    get_median_2))

students_3_size = len(students_3)
get_median_3 = StudentArrayUtilities.get_median_destructive(students_3,
                                                          students_3_size)
print('The median score for students_3 (single student) is: ' + str(
    get_median_3))

'''------------- RUN: median for odd num of students and single student
The median score for students_2 (odd number of students) is: 143
The median score for students_3 (single student) is: 197
'''