from time import strftime

def write_time_in_file(file, name, message):
    new_message = strftime("%m/%d/%Y %H:%M:%S") + " " + name + " : " + message + "\n"
    file.write(new_message)
    print(new_message)