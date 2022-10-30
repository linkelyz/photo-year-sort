import time 
import os

def main():
    # the current working directory
    cwd = os.getcwd()
    # path to folder of files we want to sort
    path = cwd + "/pics/"
    print("Preparing files for sorting...")
    print()
    time.sleep(2)
    # for each file in the pics folder specified by the path to the folder
    for filename in os.listdir(path):
        time.sleep(1)
        # os.path.getmtime returns the number of seconds since 1970 showing the time of last modification
        # time.ctime takes the number of seconds and returns a string representing the time in a human readable format
        date_mod_string = time.ctime(os.path.getmtime(path + filename))
        # time.localtime takes the numbers of seconds and returns a struct_time object containing year, month, and day information
        date_mod_obj = time.localtime(os.path.getmtime(path + filename))
        # specify a directory to be created in a sorted folder for each year based on the year of last mod (date_mod_obj.tm_year)
        year_dir = cwd + "/sorted/" + str(date_mod_obj.tm_year) + "/"
        print(f"File name: {filename}, Year Modified: {date_mod_obj.tm_year}")
        # if there is not a folder for the year already existing in the sorted folder, create a new folder based on the year of last mod (date_mod_obj.tm_year)
        if not os.path.isdir(year_dir):
            os.mkdir(year_dir)
        # replace the current directory with a new directory to the year folder in the sorted folder 
        # in other words: move the file from the current folder in pics to the year folder in the sorted folder
        os.replace((path + filename), (year_dir + filename))

    time.sleep(2)
    print()
    print("Completed sorting successfully!")

if __name__ == "__main__":
    main()
