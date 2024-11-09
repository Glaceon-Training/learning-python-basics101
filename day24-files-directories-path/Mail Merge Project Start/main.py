"""
Exercise about files, directories and paths:
Creating automated invitation letter from a number of invited guest names.
"""
PLACEHOLDER = "[name]"

"""
1. Created list of guests in "names" list by utilizing readlines() method.
"""
with open("Input/Names/invited_names.txt") as guests:
    names = guests.readlines()

"""
2. Open and read letter from template of "starting_letter.txt".
3. For name in "names" list, strip trailing spaces caused by "<backslash>n".
4. And in the same For Loop, replace placeholder "[name]" in the letter template with the every name in "names" list,
   which has been saved in "new_name" variable after stripping trailing space.
5. In the same For Loop, create the final letter where "[name]" placeholder has been replaced. The number of letter
   written is the same amount as the number of guests in "names" list.
"""
with open("Input/Letters/starting_letter.txt") as letter:
    new_letter = letter.read()
    for name in names:
        new_name = name.strip()
        invitation_letter = new_letter.replace(PLACEHOLDER, new_name)
        with open(f"Output/ReadyToSend/Letter_for_{new_name}", mode='w') as final_letter:
            final_letter.write(invitation_letter)
