import time

class ActionScript:
    def __init__(self, automated_person, action):
        self.automated_person = automated_person
        self.action = action

    def perform(self):
        current_time = int(time.time() * 1000)
        wait_time = self.action["timestamp"] - current_time
        if wait_time > 0:
            self.automated_person.wait(wait_time)
        method = getattr(self.automated_person, self.action["action"])
        if "message" in self.action:
            method(self.action["message"])
        else:
            method()
