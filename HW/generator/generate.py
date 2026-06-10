import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["BOOK_ID", "BOOK_WHIMSINESS_LEVEL", "BOOK_ANGST_LEVEL", "BOOK_AUTHOR"]

def generate_row():

    return {
        "BOOK_ID": random.randint(0, 100),
        "BOOK_WHIMSINESS_LEVEL": round(random.uniform(0.0, 10.0), 2),
        "BOOK_ANGST_LEVEL": random.randint(0, 100),
        "BOOK_AUTHOR": random.choice(["Charlotte Brontë", "Sally Rooney", "Jane Austen"]),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)
