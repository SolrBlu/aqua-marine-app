import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

parser_dir = 'aqua-language/src/parser/'
change_count = 0

def format_change_count(num):
    if 10 <= num % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(num % 10, "th")
    return f"{num}{suffix}"

print('Started watching aqua-language/pages/ for changes...')
class AquaChangeHandler(FileSystemEventHandler):
    def on_modified(self, event): # event: { event_type: 'modified', is_directory: False, src_path: '/Users/elijahmusaally/Desktop/aqua-marine-app/aqua-language/pages/HelloWorld.aqua' }
        global change_count
        if event.src_path.endswith('.aqua'):
            change_count += 1
            print(f"\n({format_change_count(change_count)}) Change detected...")
            print("Parsing Aqua files...")
            # Execute all Python files in the parser directory
            for filename in os.listdir(parser_dir):
                if filename.endswith('.py') and filename.startswith('aqua_to_'): # strictly checking for "aqua_to_[...].py" files
                    file_path = os.path.join(parser_dir, filename)
                    print(f"Executing: {os.path.basename(file_path)} with: {os.path.basename(event.src_path)}")
                    subprocess.run(['python3', file_path, event.src_path]) # remove last param if doesn't work

if __name__ == "__main__":
    path_to_watch = 'aqua-language/pages'
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

