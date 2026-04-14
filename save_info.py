import os

def setup():
    if not os.path.isdir("storage"):
        os.mkdir("storage")
    if not os.path.isdir("current_files"):
        os.mkdir("current_files")
    

def save_images(count):
    dir_name = f"current_files'{count+1}'"
    os.replace("/front.png", f"storage/{dir_name}_front.png")
    os.replace("current_files/rear.png", f"storage/{dir_name}_rear.png")

def save_spreadsheet(distillery,reference,boxed,count):
    with open('catalogue.csv','a') as file:
        file.write(f"{count+1},{distillery},{reference},{boxed}\n")

def save_info(data):
    count = len([f for f in (os.listdir('storage')) if f.endswith('_front.png')])
    distillery = data[0]
    reference = data[1]
    boxed = data[2]
    save_images(count)
    save_spreadsheet(distillery,reference,boxed,count)


