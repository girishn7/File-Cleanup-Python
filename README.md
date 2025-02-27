# File-Cleanup-Python
file cleanup python
This script is designed to automatically move files from the Downloads folder to a separate folder named to_delete if they have not been modified for more than a year (365 days). This helps in organizing and decluttering the Downloads folder by removing older unused files.

Steps:-
1.The script sets the Downloads folder path explicitly using:
folder_path = r"C:\\Users\\Downloads"
2.It defines the destination folder (to_delete) in the user's home directory.
3.If the to_delete folder does not exist, it creates it.
4.It retrieves the list of files in the Downloads folder.
5.It checks each file's last modified date and calculates the time difference.
6.If the file is older than 365 days, it is moved to the to_delete folder.
7.The script prints the names of moved files and displays "Process completed." after execution.
