from abc import ABC, abstractmethod
from automated_person import AutomatedPerson

class BaseVCS(ABC):
    def __init__(self, automated_person: AutomatedPerson):
        self.user = automated_person

    @abstractmethod
    def open_vcs(self):
        pass

    @abstractmethod
    def enter_name(self):
        pass

    @abstractmethod
    def join_vcs(self):
        pass

    @abstractmethod
    def start_video(self):
        pass

    @abstractmethod
    def start_audio(self):
        pass

    @abstractmethod
    def write_in_chat(self, message: str):
        pass

    # Define more methods for common actions...

class BBB(BaseVCS):
    def open_vcs(self):
        self.user.open_bbb()

    def enter_name(self):
        self.user.enter_name()

    def join_vcs(self):
        self.user.join_bbb()

    def start_video(self):
        self.user.start_video()

    def start_audio(self):
        self.user.start_audio()

    def write_in_chat(self, message: str):
        self.user.write_in_chat(message)

    # Implement more methods for BBB specific actions...
class VCS:
    def get_all_images(self):
        pass


class BBB(VCS):
    def get_all_images(self):
        return ["bbb_name_entering_field", "bbb_join_meeting_button", "bbb_join_meeting_button2",
                "bbb_join_meeting_button3", ...]  # Include all your BBB specific images here


class Zoom(VCS):
    def get_all_images(self):
        return ["zoom_name_entering_field", "zoom_join_meeting_button", "zoom_join_meeting_button2",
                "zoom_join_meeting_button3", ...]  # Include all your Zoom specific images here
