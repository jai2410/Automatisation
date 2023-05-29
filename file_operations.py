from time import strftime

def write_time_in_file(file, name, message):
    try:
        if not file.closed:
            new_message = strftime("%m/%d/%Y %H:%M:%S") + " " + name + " : " + message + "\n"
            file.write(new_message)
            print(new_message)
        else:
            print("Error: The file is closed.")
    except Exception as e:
        print("Error: An error occurred while writing to the file.")
        print(e)
