import time
from shelve_example import *

while True:
    time.sleep(60)
    for user in db:
        user["balance"] += user["num_of_apps"] * 25
