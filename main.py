import sys
from action import ActionScript
from automated_person import AutomatedPerson
import json

# Define all your users
users = {
    "1": AutomatedPerson("Phillip", 1, 2),
    "2": AutomatedPerson("Jane", 2, 2),
    # Add more users as required...
}

if __name__ == "__main__":
    # Load the action script
    with open('config.json', 'r') as file:
        actions = json.load(file)

    # Execute the actions
    for action in actions:
        user_id = action["id"]
        user = users[user_id]
        script = ActionScript(user, action)
        script.perform()

