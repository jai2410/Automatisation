import sys
from action import ActionScript
from automated_person import AutomatedPerson
import json
import datetime

# Define all your users
users = {
    "1": AutomatedPerson("Phillip", 1, 2),
    "2": AutomatedPerson("Jane", 2, 2),
    # Add more users as required...
}

if __name__ == "__main__":
    # Expect the first argument to be the user id
    if len(sys.argv) < 2:
        print("Please provide a user id")
        exit(1)

    # Load the action script
    with open('config.json', 'r') as file:
        actions = json.load(file)
    
    # Time Syncronization
    next_minute = datetime.datetime.now().replace(second=0, microsecond=0) + datetime.timedelta(minutes=1)
    
    while datetime.datetime.now() < next_minute:
        pass  # busy wait, you can also use time.sleep here

    # Execute the actions for the specified user only
    for action in actions:
        user_id = action["id"]
        if user_id == sys.argv[1]:   
            user = users[user_id]
            script = ActionScript(user, action)
            script.perform()
