import os

missing = []
for i in range(0, 408):
    file_number = str(1280+i)
    file_name = "/Users/theodoreshih/Desktop/throax/a_vm" + file_number + ".png"
    if os.path.isfile(file_name):
        continue
    else:
        missing.append(file_number)

print missing
