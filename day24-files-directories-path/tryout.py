"""
This method is saving the Open() into a File variable. Then, we Read() that file and save it into Content var.
Only then, we can print the Content var. to read what's written in 'my_file.txt'.
But we have to always manually Close() method for our File var. so it won't take up your computer's memory space.

This Open() is a read-only mode in by default.
"""
# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

"""
Sometimes we want to write something more, appending new texts to our current file.
The 'With Open() as <alias>:' method can come in handy. Because after we open and use the file, it will
automatically close down afterward. Does not need to call the Close() method.

But again, this method is a read-only method by default. If we run the code, "io.UnsupportedOperation : not writeable"
warning will pop-up because we can not write anything to a read-only mode file.
"""
# with open("my_file.txt") as file:
#     file.write("New text.")

"""
In Open() method, there are various variables we can input to use how we want to open the file.
One of them is "mode='a'", in which 'a' stands for Append. As we do in our List, this mode will append new text
into our file.

If we want to overwrite the entire content of the file, use "mode = 'w'" as 'w' stands for Write.
"""
# with open("my_file.txt", mode='a') as file:
#     file.write("\nI am trying to append new text into this file.")

"""
If we use Open() where there file is not exist, it will create a new file for us with the name written
in between those quotation mark. With Write mode, you can write a NEW FILE with it.

This creating a new file is only work in Write mode while the file is not exist in the first place.
"""
# with open("new_file_1.txt", mode='w') as file:
#     file.write("\nI am trying to create a new text file by using different file name in Write mode.")

"""
>>>ABSOLUTE PATH:
This exercise is learning about File Directory and Path.
Previously, we create a "new_file_1.txt" in the same directory as "tryout.py" which in folder
"day24-files-directories-path". Then, we move the "new_file_1.txt" to a folder named "Desktop" in Desktop.

The challenge is to read that file in the new directory.

The way to do it is to check the file's properties, copy the file location. 
Notice that in the properties, the slashes are backslash. 
In order to read it in PyCharm, change the backslash into forward-slash, which in this case 
the new location is: "C:/Users/Ryan/Desktop/Desktop". We can leave out the "C:" since its the root folder.
Unless you save your file in another root drive like "D:", "E:", etc.
Then we add, "/new_file_1.txt" to tell Open() which file we want to open.

And voila!
"""
# with open("/Users/Ryan/Desktop/Desktop/new_file_1.txt") as file:
#     print(file.read())

"""
>>>RELATIVE PATH:
The challenge is to call the "new_file_1.txt" relative from the "tryout.py" file path as the script code.

The "tryout.py" file path:
/Users/Ryan/Desktop/Desktop/Github/Glaceon-Training/learning-python-basics101/day24-files-directories-path

The "new_file_1.txt" file path: 
/Users/Ryan/Desktop/Desktop


---Illustration:
         <Desktop 1><Desktop 2>
/Users/Ryan/Desktop/Desktop/Github/Glaceon-Training/learning-python-basics101/day24-files-directories-path
                      4       3           2                      1             <We are here: "tryout.py">
                      
I have a Desktop (1st desktop from left on the path, let's call it "Desktop 1"), 
and a folder called Desktop (2nd desktop from left on the path, let's call it "Desktop 2").
We want to open the "new_file_1.txt" which located in Desktop 2. Meanwhile, "tryout.py" is in "day24-..." folder.
In order to go to Desktop 2, we need to "go up" the folder 4 times. And to go up one folder, we use "../".

Voila!
"""
# with open("../../../../new_file_1.txt") as file:
#     print(file.read())

"""
RELATIVE PATH EXERCISE:

I move the "new_file_1.txt" to Github folder:
C:/Users/Ryan/Desktop/Desktop/Github

And now I want to open this file relative to "tryout.py" which in:
/Users/Ryan/Desktop/Desktop/Github/Glaceon-Training/learning-python-basics101/day24-files-directories-path

Let's use the "Desktop 2" as our Working Folder and call the "new_file_1.txt".

---Illustration:
         <Desktop 1><Desktop 2>
/Users/Ryan/Desktop/Desktop/Github/Glaceon-Training/learning-python-basics101/day24-files-directories-path
                      4       3           2                      1             <We are here: "tryout.py">

I will go up 4 folder and go down to Github folder to fetch the file.
"""
with open("../../../../Github/new_file_1.txt") as file:
    print(file.read())

"""
>>>RELATIVE PATH:
--QUIZ 1:
If the "new_file_1.txt" is in the same "day24-..." folder with "tryout.py". 
We can write the relative path as: "./new_file_1.txt", 
but since the "./" is optional we can just write the relative path as: "new_file_1.txt".

--QUIZ 2:
A "quiz.txt" has an absolute path: /Users/my_project/quiz.txt

We don't need to add "Macintosh HD" or "C:" before "/Users" since absolute path is always relative to root.
Which is the "Macintosh HD" or "C:".

--QUIZ 3:
A "quiz.txt" path is: /all_files/my_files/quiz_files/quiz.txt
A "miles_to_km.py" path is: /all_files/my_project/miles_to_km.py

To open "quiz.txt" relative to "miles_to_km.py", the Open() path is:
../my_files/quiz_files/quiz.txt

it is to go up one folder to "all_files" then go down the "my_files" and so on folders to get "quiz.txt".
"""