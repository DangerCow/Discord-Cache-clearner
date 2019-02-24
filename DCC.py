import os

print(os.path.dirname(os.path.realpath(__file__)))

installed = input("have you installed discord to a custom folder? y/n: ")


if installed == "y":
    dir = input("directory: ")
elif installed == "n":
    dir = os.path.dirname(os.path.realpath(__file__))
    start = dir.split("\\")[0] + "\\" + dir.split("\\")[1] + "\\" + dir.split("\\")[2]
    dir = start + "\AppData\Roaming\Discord\Cache"

i = 0
size = 0

for the_file in os.listdir(dir):
    file_path = os.path.join(dir, the_file)
    try:
        tmpsize = os.path.getsize(file_path)
        if os.path.isfile(file_path):
            os.unlink(file_path)
            print("file deleted " + the_file)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        size += tmpsize
        i += 1
    except Exception as e:
        print("failed to delete file " + the_file)
        

input("deleted " + str(i) + " files and cleared " + "{:,}".format(size) + " bytes of storage")