import csv
import datetime
import re

# Problem 1: The "AI Training Data" Cleaner (CSV & Strings)


# Create a Decorator called @audit_log that prints the name of the file being processed and the current time.
def audit_log(fun):
    def wrapper(*args, **kwargs):
        print(f"---Starting Processing for {fun.__name__}---")
        print(f"------Start time------")
        print(datetime.datetime.now())
        result = fun(*args, **kwargs)
        print(f"------End time------")
        print(datetime.datetime.now())
        return result

    return wrapper


# Load the csv file
def load_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            header = reader.fieldnames
            return header, list(reader)
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None, []

# The Process: For every review, convert the text to lowercase, remove any special characters (like !, @, #), and strip extra whitespace.


def clean_review(row):
    # Use .get() as a safety net
    tid_raw = row.get('ReviewID', 0)
    comment_raw = row.get('Text', "")
    rating_raw = row.get('Rating', 0)

    # 1. Regex: Keep alphanumeric and spaces, lowercase it
    comment = re.sub(r'[^a-zA-Z0-9 ]', '', comment_raw).lower()
    # 2. The Magic: Collapse multiple internal spaces into one and trim leading/trailing spaces
    comment = " ".join(comment.split())

    return [int(tid_raw), comment, int(rating_raw)]

# Write the "cleaned" data into a new file called cleaned_reviews.csv


def write_csv(base_name, header, data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    file_path = f"./Self_run/Cleaner/output/{base_name}_{timestamp}.csv"
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)  # Write header
            csv_writer.writerows(data)   # Write data rows
    except Exception as e:
        print(f"Error writing CSV: {e}")


@audit_log
def run_pipeline():
    header, list_rows = load_csv("Self_run/Cleaner/raw_reviews.csv")
    cleaned_data = []
    for row in list_rows:
        cleaned_data.append(clean_review(row))
    write_csv("cleaned_reviews", header, cleaned_data)


if __name__ == "__main__":
    run_pipeline()
