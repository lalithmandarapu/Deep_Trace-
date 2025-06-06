import os
import csv
from bs4 import BeautifulSoup
from nlp import classify_text_batch
from categorize import get_possible_categories

def process_files(directory_path='archive', output_csv_path='data/hateful_files.csv'):
    with open(output_csv_path, 'a+', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        os.makedirs(directory_path, exist_ok=True)
        for filename in os.listdir(directory_path):
            if filename.endswith('.csv'):
                continue
            now = csvfile.tell()
            csvfile.seek(0)
            if filename in csvfile.read():
                continue
            csvfile.seek(now)
            file_path = os.path.join(directory_path, filename)

            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = file.read()

                    soup = BeautifulSoup(data, 'html.parser')
                    text_content = soup.text

                    classification_result = classify_text_batch([text_content])
                    categories = get_possible_categories(text_content)

                    if any(label['label'] == 'HATE' for label in classification_result):
                        csv_writer.writerow([filename, 'HATEFUL', categories])
                    else:
                        csv_writer.writerow([filename, 'NOT HATEFUL', categories])

if __name__ == "__main__":
    process_files()
