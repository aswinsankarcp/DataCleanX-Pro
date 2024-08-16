import os

def validate_file(file_path, extensions):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if not any(file_path.endswith(ext) for ext in extensions):
        raise ValueError(f"Invalid file type. Expected one of {extensions}")
