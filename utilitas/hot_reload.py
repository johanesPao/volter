import sys
import time
from subprocess import Popen
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

SCRIPT = "../main.py"


class RestartHandler(FileSystemEventHandler):
    def __init__(self):
        self.proses = None
        self.mulai_script()

    def mulai_script(self):
        if self.proses:
            self.proses.terminate()
        print(f"Memulai {SCRIPT}...")
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), SCRIPT))
        self.proses = Popen([sys.executable, "-u", script_path])

    def dalam_modifikasi(self, event):
        if event.src_path.endswith(".py"):
            print(f"Mendeteksi perubahan pada {event.src_path}, memulai kembali...")
            self.mulai_script()


if __name__ == "__main__":
    path_pengawasan = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    event_handler = RestartHandler()
    pengamat = Observer()
    pengamat.schedule(event_handler, path=path_pengawasan, recursive=True)
    pengamat.start()
    print("Hot reload dimulai, mengawasi perubahan pada file python...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pengamat.stop()
    pengamat.join()
