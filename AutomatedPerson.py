from botcity.core import DesktopBot
from time import strftime

class AutomatedPerson(DesktopBot):
    
    def __init__(self, name : str, number : int, max_number = 3 ):
        super().__init__()
        self.name = name
        self.__add_all_images()
        self.file = open("timefile.txt", "a")
        #set the number to one lower (first person dont have to wait)
        self.number = number - 1
        self.max_number = max_number - 1
        self.file.write("\n-------------------------------------------------------------\n")

    def __del__(self):
        self.file.close()
    
    def action(self):
        #start browser and get ready fro joining
        self.wait(10000 * self.number)
        self.open_bbb()
        self.enter_name()
        self.wait(10000 * (self.max_number - self.number) )

        #join bbb
        self.wait(20000 * self.number)
        self.join_bbb()
        self.wait(20000 * (self.max_number - self.number))
        
        #write in chat
        self.wait(15000 * self.number)
        self.write_in_chat("Hey")
        self.write_in_chat("Der Sinn des Lebens ist 42.")
        self.wait(15000 * (self.max_number -self.number))
        
        #start and stop of audio and video with 2 minutes of streaming
        self.wait(130000 * self.number)
        self.start_audio()
        self.start_video()
        self.wait(120000) #wait 2 minutes
        self.stop_audio()
        self.stop_video()
        self.wait(130000 * (self.max_number - self.number))
        
        #screen sharing
        self.wait(25000 * self.number)
        self.start_screen_sharing()
        self.wait(11600)
        self.stop_screen_sharing()
        self.wait(10000)
        self.wait(25000 * (self.max_number - self.number))

        #shutdown window
        self.wait(5000 * self.number)
        self.close_window()
    
    def write_time_in_file(self, message : str):
        new_message = strftime("%m/%d/%Y %H:%M:%S") + " " + self.name + " : " + message + "\n"
        self.file.write(new_message)
        print(new_message)

    def open_bbb(self):
        """waits 3 seconds after starting"""
        self.browse("https://bbb1.th-brandenburg.de/b/jay-lft-64p-myb")
        self.write_time_in_file("Start browser and open BBB URL")
        self.wait(3000)

    def enter_name(self):
        """waits 3 x 100 ms in this method + namelength x 100 ms"""
        done = False
        #click on input field
        while not done:
            try:
                self.click_on("name_entering_field")
                done = True
            except Exception as e:
                print(e)
        self.write_time_in_file("Click on namefield")
        self.wait(100)

        #delete all chars from input
        self.control_a(wait=100)
        self.backspace(wait=100)

        #type in name
        self.type_keys_with_interval(100, self.name)
        self.write_time_in_file("Write name into namefield")
        self.wait(100)

    def join_bbb(self):
        """waits 3 x 3 seconds + 100 ms"""
        done = False
        #click on join button
        while not done:
            try:
                self.click_on("join_meeting_button")
                done = True
            except Exception as e:
                try:
                    self.click_on("join_meeting_button2")
                    done = True
                except Exception as e:
                    try:
                        self.click_on("join_meeting_button3")
                        done = True
                    except Exception as e:
                        print(e)
        self.write_time_in_file("Click on join button")
        self.wait(3000)

        done = False

        #click on join with micro button
        while not done:
            try:
                self.click_on("join_with_micro_button")
                done = True
            except Exception as e:
                try:
                    self.click_on("join_with_micro_button2")
                    done = True
                except Exception as e:
                    print(e)
        self.write_time_in_file("Click on join with mic")
        self.wait(3000)

        done = False
        #click on confirmation for working micro button
        while not done:
            try:
                self.click_on("confirm_micro_working_button")
                done = True
            except Exception as e:
                print(e)
        self.write_time_in_file("Click on confirm working audio")
        self.wait(3000)

        self.__change_audio_settings()
    

    def __change_audio_settings(self):
        """waits 2 x 100 ms"""
        done = False
        #click on change audio settings
        while not done:
            try:
                self.click_on("change_audio_settings")
                done = True
            except Exception as e:
                print(e)
        self.wait(100)
        self.click_on("set_audio_to_cable_output")
        self.wait(100)

    def write_in_chat(self, message : str):
        try:
            self.click_on("comment_entering_field")
        except:
            self.click_on("comment_entering_field2")
        

        self.wait(100)
        self.write_time_in_file("Start Write in Chat")
        self.type_keys_with_interval(100, message)
        self.enter()
        self.write_time_in_file(f'Send "{message}" in Chat')
        self.wait(100)

    def start_audio(self):
        done = False
        while not done:
            try:
                self.click_on("start_audio_button")
                done = True
            except Exception as e:
                print(e)
        self.write_time_in_file("Start audio")
        

    def stop_audio(self):
        done = False
        while not done:
            try:
                self.click_on("stop_audio_button")
                done = True
            except Exception as e:
                print(e)
        
        self.write_time_in_file("Stop audio")

    def start_video(self):
        """waits 3 s + 3 x 3 s"""
        self.click_on("start_video_button")
        self.write_time_in_file("Press start Video")
        self.wait(3000)
        done = False
        while not done:
            try:
                self.click_on("change_video_settings")
                done = True
            except Exception as e:
                print(e)
        self.wait(1000)
        self.click_on("set_video_to_obs_camera")
        self.wait(1000)
        self.click_on("start_access")
        self.write_time_in_file("Start Video")
        self.wait(1000)

    def stop_video(self):
        done = False
        while not done:
            try:
                self.click_on("stop_video_button")
                done = True
            except Exception as e:
                print(e)
        self.write_time_in_file("Stop video")
    
    def start_screen_sharing(self):
        try:
            self.click_on("options_button")
            self.wait(100)
            self.click_on("become_presenter")
            self.wait(1000)
        except:
            self.click_on("start_screen_sharing")

        try:
            self.click_on("start_screen_sharing")
        except:
            pass
                
        self.write_time_in_file("Press start screen sharing")
        self.wait(3000)
        self.click_on("set_screen_setting")
        self.wait(100)
        self.click_on("set_screen")
        self.wait(100)
        self.click_on("allow_sharing")
        self.write_time_in_file("Start screen sharing")
        self.wait(100)

    def stop_screen_sharing(self):
        try:
            self.click_on("stop_screen_sharing")
            self.write_time_in_file("Stop screen sharing")
        except:
            self.write_time_in_file("Forced stop screen sharing (stolen presenter rights)")

    def close_window(self):
        self.alt_f4()
        self.write_time_in_file("Shutdown firefox window")

    def __add_all_images(self):
        self.add_image("name_entering_field", "images/name_entering_field_mac.png")
        self.add_image("join_meeting_button", "images/join_meeting_button.png")
        self.add_image("join_meeting_button2", "images/join_meeting_button2.png")
        self.add_image("join_meeting_button3", "images/join_meeting_button3.png")
        self.add_image("join_with_micro_button", "images/join_with_micro_button.png")
        self.add_image("join_with_micro_button2", "images/join_with_micro_button2.png")
        self.add_image("confirm_micro_working_button", "images/confirm_micro_working_button.png")
        self.add_image("change_audio_settings", "images/change_audio_settings.png")
        self.add_image("set_audio_to_cable_output", "images/set_audio_to_cable_output.png")
        self.add_image("start_audio_button", "images/start_audio_button.png")
        self.add_image("stop_audio_button", "images/stop_audio_button.png")

        self.add_image("start_video_button", "images/start_video_button.png")
        self.add_image("stop_video_button", "images/stop_video_button.png")
        self.add_image("stop_video_button2", "images/stop_video_button2.png")
        self.add_image("change_video_settings", "images/change_video_settings.png")
        self.add_image("set_video_to_obs_camera", "images/set_video_to_obs_camera.png")
        self.add_image("start_access", "images/start_access.png")

        self.add_image("start_screen_sharing", "images/start_screen_sharing.png")
        self.add_image("stop_screen_sharing", "images/stop_screen_sharing.png")
        self.add_image("options_button", "images/options_button.png")
        self.add_image("become_presenter", "images/become_presenter.png")
        self.add_image("set_screen_setting", "images/set_screen_setting.png")
        self.add_image("set_screen", "images/set_screen.png")
        self.add_image("allow_sharing", "images/allow_sharing.png")

        self.add_image("comment_entering_field", "images/comment_entering_field.png")
        self.add_image("comment_entering_field2", "images/comment_entering_field2.png")
        
if __name__ == "__main__":
    jan = AutomatedPerson("Phillip", 1, 1)
    jan.action()

