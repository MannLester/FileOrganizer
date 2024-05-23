import os
import shutil
from datetime import datetime

# Set up folder paths
desktop_path = os.path.join(os.path.expanduser("~"), "OneDrive", "Desktop")
organized_folder = os.path.join(desktop_path, "Organized Downloaded Files")
image_folder = os.path.join(organized_folder, "Images")
video_folder = os.path.join(organized_folder, "Videos")
pdf_folder = os.path.join(organized_folder, "PDFs")

# Create main folder if it doesn't exist
for folder in [organized_folder, image_folder, video_folder, pdf_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

def organize_downloads():
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        if os.path.isfile(file_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                move_to_folder(file_path, image_folder)
            elif filename.lower().endswith(('.mp4', '.avi', '.mkv')):
                move_to_folder(file_path, video_folder)
            elif filename.lower().endswith('.pdf'):
                move_to_folder(file_path, pdf_folder)

def move_to_folder(file_path, destination_folder):
    creation_time = os.path.getctime(file_path)
    creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
    date_folder = os.path.join(destination_folder, creation_date)
    if not os.path.exists(date_folder):
        os.makedirs(date_folder)
    destination_file_path = os.path.join(date_folder, os.path.basename(file_path))
    shutil.move(file_path, destination_file_path)
    print(f"Moved {os.path.basename(file_path)} to {date_folder}")

if __name__ == "__main__":
    organize_downloads()
