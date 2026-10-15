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
        self.membership_locked = False

    def add_member(self, name):
        if self.membership_locked:
            raise ValueError("Members cannot join after payments have started.")

        clean_name = name.strip()

        if not clean_name:
            raise ValueError("A member name cannot be empty.")

        for existing_name in self.members:
            if existing_name.casefold() == clean_name.casefold():
                raise ValueError("This member already exists.")

        self.members.append(clean_name)

if __name__ == "__main__":
    group = SusuGroup("50.00")
    group.add_member("Ama")
    group.add_member("Kofi")
    group.add_member("Esi")
    group.add_member(" ama ")

    print("Susu group created.")
    print(f"Weekly contribution: {group.weekly_amount} pesewas")
    print(f"Current week: {group.current_week}")
    print("Members:", ", ".join(group.members))