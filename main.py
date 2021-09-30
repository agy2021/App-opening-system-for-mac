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
        if "code" in app or "ide" in app:
            os.system('open -a "visual studio code"')
            os.system("clear")
        elif "java" in app:
            os.system('open -a "intellij idea ce"')
            os.system("clear")
        elif "chrome" in app:
            os.system('open -a "google chrome"')
            os.system("clear")
        elif "saf" in app:
            os.system('open -a safari')
            os.system("clear")
        elif "repl" in app:
            os.system('open -a "replit.com"')
            os.system("clear")
        elif "jlearn" in app:
            os.system('open -a "java learning | mike dane"')
            os.system("clear")
        elif "nt" in app:
            os.system('open -a "nitro type"')
            os.system("clear")
        elif "settings" in app:
            os.system('open -a "system preferences"')
            os.system("clear")

        os.system('open -a "' + app + '"')
        os.system("clear")