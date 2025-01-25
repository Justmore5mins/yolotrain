text = []

with open("requirements.txt") as file:
    for item in file.readlines():
        text.append(item.split(">=")[0]+"\n")

with open("requirements.txt","w") as file:
    file.writelines(text)