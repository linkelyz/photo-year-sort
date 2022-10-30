# Photo Year Sort 📷 📁

A python project that sorts photos into folders based upon the year they were last modified. Created in collaboration with @marikit-yake. 

## Motivation: Why? 🤔

A friend needed over 30K photos on a hard drive sorted by year for better accessibility.

## Problems Solved: How? 🤷

Through a for loop and with the help of packages os and time, we can check the date a file was both created and modified. Since the created by date often only reflects when the file was downloaded or moved to the location it is in, we check the date of last modification to sort the files. The program then checks if a folder for that year of modification has been created and if not, creates a new folder and moves the file to that new location. 

## Future considerations 🔮

While currently the program has only sorted photos, it can sort any file for which a last date of modification is accessibile. Further inquires include the question of how to address duplicate files and preserve originals.