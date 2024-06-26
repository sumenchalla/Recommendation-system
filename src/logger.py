import logging.config
import os
from pathlib import Path
import sys

log_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
folder ="log"
log_path = os.path.join(folder,"running_logs.log")
os.makedirs(folder,exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format=log_str,
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
    
)