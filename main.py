from time import strftime
from action import action_script
from automated_person import AutomatedPerson

if __name__ == "__main__":
    jan = AutomatedPerson("Phillip", 1, 1)
    new_script = action_script(jan)
    new_script.perform()