import json
from actions import OpenVCS, EnterName, JoinVCS, StartVideo, StartAudio, WriteInChat
from vcs import BBB
from automated_person import AutomatedPerson

def main():
    # Initialize users with BBB
    users = {
        "1": BBB(AutomatedPerson("1")),
        "2": BBB(AutomatedPerson("2")),
        # add more users if needed
    }

    # Read actions from JSON file
    with open('actions.json') as f:
        actions_json = json.load(f)

    # Sort actions by timestamp
    actions_json.sort(key=lambda x: x["timestamp"])

    # Execute actions
    for action in actions_json:
        user = users[action["id"]]
        wait_time = action["timestamp"]

        action_obj = None
        if action["action"] == "open_bbb":
            action_obj = OpenVCS(user, wait_time)
        elif action["action"] == "enter_name":
            action_obj = EnterName(user, wait_time)
        elif action["action"] == "join_bbb":
            action_obj = JoinVCS(user, wait_time)
        elif action["action"] == "start_audio":
            action_obj = StartAudio(user, wait_time)
        elif action["action"] == "start_video":
            action_obj = StartVideo(user, wait_time)
        elif action["action"] == "write_in_chat":
            action_obj = WriteInChat(user, wait_time)
        else:
            print(f"Unknown action: {action['action']}")

        if action_obj is not None:
            action_obj.perform()

if __name__ == "__main__":
    main()
