import os

path = input("Enter folder path to directory: ")
word = input("Word/sentence that are to be removed/replaced: ")
new = input("Word/Sentence that is to be put in: ")

try:
    for dirpath, _, files in os.walk(path):
        for filename in files:
            if word in filename:
                new_filename = filename.replace(word, new)
                os.rename(os.path.join(dirpath, filename), os.path.join(dirpath, new_filename))
                print(f"Renamed '{filename}' to '{new_filename}'")
            else:
                print(f"{filename} does not contain the word.")
except Exception as e:
    print("Error: ", e)

input()
        
                
        
