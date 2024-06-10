import sys
import csv
import os
from datetime import datetime
from Bio import Entrez

Entrez.email = "adi.bar-el-meisel@weizmann.ac.il"
MAX_NUMBER_TO_FETCH = 100000


def ensure_log_file():
    if not os.path.exists("search_log.csv"):
        with open("search_log.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["date", "term", "max", "total"])

def search_ncbi(term, number):
    handle = Entrez.esearch(db="nucleotide", term=term, retmax=number)
    record = Entrez.read(handle)
    handle.close()
    return record["IdList"], record["Count"]

def fetch_and_save_data(ids):
    filenames = []
    for i, id in enumerate(ids):
        handle = Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
        filename = f"result_{id}.gb"
        with open(filename, "w") as file:
            file.write(handle.read())
        filenames.append(filename)
        handle.close()
    return filenames

def update_log_search(term, max_number, total_count):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = [date, term, max_number, total_count]
    ensure_log_file()
    # Append to the CSV log file
    with open("search_log.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(log_entry)

def main():
    if len(sys.argv) != 3:
        print("Usage: python ncbi.py TERM NUMBER")
        sys.exit(1)

    term = sys.argv[1]
    number = int(sys.argv[2])

    if number > MAX_NUMBER_TO_FETCH:
        print("Please enter a number of sequences less than", MAX_NUMBER_TO_FETCH)
        sys.exit(1)

    ids, total_count = search_ncbi(term, number)
    filenames = fetch_and_save_data(ids)
    for filename in filenames:
        print(filename)

    update_log_search(term, number, total_count)

if __name__ == "__main__":
    main()
