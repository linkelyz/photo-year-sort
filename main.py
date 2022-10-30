import time 
import os

def main():
    cwd = os.getcwd()
    path = cwd + "/pics/"
    print("Preparing files for sorting...")
    print()
    time.sleep(2)

    for filename in os.listdir(path):
        time.sleep(1)
        date_mod_string = time.ctime(os.path.getmtime(path + filename))
        date_mod_obj = time.localtime(os.path.getmtime(path + filename))
        year_dir = cwd + "/sorted/" + str(date_mod_obj.tm_year) + "/"
        print(f"File name: {filename}, Year Modified: {date_mod_obj.tm_year}")
        if not os.path.isdir(year_dir):
            os.mkdir(year_dir)
        os.replace((path + filename), (year_dir + filename))

    time.sleep(2)
    print()
    print("Completed sorting successfully!")

if __name__ == "__main__":
    main()
