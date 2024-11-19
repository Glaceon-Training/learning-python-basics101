import random
import pandas

"""
List Comprehension Formula:
1. Let's start from the beginning, we learn the basic of creating a list.
"""
# a = [1, 2, 3]
# b = []
# for n in a:
#     new_num = n + 1
#     b.append(new_num)
# print(b)
"""
On the code above, we created 'b' list from empty. Made a For Loop for each item in 'a' list.
We wanted to make a new list where the items are the 'n + 1' from 'a' list.
Therefore, the result will be [2, 3, 4].

We can shorten the line of codes with list comprehension.
"""
"""
Formula:
new_list = [new_item FOR n IN list]

* list = 'a' list
* n = every item in 'a' list.
* new_item = formula to create new list, which is the 'n + 1'.

so the code should be:
new_list = [n + 1 FOR n IN a]

Let's make n + 2.
"""
# c = [n + 2 for n in a]
# print(c)

"""
Now, let's make 'n * 2' from a 'range(1, 5)'.
Range(1, 5) = [1, 2, 3, 4]. Whereas, Range(5) = [0, 1, 2, 3, 4].
"""
# d = [n * 2 for n in range(1, 5)]
# print(d)
"""Therefore, n * 2 in range(1, 5) = [2, 4, 6, 8]."""

"""
Conditional list comprehension formula:
new_list = [new_item FOR n IN list IF test]

* new_item = formula of new item
* n = every item in list
* list = the list referenced
* test = condition to be passed

The 'new_item' will only be generated IF the 'test' passed. Then, the 'new_item' formula will proceed
for every 'n' in 'list'.
"""
"""
Let's make list with only names that has character no more than 5.
The final result will be: ["Alex", "Beth", "Dave"]
"""
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_name = [name for name in names if len(name) < 5]
# print(new_name)
"""
The IF part will act as a conditional term for the For Loop going through.
IF the len(name) < 5, add the 'name' item from 'names' list to 'new_name' list. 
"""
"""
Let's create a new list which only take name with >5 characters, and make every name Upper Case.
"""
# new_name_2 = [name.upper() for name in names if len(name) > 5]
# print(new_name_2)


"""
1) Dictionary comprehension formula from an existing LIST:
new_dict = {new_key: new_item FOR item IN list}

2) Dictionary comprehension formula from an existing DICTIONARY:
new_dict = {new_key: new_value FOR (key, value) IN dict.items()}

3) Dictionary comprehension also can add CONDITION:
new_dict = {new_key: new_value FOR (key, value) IN dict.items() IF test}
"""
"""
Let's make a new dictionary of student score, the score is generated using random module,
that will look like (1):

student_score = {
                  "Alex": 80,
                  "Beth":67,
                  "Caroline":90,
}
"""
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_score = {student: random.randint(1, 100) for student in names}
# print(student_score)

"""
Sample: {'Alex': 73, 'Beth': 89, 'Caroline': 67, 'Dave': 91, 'Eleanor': 17, 'Freddie': 80}

Let's try make a dictionary from an existing dictionary (the (3)). This dictionary will get passed student
who have scored >60, the dictionary will look like this:

passed_student = {
                   "Alex": 73,
                   "Beth": 89,
                   "Caroline": 67,
}
"""
# passed_student = {student: score for (student, score) in student_score.items() if score > 60}
# print(passed_student)
"""
Result:
{'Alex': 29, 'Beth': 64, 'Caroline': 100, 'Dave': 78, 'Eleanor': 52, 'Freddie': 44}
{'Beth': 64, 'Caroline': 100, 'Dave': 78}
"""

# weather_c = {
#     "Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24
# }
# weather_f = {
#     day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()
# }
# print(weather_f)

"""
Loop through pandas:
FOR (key, value) IN dataframe.items():
    print(key) OR
    print(value)
"""
"""Dictionary to make into pandas dataframe"""
student_score = {
    "student": ["Angela", "Beth", "Caroline"],
    "score": [90, 70, 80],
}
"""Create pandas dataframe"""
student_df = pandas.DataFrame(student_score)
# print(student_df)
"""Loop through items in student dataframe:"""
"""This part only print column title"""
# for (key, value) in student_df.items():
#     print(key)
"""This part print value of columns"""
# for (key, value) in student_df.items():
#     print(value)

"""
Loop through pandas iterrows:
FOR (index, value) IN dataframe.iterrows():
    print(index) OR
    print(value)
"""
"""This part returns row indices"""
# for (index, value) in student_df.iterrows():
#     print(index)
"""This part returns values by rows, not columns"""
# for (index, value) in student_df.iterrows():
#     print(value)
"""This part returns only values of student column"""
# for (index, value) in student_df.iterrows():
#     print(value.student)
"""This part returns only values of student score"""
# for (index, value) in student_df.iterrows():
#     print(value.score)
"""Give condition to student we are looking for, then print the student's score"""
for (index, value) in student_df.iterrows():
    if value.student == "Angela":
        print(value.score)