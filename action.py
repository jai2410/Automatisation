# Seperate python file of defining user actions
from automated_person import AutomatedPerson
from time import strftime
class action_script:

	def __init__(self, automated_person):
		self.automated_person = automated_person

	def perform(self):
		#start browser and get ready fro joining
		self.automated_person.wait(10000 * self.automated_person.number)
		self.automated_person.open_bbb()
		self.automated_person.enter_name()
		self.automated_person.wait(10000 * (self.automated_person.max_number - self.automated_person.number) )

		#join bbb
		self.automated_person.wait(20000 * self.automated_person.number)
		self.automated_person.join_bbb()
		self.automated_person.wait(20000 * (self.automated_person.max_number - self.automated_person.number))

		#write in chat
		self.automated_person.wait(15000 * self.automated_person.number)
		self.automated_person.write_in_chat("Hey")
		self.automated_person.write_in_chat("Der Sinn des Lebens ist 42.")
		self.automated_person.wait(15000 * (self.automated_person.max_number -self.automated_person.number))

		#start and stop of audio and video with 2 minutes of streaming
		self.automated_person.wait(130000 * self.automated_person.number)
		self.automated_person.start_audio()
		self.automated_person.start_video()
		self.automated_person.wait(120000) #wait 2 minutes
		self.automated_person.stop_audio()
		self.automated_person.stop_video()
		self.automated_person.wait(130000 * (self.automated_person.max_number - self.automated_person.number))

		#screen sharing
		self.automated_person.wait(25000 * self.automated_person.number)
		self.automated_person.start_screen_sharing()
		
		self.automated_person.wait(11600)
		self.automated_person.stop_screen_sharing()
		self.automated_person.wait(10000)
		self.automated_person.wait(25000 * (self.automated_person.max_number - self.automated_person.number))
		#shutdown window
		self.automated_person.wait(5000 * self.automated_person.number)
		self.automated_person.close_window()
		pass
