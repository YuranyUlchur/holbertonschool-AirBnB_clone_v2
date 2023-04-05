#!/usr/bin/python3
import inspect
import io
import sys
import cmd
import shutil

"""
 Cleanup file storage
"""
import os
file_path = "file.json"
if not os.path.exists(file_path):
    try:
        from models.engine.file_storage import FileStorage
        file_path = FileStorage._FileStorage__file_path
    except:
        pass
if os.path.exists(file_path):
    os.remove(file_path)

"""
 Backup console file
"""
if os.path.exists("tmp_console_main.py"):
    shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("console.py", "tmp_console_main.py")


"""
 Updating console to remove "__main__"
"""
with open("tmp_console_main.py", "r") as file_i:
    console_lines = file_i.readlines()
    with open("console.py", "w") as file_o:
        in_main = False
        for line in console_lines:
            if "__main__" in line:
                in_main = True
            elif in_main:
                if "cmdloop" not in line:
                    file_o.write(line.lstrip("    ")) 
            else:
                file_o.write(line)

import console

"""
 Create console
"""
console_obj = "HBNBCommand"
for name, obj in inspect.getmembers(console):
    if inspect.isclass(obj) and issubclass(obj, cmd.Cmd):
        console_obj = obj

my_console = console_obj(stdout=io.StringIO(), stdin=io.StringIO())
my_console.use_rawinput = False

"""
 Exec command
"""
def exec_command(my_console, the_command, last_lines = 1):
    my_console.stdout = io.StringIO()
    real_stdout = sys.stdout
    sys.stdout = my_console.stdout
    my_console.onecmd(the_command)
    sys.stdout = real_stdout
    lines = my_console.stdout.getvalue().split("\n")
    return "\n".join(lines[(-1*(last_lines+1)):-1])

"""
 Objects creations
"""
state_id_1 = exec_command(my_console, "create State name=\"California\"")
if state_id_1 is None or state_id_1 == "":
    print("FAIL: Can't create State 1")
    
city_id_1 = exec_command(my_console, "create City state_id=\"{}\" name=\"Fremont\"".format(state_id_1))
if city_id_1 is None or city_id_1 == "":
    print("FAIL: Can't create City 1")

city_id_2 = exec_command(my_console, "create City state_id=\"{}\" name=\"Napa\"".format(state_id_1))
if city_id_2 is None or city_id_2 == "":
    print("FAIL: Can't create City 2")

state_id_2 = exec_command(my_console, "create State name=\"California2\"")
if state_id_2 is None or state_id_2 == "":
    print("FAIL: Can't create State 2")
    
city_id_3 = exec_command(my_console, "create City state_id=\"{}\" name=\"Sonoma\"".format(state_id_2))
if city_id_3 is None or city_id_3 == "":
    print("FAIL: Can't create City 3")


"""
 Tests
"""
from models import storage
from models.state import State

def wrapper_all_type(m_class):
    res = {}
    try:
        res = storage.all(m_class)
    except:
        res = {}
    if res is None or len(res.keys()) == 0:
        try:
            res = storage.all(m_class.__name__)
        except:
            res = {}
    return res


all_states = wrapper_all_type(State)
state_1 = all_states.get(state_id_1)
if state_1 is None:
    state_1 = all_states.get("State.{}".format(state_id_1))
if state_1 is not None:
    all_cities = state_1.cities
    if len(all_cities) != 2:
        print("FAIL: {} cities found instead of 2".format(len(all_cities)))

    city_ids_to_search = [city_id_1, city_id_2]
    for city in all_cities:
        if city.id in city_ids_to_search:
            city_ids_to_search.remove(city.id)

    if len(city_ids_to_search) > 0:
        print("FAIL: {} missing".format(city_ids_to_search))
else:
    print("FAIL: State 1 not found")
  

print("OK", end="")

shutil.copy("tmp_console_main.py", "console.py")