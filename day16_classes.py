from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")

# # MOVEMENT
# timmy.fd(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()

table.add_column("Name", ["Shepard", "Garrus", "Tali", "Liara", "Wrex", "Thane"])
table.add_column("Specie", ["Human", "Turian", "Quarian", "Asari", "Krogan", "Drell"])
table.add_column("Job", ["Commander", "C-Sec Agent", "Engineer", "Scientist", "Mercenary", "Assassin"])
table.align = "l"
print(table)