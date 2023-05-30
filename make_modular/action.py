from abc import ABC, abstractmethod
from vcs import BaseVCS

class Action(ABC):
    def __init__(self, user: BaseVCS, wait_time: int):
        self.user = user
        self.wait_time = wait_time

    @abstractmethod
    def perform(self):
        pass

class OpenVCS(Action):
    def perform(self):
        self.user.open_vcs()
        self.user.wait(self.wait_time)

class EnterName(Action):
    def perform(self):
        self.user.enter_name()
        self.user.wait(self.wait_time)

class JoinVCS(Action):
    def perform(self):
        self.user.join_vcs()
        self.user.wait(self.wait_time)

class StartVideo(Action):
    def perform(self):
        self.user.start_video()
        self.user.wait(self.wait_time)

class StartAudio(Action):
    def perform(self):
        self.user.start_audio()
        self.user.wait(self.wait_time)

class WriteInChat(Action):
    def perform(self):
        self.user.write_in_chat()
        self.user.wait(self.wait_time)
