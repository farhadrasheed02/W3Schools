import logging
import os
import sys
from datetime import datetime

# Create logs folder if not exists
log_dir = r"C:\Users\Farhad_Rashid\PycharmProjects\W3Schools\logs"
os.makedirs(log_dir, exist_ok=True)

# Use the main script name for logfile
script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(log_dir, f"{script_name}_{timestamp}.log")
print(f"Test Report is getting generated: {log_file}")

logging.basicConfig(
    filename=log_file,
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
