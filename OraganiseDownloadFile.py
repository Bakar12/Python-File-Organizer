import os
import shutil

# Define the download directory and target directories
download_dir = "Downloads"
target_dirs = {
    "images": r"C:\Users\abuba\OneDrive\Pictures",
    "documents": r"C:\Users\abuba\OneDrive\Documents",
    "videos": "Videos",
    "music": "Music",
    "archives": "archives",
    "others": "Downloads"
}

# Mapping of file extensions to target directories
extension_mapping = {
    ".jpg": target_dirs["images"],
    ".jpeg": target_dirs["images"],
    ".png": target_dirs["images"],
    ".gif": target_dirs["images"],
    ".bmp": target_dirs["images"],
    ".pdf": target_dirs["documents"],
    ".doc": target_dirs["documents"],
    ".docx": target_dirs["documents"],
    ".xls": target_dirs["documents"],
    ".xlsx": target_dirs["documents"],
    ".ppt": target_dirs["documents"],
    ".pptx": target_dirs["documents"],
    ".txt": target_dirs["documents"],
    ".mp4": target_dirs["videos"],
    ".mkv": target_dirs["videos"],
    ".avi": target_dirs["videos"],
    ".mp3": target_dirs["music"],
    ".wav": target_dirs["music"],
    ".zip": target_dirs["archives"],
    ".rar": target_dirs["archives"],
    ".7z": target_dirs["archives"]
}


# Function to move files to the appropriate directories
def organize_files():
    # Create target directories if they don't exist
    for target_dir in target_dirs.values():
        os.makedirs(target_dir, exist_ok=True)

    # Iterate through each file in the download directory
    for filename in os.listdir(download_dir):
        file_path = os.path.join(download_dir, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file's extension
        file_ext = os.path.splitext(filename)[1].lower()

        # Get the target directory for the file extension
        target_dir = extension_mapping.get(file_ext, target_dirs["others"])

        # Move the file to the target directory
        shutil.move(file_path, os.path.join(target_dir, filename))


if __name__ == "__main__":
    organize_files()
    print("Files organized successfully.")
