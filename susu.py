from decimal import Decimal, InvalidOperation


def parse_money(amount_text):
    try:
        amount = Decimal(amount_text)
    except (InvalidOperation, ValueError):
        raise ValueError("Enter a valid amount, such as 50.00.")

    if not amount.is_finite() or amount <= 0:
        raise ValueError("The amount must be greater than zero.")

    if amount.as_tuple().exponent < -2:
        raise ValueError("Use no more than two decimal places.")

    whole, _, fraction = format(amount, "f").partition(".")
    return int(whole) * 100 + int(fraction.ljust(2, "0"))


def format_money(pesewas):
    return f"{pesewas // 100}.{pesewas % 100:02d}"


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

    def is_complete(self):
        return bool(self.members) and self.current_week > len(self.members)

    def amount_owed(self, name):
        member = self.find_member(name)

        if self.is_complete():
            return 0

        amount_paid = self.payments.get(member, 0)
        return self.weekly_amount - amount_paid

    def record_contribution(self, name, week, amount_text):
        if self.is_complete():
            raise ValueError("The savings cycle is complete.")

        if type(week) is not int or week != self.current_week:
            raise ValueError("Payments are accepted only for the current week.")

        member = self.find_member(name)
        amount = parse_money(amount_text)

        if amount > self.amount_owed(member):
            raise ValueError("Payment exceeds what this member owes.")

        self.payments[member] = self.payments.get(member, 0) + amount
        self.membership_locked = True

    def close_week(self):
        if not self.members:
            raise ValueError("Add members before closing a week.")

        if self.is_complete():
            raise ValueError("The savings cycle is complete.")

        outstanding = []

        for member in self.members:
            owed = self.amount_owed(member)

            if owed > 0:
                outstanding.append(
                    f"{member} owes GHS {format_money(owed)}"
                )

        if outstanding:
            raise ValueError(
                "Week cannot close: " + "; ".join(outstanding)
            )

        recipient = self.members[self.current_week - 1]
        pot = self.weekly_amount * len(self.members)

        payout = {
            "week": self.current_week,
            "member": recipient,
            "amount": pot,
        }

        self.payout_history.append(payout)
        self.current_week += 1
        self.payments = {}

        return payout

    def report(self):
        lines = [
            "SUSU GROUP REPORT",
            f"Weekly contribution: GHS {format_money(self.weekly_amount)}",
            f"Current week: {self.current_week}",
        ]

        if self.is_complete():
            lines.append("Status: savings cycle complete.")
        elif self.members:
            next_member = self.members[self.current_week - 1]
            lines.append(f"Next payout recipient: {next_member}")
        else:
            lines.append("No members have joined yet.")

        lines.append("")
        lines.append("Member balances:")

        for member in self.members:
            owed = self.amount_owed(member)

            if self.is_complete():
                lines.append(f"- {member}: cycle complete, nothing owed")
            elif owed == 0:
                lines.append(f"- {member}: paid in full")
            else:
                lines.append(
                    f"- {member}: owes GHS {format_money(owed)}"
                )

        lines.append("")
        lines.append("Payout history:")

        if not self.payout_history:
            lines.append("No payouts yet.")

        for payout in self.payout_history:
            lines.append(
                f"- Week {payout['week']}: "
                f"{payout['member']} received "
                f"GHS {format_money(payout['amount'])}"
            )

        return "\n".join(lines)


if __name__ == "__main__":
    group = SusuGroup("50.00")
    group.add_member("Ama")
    group.add_member("Kofi")
    group.add_member("Esi")

    group.record_contribution("Ama", 1, "50.00")
    group.record_contribution("Kofi", 1, "50.00")
    group.record_contribution("Esi", 1, "30.00")

    try:
        group.close_week()
    except ValueError as error:
        print(error)

    print(f"Current week: {group.current_week}")

    group.record_contribution("Esi", 1, "20.00")
    payout = group.close_week()

    print(
        f"{payout['member']} receives "
        f"GHS {format_money(payout['amount'])}"
    )
    print()
    print(group.report())