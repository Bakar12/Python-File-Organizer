# Python File Organizer

This Python script organizes files in the "Downloads" directory by moving them to appropriate directories based on their file extensions.

## How it works

The script defines a mapping of file extensions to target directories. It then iterates through each file in the "Downloads" directory, determines the file's extension, and moves the file to the corresponding target directory.

## Target Directories

The target directories are defined as follows:

- Images (`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`): `Pictures`
- Documents (`.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.txt`): `Documents`
- Videos (`.mp4`, `.mkv`, `.avi`): `Videos`
- Music (`.mp3`, `.wav`): `Music`
- Archives (`.zip`, `.rar`, `.7z`): `Archives`
- Others: `Downloads`

## Usage

To run the script, navigate to the directory containing `OraganiseDownloadFile.py` and run the following command:

```bash
python OraganiseDownloadFile.py
```