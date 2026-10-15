import unittest

from susu import SusuGroup, parse_money


class TestSusuGroup(unittest.TestCase):
    def setUp(self):
        self.group = SusuGroup("50.00")
        self.group.add_member("Ama")
        self.group.add_member("Kofi")
        self.group.add_member("Esi")

    def pay_everyone(self):
        for member in self.group.members:
            self.group.record_contribution(
                member, self.group.current_week, "50.00"
            )

    def test_create_group(self):
        self.assertEqual(self.group.weekly_amount, 5000)
        self.assertEqual(self.group.current_week, 1)

    def test_money_is_exact(self):
        group = SusuGroup("0.30")
        group.add_member("Ama")
        group.record_contribution("Ama", 1, "0.10")
        group.record_contribution("Ama", 1, "0.20")

        self.assertEqual(group.amount_owed("Ama"), 0)

    def test_invalid_amounts_are_rejected(self):
        for amount in ("0", "-10", "abc", "NaN", "Infinity", "1.001"):
            with self.subTest(amount=amount):
                with self.assertRaises(ValueError):
                    parse_money(amount)

    def test_duplicate_member_is_rejected(self):
        with self.assertRaises(ValueError):
            self.group.add_member(" ama ")

        self.assertEqual(len(self.group.members), 3)

    def test_empty_member_is_rejected(self):
        with self.assertRaises(ValueError):
            self.group.add_member("   ")

    def test_unknown_member_is_rejected(self):
        with self.assertRaises(ValueError):
            self.group.record_contribution("Unknown", 1, "10.00")

        self.assertEqual(self.group.payments, {})

    def test_partial_payments(self):
        self.group.record_contribution("Esi", 1, "30.00")
        self.assertEqual(self.group.amount_owed("Esi"), 2000)

        self.group.record_contribution("Esi", 1, "20.00")
        self.assertEqual(self.group.amount_owed("Esi"), 0)

    def test_overpayment_is_rejected(self):
        self.group.record_contribution("Esi", 1, "30.00")

        with self.assertRaises(ValueError):
            self.group.record_contribution("Esi", 1, "20.01")

        self.assertEqual(self.group.amount_owed("Esi"), 2000)

    def test_invalid_contributions_are_rejected(self):
        for amount in ("0", "-1", "abc"):
            with self.subTest(amount=amount):
                with self.assertRaises(ValueError):
                    self.group.record_contribution("Ama", 1, amount)

        self.assertEqual(self.group.payments, {})
        self.assertFalse(self.group.membership_locked)

    def test_wrong_week_is_rejected(self):
        for week in (0, 2):
            with self.subTest(week=week):
                with self.assertRaises(ValueError):
                    self.group.record_contribution("Ama", week, "50.00")

        self.assertEqual(self.group.payments, {})

    def test_week_cannot_close_with_unpaid_balance(self):
        self.group.record_contribution("Ama", 1, "50.00")
        self.group.record_contribution("Kofi", 1, "50.00")
        self.group.record_contribution("Esi", 1, "30.00")

        with self.assertRaisesRegex(
            ValueError, r"Esi owes GHS 20\.00"
        ):
            self.group.close_week()

        self.assertEqual(self.group.current_week, 1)
        self.assertEqual(self.group.payout_history, [])
        self.assertEqual(self.group.amount_owed("Esi"), 2000)

        self.group.record_contribution("Esi", 1, "20.00")
        payout = self.group.close_week()

        self.assertEqual(payout["member"], "Ama")
        self.assertEqual(payout["amount"], 15000)
        self.assertEqual(self.group.current_week, 2)
        self.assertEqual(self.group.amount_owed("Ama"), 5000)

    def test_payouts_follow_joining_order(self):
        for expected_member in ("Ama", "Kofi", "Esi"):
            self.pay_everyone()
            payout = self.group.close_week()

            self.assertEqual(payout["member"], expected_member)
            self.assertEqual(payout["amount"], 15000)

        self.assertEqual(len(self.group.payout_history), 3)
        self.assertTrue(self.group.is_complete())

    def test_membership_locks_after_first_payment(self):
        self.group.record_contribution("Ama", 1, "1.00")

        with self.assertRaises(ValueError):
            self.group.add_member("Yaw")

        self.assertEqual(len(self.group.members), 3)

    def test_empty_group_cannot_close(self):
        group = SusuGroup("50.00")

        with self.assertRaises(ValueError):
            group.close_week()

        self.assertEqual(group.current_week, 1)

    def test_completed_cycle_rejects_more_activity(self):
        group = SusuGroup("50.00")
        group.add_member("Ama")
        group.record_contribution("Ama", 1, "50.00")
        group.close_week()

        with self.assertRaises(ValueError):
            group.record_contribution("Ama", 2, "50.00")

        with self.assertRaises(ValueError):
            group.close_week()

        self.assertEqual(len(group.payout_history), 1)
        self.assertEqual(group.amount_owed("Ama"), 0)

    def test_report_shows_balances_and_history(self):
        self.group.record_contribution("Ama", 1, "50.00")
        report = self.group.report()

        self.assertIn("Ama: paid in full", report)
        self.assertIn("Kofi: owes GHS 50.00", report)
        self.assertIn("No payouts yet.", report)

        self.group.record_contribution("Kofi", 1, "50.00")
        self.group.record_contribution("Esi", 1, "50.00")
        self.group.close_week()
        report = self.group.report()

        self.assertIn("Current week: 2", report)
        self.assertIn("Next payout recipient: Kofi", report)
        self.assertIn("Week 1: Ama received GHS 150.00", report)


if __name__ == "__main__":
    unittest.main()