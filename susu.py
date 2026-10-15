from decimal import Decimal, InvalidOperation


def parse_money(amount_text):
    try:
        amount = Decimal(amount_text)
    except InvalidOperation:
        raise ValueError("Enter a valid amount, such as 50.00.")

    if not amount.is_finite() or amount <= 0:
        raise ValueError("The amount must be greater than zero.")

    pesewas = amount * 100

    if pesewas != pesewas.to_integral_value():
        raise ValueError("The amount cannot include fractions of a pesewa.")

    return int(pesewas)


class SusuGroup:
    def __init__(self, weekly_amount):
        self.weekly_amount = parse_money(weekly_amount)
        self.members = []
        self.current_week = 1
        self.payout_history = []


if __name__ == "__main__":
    group = SusuGroup("50.00")
    print("Susu group created.")
    print(f"Weekly contribution: {group.weekly_amount} pesewas")
    print(f"Current week: {group.current_week}")