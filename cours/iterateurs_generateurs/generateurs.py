def generate_promo_codes(prefix="PROMO", start=1):
    count = start
    while True:
        yield f"{prefix}-{count:003}"
        count += 1

if __name__ == "__main__":
    codes = generate_promo_codes()

    # print(next(codes))

    # for _ in range(1_000_000):
    #     print(next(codes))