from typing import Iterator

class InvoiceNumberIterator:
    def __init__(self, prefix: str = "FAC", start: int = 1) -> None:
        self.prefix: str = prefix
        self.current: int = start

    def __iter__(self) -> Iterator[str]:
        return self

    def __next__(self) -> str:
        invoice_number: str = f"{self.prefix}-{self.current:03}"
        self.current += 1
        return invoice_number


invoices: InvoiceNumberIterator = InvoiceNumberIterator()

print(next(invoices))  # FAC-001
print(next(invoices))  # FAC-002

custom: InvoiceNumberIterator = InvoiceNumberIterator(prefix="INV", start=42)
print(next(custom))    # INV-042
print(next(custom))    # INV-043
