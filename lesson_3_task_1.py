import os
from user import User

print("Current working directory:", os.getcwd())

my_user = User("Илья", "Романов")

my_user.print_first_name()
my_user.print_last_name()
my_user.print_full_name()
