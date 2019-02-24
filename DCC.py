import os

print(os.path.dirname(os.path.realpath(__file__)))

installed = input("have you installed discord to a custom folder? y/n: ")

if installed == "y":
    dir = input("directory: ")
elif installed == "n":
    dir = os.path.dirname(os.path.realpath(__file__))
    start = dir.split("\\")[0] + "\\" + dir.split("\\")[1] + "\\" + dir.split("\\")[2]
    dir = start + "\AppData\Roaming\Discord\Cache"

for the_file in os.listdir(dir):
    file_path = os.path.join(dir, the_file)
    try:
        if os.path.isfile(file_path):
            print("file deleted " + file_path)
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)
