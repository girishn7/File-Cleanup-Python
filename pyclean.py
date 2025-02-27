import os
import shutil
from datetime import datetime, timedelta

folder_path = r"C:\\Users\\giris\\OneDrive\\Downloads"

to_delete_folder_path = os.path.join(os.path.expanduser('~'), 'to_delete')

if not os.path.exists(to_delete_folder_path):
    os.makedirs(to_delete_folder_path)

files = os.listdir(folder_path)

now = datetime.now()

for file in files:
    file_path = os.path.join(folder_path, file)
    
    if os.path.isfile(file_path):
        modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
        time_difference = now - modified_date

        if time_difference > timedelta(days=365):
            shutil.move(file_path, to_delete_folder_path)
            print(f"Moved:{file}")

print("Process completed.")

