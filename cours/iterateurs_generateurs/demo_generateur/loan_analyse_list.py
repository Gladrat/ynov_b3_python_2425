import csv
from datetime import date
from typing import TypedDict


class Loan(TypedDict):
    user_id: str
    book_id: str
    borrow_date: date
    return_date: date


def load_loans(path: str) -> list[Loan]:
    loans: list[Loan] = []
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                loans.append({
                    "user_id": row["user_id"],
                    "book_id": row["book_id"],
                    "borrow_date": date.fromisoformat(row["borrow_date"]),
                    "return_date": date.fromisoformat(row["return_date"])
                })
            except (KeyError, ValueError):
                # Ligne mal formée — on l’ignore
                continue
    return loans


def get_overdue_loans(loans: list[Loan]) -> list[Loan]:
    today = date.today()
    return [loan for loan in loans if loan["return_date"] < today]


# --- Utilisation ---
if __name__ == "__main__":
    filepath = r".\loans.csv"
    all_loans = load_loans(filepath)
    overdue_loans = get_overdue_loans(all_loans)

    print("📋 Prêts en retard :")
    for loan in overdue_loans:
        # print(f"- Utilisateur {loan['user_id']} doit rendre {loan['book_id']} (retour prévu le {loan['return_date']})")
        continue
