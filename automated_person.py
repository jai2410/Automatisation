from botcity.core import DesktopBot
from time import strftime
from file_operations import write_time_in_file

class AutomatedPerson(DesktopBot):
    
    def __init__(self, name : str, number : int, max_number = 3):
        super().__init__()
        self.name = name
        self.file = open("timefile.txt", "a")
        #set the number to one lower (first person dont have to wait)
        self.number = number - 1
        self.max_number = max_number - 1
        self.file.write("\n-------------------------------------------------------------\n")
        self.__add_all_images()

    def __del__(self):
        if not self.file.closed:
            self.file.close()

    def write_time_in_file(self, message):
        write_time_in_file(self.file, self.name, message)
    
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
        images = ["name_entering_field", "join_meeting_button", "join_meeting_button2",
                  "join_meeting_button3", "join_with_micro_button", "join_with_micro_button2",
                  "confirm_micro_working_button", "change_audio_settings", "set_audio_to_cable_output",
                  "start_audio_button", "stop_audio_button", "start_video_button", "stop_video_button",
                  "stop_video_button2", "change_video_settings", "set_video_to_obs_camera",
                  "start_access", "start_screen_sharing", "stop_screen_sharing", "options_button",
                  "become_presenter", "set_screen_setting", "set_screen", "allow_sharing",
                  "comment_entering_field", "comment_entering_field2"]

        for image in images:
            self.add_image(image, f"images/{image}.png")
        