import os, zipfile

folders = ["Part1", "Part2", "Part3", "Part4"]

for folder in folders:
    folder = os.path.join("..", folder)
    os.chdir(folder)
    for file in os.listdir(folder):
        if zipfile.is_zipfile(file):
            with zipfile.ZipFile(file) as item:
                item.extractall()