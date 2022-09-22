from multiprocessing import Event
import time
import os 
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Majeed-Home/Downloads"
to_dir = "Document_Files" 

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,ext = os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if ext in value:
                fname = os.path.basename(event.src_path)
                print("Downloaded " + fname)

                path1 = from_dir + '/' + fname
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + fname

                if os.path.exists(path2):

                    print("Directory Exists...")
                    print("Moving " + fname + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving " + fname + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)
          

event_Handler = FileSystemEventHandler()
observer = Observer()
observer.schedule(event_Handler,from_dir,recursive=True)
observer.start()
try:
    while True :
        time.sleep(2)
        print("running.....")
except KeyboardInterrupt:
    print("stop")   
    observer.stop()  