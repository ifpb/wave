import yaml, time, os
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class YamlHandler(FileSystemEventHandler):
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.data = yaml.load(file, Loader=yaml.FullLoader)
        except FileNotFoundError:
            print(f"Arquivo não foi criado!")

    def on_modified(self, event):
        if event.server_path == self.filename:
            with open(self.filename, 'r') as file:
                new_data = yaml.load(file, Loader=yaml.FullLoader)
                if new_data != self.data:
                    self.data = new_data
                    print(f"Arquivo {event.server_path} foi modificado. Novo conteúdo: {self.data}")

if __name__ == "__main__":

    path_app = Path(os.path.abspath("app"))    
    config_yaml_dir = Path(path_app,"provision") 
    event_handler = YamlHandler(f"{config_yaml_dir}/config.yaml")
    observer = Observer()
    observer.schedule(event_handler, path=f"{config_yaml_dir}", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

