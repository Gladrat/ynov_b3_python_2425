from datetime import date
import csv

from rich.pretty import pprint


def load_loans_csv(path):
    loans = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            loans.append({
                "loan_id": row["loan_id"],
                "user_id": row["user_id"],
                "book_id": row["book_id"],
                "book_title": row["book_title"],
                "borrow_date": date.fromisoformat(row["borrow_date"]),
                "return_date": date.fromisoformat(row["return_date"]),
            })
    return loans


def get_active_loans(loans):
    today = date.today()
    return [
        loan for loan in loans
        if loan["return_date"] >= today
    ]


if __name__ == "__main__":
    data = load_loans_csv(r'.\library_loans.csv')

    pprint(len(data))

    pprint(get_active_loans(data))
    pprint(len(get_active_loans(data)))
