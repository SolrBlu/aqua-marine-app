import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

print('Started watching aqua-language/src/ for changes...')

parser_dir = 'aqua-language/parser/'
change_count = 0

def format_change_count(num):
    if 10 <= num % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(num % 10, "th")
    return f"{num}{suffix}"

def grab_aqua_files(event): # Execute all Python files in the parser directory
    src_path = event['src_path'] if isinstance(event, dict) else event.src_path
    aqua_file_name = os.path.basename(src_path)
    
    # Check if the file is an Aqua file
    if aqua_file_name.endswith('.aqua'):
        base_file_name = aqua_file_name[:-5] # Remove '.aqua'
        nextjs_file_path = f"nextjs-app/src/app/{base_file_name}/page.js" if not base_file_name == "index" else "nextjs-app/src/app/page.js"
        
        for filename in os.listdir(parser_dir):
            if filename.endswith('.py') and filename.startswith('aqua_to_'): # strictly checking for "aqua_to_[...].py" files
                file_path = os.path.join(parser_dir, filename)
                print(f"Executing: {os.path.basename(file_path)} with: {aqua_file_name}")
                subprocess.run(['python3', file_path, src_path, nextjs_file_path, base_file_name])

class AquaChangeHandler(FileSystemEventHandler):
    def on_modified(self, event): # event: { event_type: 'modified', is_directory: False, src_path: '/Users/elijahmusaally/Desktop/aqua-marine-app/aqua-language/pages/HelloWorld.aqua' }
        global change_count
        if event.src_path.endswith('.aqua'):
            change_count += 1
            print(f"\n({format_change_count(change_count)}) Change detected...")
            print("Parsing Aqua files...")
            grab_aqua_files(event)

if change_count == 0:
    grab_aqua_files({
        "event_type": "initial",
        "src_path": "aqua-language/src/pages/index.aqua",
        "is_directory": False
    }) # add hardcoded event to func with index.aqua / app.aqua being the entry point (src_path)

if __name__ == "__main__":
    path_to_watch = 'aqua-language/src'
    event_handler = AquaChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
