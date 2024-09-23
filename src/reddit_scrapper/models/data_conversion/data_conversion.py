import json
import csv

def export_json(submission_list: list):
    jsonInfo = json.dumps(submission_list, indent=4, ensure_ascii=False)
    with open("data.json", "w",  newline='', encoding='utf-8') as json_file:
        json_file.write(jsonInfo)
    print("Data saved as json!")

def export_csv(submission_list: list):
    with open("data.csv", "w", newline='', encoding='utf-8') as csv_file:
        fieldnames = submission_list[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in submission_list:
            writer.writerow(row)
    print("Data saved as csv!")
