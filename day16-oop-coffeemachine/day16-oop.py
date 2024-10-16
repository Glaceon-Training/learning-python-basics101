# from turtle import *
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkSeaGreen4")
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokedex No.", "Pokemon", "Type"]
table.add_rows(
    [
        ["#001", "Chespin", "Grass"],
        ["#002", "Quilladin", "Grass"],
        ["#003", "Chesnaught", "Grass - Fighting"],
        ["#004", "Fennekin", "Fire"],
        ["#005", "Braixen", "Fire"],
        ["#006", "Delphox", "Fire - Psychic"],
        ["#007", "Froakie", "Water"],
        ["#008", "Frogadier", "Water"],
        ["#009", "Greninja", "Water - Dark"],
        ["#010", "Pikachu", "Electric"],
        ["#011", "Ratata", "Normal"],
    ]
)

table.align["Pokemon"] = "l"
table.align["Type"] = "l"

print(table)
