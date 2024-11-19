import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

"""
>>>Label:
Label are available within tkinter module in Label() class.
The usage is shown below, after every label declaration, pack the variable to show in window,
or it won't show at all.
The pack method, pass arguments (*args) and keyword arguments (**kwargs).

A sample of keyword arguments have been learned in previous lessons:
def my_function(a, b, c):
    Do this with a
    Then do this with b
    Finally do this with c

my_function(c=3, a=1, b=2), we can use arguments without order with keyword arguments as long as we got
the keyword in front (the a, b, c). The drawback of this method is we have to call the arguments everytime
we call the function.
Python have Arguments with Default Values method, by putting the integer in the function declaration.
So it goes:
def my_function(a=1, b=2, c=3):
    Do this with a
    Then do this with b
    Finally do this with c

Then we can just call the function like: my_function(), because the values are in default within the declaration.
If we want to change one of the arguments, we can do: my_function(b=5), then the value of b will be equal to 5,
instead of the default value of 2.

---Key Takeaway:
Default arguments are preset in function. Moreover, we can change the default value to the one
we want when we call the function.

>>>Button:
Button is a class in Tkinter. It creates button in your GUI.
Button has optional keyword arguments, we can customize the text within the button.
In button, there is a "command" kwarg, in which we can call the name of a function. When we click the button, 
it will command the button to run the function.
"""
# my_label = tkinter.Label(text="Mining Outlook", font=("Courier", 18))
# my_label2 = tkinter.Label(text="2024 Edition", font=("Courier", 12, "italic"))
# my_label.pack()
# my_label2.pack()
my_label3 = tkinter.Label(text="New Text", font=("Arial", 18, "normal"))
my_label3.pack()

input = tkinter.Entry(width=20)
input.pack()


def button_clicked():
    get_it = input.get()
    my_label3.config(text=get_it)


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

"""
A loop to make the window to stay open, similar to turtle.mainloop().
Codes are written above between window variable declaration and mainloop.
"""
window.mainloop()

# def foo(a, b=4, c=6):
#     print((a, b, c))
#     print(a, b, c)
#
# def fos(*args):
#     print(args)
#
# foo(a=1)
# fos(1, 2, 3, 4)

"""
>>> *args: Taking any number of arguments for a function.
def add(*args):
    for n in args:
        print(n)

Using *args can make our function take any number of arguments, for this example is for our addition function.
"""
"""
>>>About *args:
*args in function definitions in Python is used to pass a variable number of arguments to a function.
The syntax is to use the symbol * to take in a variable number of arguments; 
by convention, it is often used with the word args.

A challenge to add all arguments with *args. We can use 2 methods:
1. For loop:
    my_sum = 0
    for i in args:
        my_sum += i
2. sum(args)

Printing the args of function will return in tuple that represents the inputs when function is called.
So position matters, if we call the index of the args, it will return the value by its positional index.
"""
# def add(*args):
#     my_sum = 0
#     for n in args:
#         print(n)
#     for i in args:
#         my_sum += i
#     print(type(args))
#     print(args)
#     print(args[0])
#     print(args[-2])
#     print(my_sum)
#     print(sum(args))
#
# add(3, 5, 6, 7, 4, 1, 3)

"""
>>>About **kwargs:
*args collects additional positional arguments as a tuple, 
while **kwargs collects additional keyword arguments as a dictionary.

**kwargs type is dictionary. We can use kwargs' keyword arguments like how dictionary does.
A sample below.
"""
# def calculate(n, **kwargs): # Having a 'n' argument to do with kwargs variables.
#     print(type(kwargs))
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     n += kwargs["add"]
#     print(n)
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=3, multiply=5)

"""
>>>Using **kwargs in Class' Object:
--We can create many optional keyword argument of object we wanted to create.

Creating object in the sample below is like calling a dictionary value.
We specify the keyword and value on the kwargs, then we can call it with "kw['make']" for self.make, or
"kw['model']" for self.model.
Unfortunately, this square-bracket method will get error if we did not specify one of the attribute.
Using kw.get() will return NONE if there are no kwarg attribute specified, did not return error.

Furthermore, we can add as many optional attribute as we want because we use .get method.
"""
# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.seat = kw.get("seat")
#
# my_car = Car(make="Toyota", model="Supra", color="purple", seat=2)
# print(my_car.color)
# print(my_car.seat)

"""QUIZ #1"""
# def bar(spam, eggs, toast="yes please!", ham=0):
#     print(spam, eggs, toast, ham)
#
# bar(1, 2)

"""QUIZ #2"""
# def bar(spam, eggs, toast="yes please!", ham=0):
#     print(spam, eggs, toast, ham)
#
# bar(toast="nah", spam=4, eggs=2)

"""QUIZ #3"""
# def test(*args):
#     print(args)
#
# test(1, 2, 3, 5)

"""QUIZ #4"""
# def test(*args):
#     print(args)
#
# test(1, 2, 3, 5)

"""QUIZ #5"""
# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
#
# all_aboard(4, 7, 3, 0, x=10, y=64)
