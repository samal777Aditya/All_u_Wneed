import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of files to create
list_of_files = [
    "data/pdfs/pdf1.pdf",
    "data/pdfs/pdf2.pdf",
    "data/images/image.jpg",
    "data/datasets/custom_data.csv",
    "scripts/model_setup.py",
    "scripts/text_generation.py",
    "scripts/fine_tuning.py",
    "scripts/pdf_processing.py",
    "scripts/data_analysis.py",
    "scripts/image_processing.py",
    "scripts/helper_functions.py",
    "main.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent  # Get the parent directory
    filename = filepath.name  # Get the file name
    
    if filedir and not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {filedir}")
    
    if not filepath.exists():
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
