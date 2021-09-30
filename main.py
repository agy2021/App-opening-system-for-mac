import os

while True:
    app = input("Enter app name: ")
    app.lower()
    
    if app == "clear":
        os.system("clear")
    elif app == "exit":
        os.system("clear")
        exit()
    else:
        os.system('open -a "' + app + '"')
        os.system("clear")
