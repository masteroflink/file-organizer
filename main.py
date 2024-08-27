import os
import shutil
from dotenv import load_dotenv

DOTENV_FILE = os.getenv('DOTENV_FILE', './.env')

load_dotenv(dotenv_path=DOTENV_FILE)

# ENV vars set in env file
SOURCE_DIR = os.environ['SOURCE_DIR']
DATA_DIR = os.environ['DATA_DIR']
IMAGE_DIR = os.environ['IMAGE_DIR']
DOCUMENTS_DIR = os.environ['DOCUMENTS_DIR']
EXE_DIR = os.environ['EXE_DIR']
MUSIC_DIR = os.environ['MUSIC_DIR']
VIDEO_DIR = os.environ['VIDEO_DIR']
ARCHIVE_DIR = os.environ['ARCHIVE_DIR']

FILE_EXT = {
    'pdf': DOCUMENTS_DIR,
    'png': IMAGE_DIR,
    'jpg': IMAGE_DIR,
    'jpeg': IMAGE_DIR,
    'gif': IMAGE_DIR,
    'doc': DOCUMENTS_DIR,
    'docx': DOCUMENTS_DIR,
    'txt': DOCUMENTS_DIR,
    'csv': DATA_DIR,
    'xlsx': DATA_DIR,
    'zip': ARCHIVE_DIR,
    'rar': ARCHIVE_DIR,
    'exe': EXE_DIR,
    'mp3': MUSIC_DIR,
    'wav': MUSIC_DIR,
    'mp4': VIDEO_DIR,
    'avi': VIDEO_DIR,
    'flv': VIDEO_DIR,
    'wmv': VIDEO_DIR
}

for root, dirs, files in os.walk(SOURCE_DIR):
    for f in files:
        print(f"working: {f}")
        base_filename, file_ext = os.path.splitext(f)
        if file_ext[1:] not in FILE_EXT.keys():
            print(f"{file_ext} not valid. Skipping.")
            continue

        dest_filename = os.path.join(FILE_EXT[file_ext[1:]], f)

        if os.path.isfile(dest_filename):
            if input(f"File {f} already exists. Overwrite it? (y/n)").lower() == 'y':
                print("Overwriting file.")
            else:
                print("Skipping to prevent overwriting.")
                continue

        os.rename(os.path.join(root, f), os.path.join(FILE_EXT[file_ext[1:]], f))
        print(f"Successfully moved: {f}")
