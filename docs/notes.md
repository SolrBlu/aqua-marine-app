### Think about putting main.py, update.py, watch.py, etc. scripts in app-root/scripts/ directory

can use 
 ```
# package.json
"scripts": {
    "dev": "concurrently \"npm run start-next\" \"python3 -u watch.py\""
}
    - affects all print() statments, all will be logged immediately to console
    - Current implementation

# [some_file].py
print("Some log message", flush=True)
    - allows for greater control, only log the messages to the console that need to be shown
 ```