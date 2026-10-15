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
        self.payments = {}

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
    def find_member(self, name):
        clean_name = name.strip()

        for existing_name in self.members:
            if existing_name.casefold() == clean_name.casefold():
                return existing_name

        raise ValueError("Unknown member.")

    def amount_owed(self, name):
        member = self.find_member(name)
        amount_paid = self.payments.get(member, 0)
        return self.weekly_amount - amount_paid

    def record_contribution(self, name, week, amount_text):
        if week != self.current_week:
            raise ValueError("Payments are accepted only for the current week.")

        member = self.find_member(name)
        amount = parse_money(amount_text)

        if amount > self.amount_owed(member):
            raise ValueError("Payment exceeds what this member owes.")

        self.payments[member] = self.payments.get(member, 0) + amount
        self.membership_locked = True

if __name__ == "__main__":
    group = SusuGroup("50.00")
    group.add_member("Ama")
    group.add_member("Kofi")
    group.add_member("Esi")
    

    print("Susu group created.")
    print(f"Weekly contribution: {group.weekly_amount} pesewas")
    print(f"Current week: {group.current_week}")
    print("Members:", ", ".join(group.members))
    group.record_contribution("Esi", 1, "30.00")
    print(f"Esi owes: {group.amount_owed('Esi')} pesewas")

    group.record_contribution("Esi", 1, "20.00")
    print(f"Esi now owes: {group.amount_owed('Esi')} pesewas")
   