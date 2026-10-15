from susu import SusuGroup, format_money


def main():
    print("Welcome to Susu Manager")
    print("Amounts are in GHS, for example 50.00.")
    print("Data is kept only while this program is running.")
    print()

    while True:
        weekly_amount = input("Enter the weekly contribution: ").strip()

        try:
            group = SusuGroup(weekly_amount)
            break
        except ValueError as error:
            print(f"Error: {error}")

    print("Group created.")

    while True:
        print()
        print("1. Add a member")
        print("2. Record a contribution")
        print("3. Close the current week")
        print("4. Show report")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        try:
            if choice == "1":
                name = input("Member name: ")
                group.add_member(name)
                print(f"Member added: {name.strip()}")

            elif choice == "2":
                if not group.members:
                    print("Add members before recording contributions.")
                    continue

                if group.is_complete():
                    print("The savings cycle is complete.")
                    continue

                print(f"Current week: {group.current_week}")
                name = input("Member name: ")

                try:
                    week = int(input("Week number: ").strip())
                except ValueError:
                    print("Enter a whole number for the week.")
                    continue

                amount = input("Contribution amount in GHS: ").strip()
                group.record_contribution(name, week, amount)
                owed = group.amount_owed(name)

                print("Contribution recorded.")
                print(f"Remaining balance: GHS {format_money(owed)}")

            elif choice == "3":
                payout = group.close_week()

                print(
                    f"Week {payout['week']} closed. "
                    f"{payout['member']} receives "
                    f"GHS {format_money(payout['amount'])}."
                )

                if group.is_complete():
                    print("The savings cycle is complete.")
                else:
                    next_member = group.members[group.current_week - 1]
                    print(f"Current week: {group.current_week}")
                    print(f"Next payout recipient: {next_member}")

            elif choice == "4":
                print()
                print(group.report())

            elif choice == "5":
                print("Goodbye. Session data has not been saved.")
                break

            else:
                print("Choose a number from 1 to 5.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram closed. Session data has not been saved.")