import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class AquaChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.aqua'):
            print(f"Change detected in {event.src_path}, re-running main.py...")
            subprocess.run(['python3', 'path/to/main.py'])

if __name__ == "__main__":
    path_to_watch = 'aqua-language/src/'  # Adjust to your Aqua source directory
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
