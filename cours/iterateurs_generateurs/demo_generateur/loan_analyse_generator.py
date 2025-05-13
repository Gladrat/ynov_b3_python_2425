import csv
from datetime import date
from typing import Generator, TypedDict


class Loan(TypedDict):
    user_id: str
    book_id: str
    borrow_date: date
    return_date: date


def load_loans_lazy(filepath: str) -> Generator[Loan, None, None]:
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                yield {
                    "user_id": row["user_id"],
                    "book_id": row["book_id"],
                    "borrow_date": date.fromisoformat(row["borrow_date"]),
                    "return_date": date.fromisoformat(row["return_date"])
                }
            except (KeyError, ValueError):
                # Ligne mal formée — on l’ignore
                continue


def get_overdue_loans(loans: Generator[Loan, None, None]) -> Generator[Loan, None, None]:
    today = date.today()
    for loan in loans:
        if loan["return_date"] < today:
            yield loan


# --- Utilisation ---
if __name__ == "__main__":
    filepath = r".\loans.csv"
    overdue_loans = get_overdue_loans(load_loans_lazy(filepath))

    print("📋 Prêts en retard :")
    for loan in overdue_loans:
        # print(f"- Utilisateur {loan['user_id']} doit rendre {loan['book_id']} (retour prévu le {loan['return_date']})")
        continue
