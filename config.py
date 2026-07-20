from pathlib import Path

# ===============================
# PROJECT PATHS
# ===============================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

REPORT_DIR = BASE_DIR / "reports"

EXCEL_DIR = BASE_DIR / "excel"

LOG_DIR = BASE_DIR / "logs"

# ===============================
# CREATE FOLDERS IF THEY DON'T EXIST
# ===============================

for folder in [
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    REPORT_DIR,
    EXCEL_DIR,
    LOG_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)