import csv
import random
from datetime import date, timedelta
import time

def random_date(start: date, end: date) -> date:
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, delta))

def generate_loans_csv(path: str, num_rows: int) -> None:
    start_time = time.time()
    
    user_ids = [f"user_{i}" for i in range(1, 10001)]
    book_ids = [f"book_{i}" for i in range(1, 5001)]

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["user_id", "book_id", "borrow_date", "return_date", "n"])

        for i in range(num_rows):
            user_id = random.choice(user_ids)
            book_id = random.choice(book_ids)
            borrow = random_date(date(2020, 1, 1), date(2025, 1, 1))
            return_d = borrow + timedelta(days=random.randint(1, 60))
            n = random.randint(0, 1000)

            writer.writerow([user_id, book_id, borrow.isoformat(), return_d.isoformat(), n])

            if i % 1_000_000 == 0 and i > 0:
                elapsed = time.time() - start_time
                print(f"{i:,} lignes générées... ({elapsed:.1f}s)")

if __name__ == "__main__":
    n: int = 10_000_000
    print(f"⏳ Génération de {n} de lignes dans 'loans.csv'...")
    generate_loans_csv(r".\big_loans.csv", num_rows=n)
    print("✅ Terminé.")
