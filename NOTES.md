\# Assumptions and Decisions



\## Group membership



\- The program manages one group per session.

\- Members receive payouts in the order they joined.

\- Names cannot be empty.

\- Names are compared without capitalization differences and without

&#x20; surrounding spaces. "Ama" and " ama " refer to the same member.

\- Members can join until the first valid contribution is recorded.

\- After that contribution, membership is locked.

\- Members cannot be removed or renamed.



\## Contributions and money



\- The weekly contribution is fixed when the group is created.

\- Amounts must be positive, finite and have no more than two decimal places.

\- Money input uses a decimal point, for example 50.00.

\- Decimal reads the amount exactly; integer pesewas store the value.

\- Partial payments and multiple payments in the same week are allowed.

\- Payments cannot exceed the member's outstanding balance.

\- Payments are accepted only for the current week.

\- Past and future week payments are rejected.

\- Members continue contributing after receiving their own payout.



\## Closing weeks



\- A group with no members cannot close a week.

\- If anyone owes money, closing is refused and all outstanding balances

&#x20; are reported.

\- A refused closing does not change the week, payments or payout history.

\- When everyone has paid, the full pot is recorded for the next recipient.

\- The current week then advances and weekly payment balances reset.

\- A cycle lasts as many weeks as there are members.

\- After everyone receives one payout, the cycle ends.

\- The final report displays the advanced week number and marks the cycle

&#x20; complete. No further contributions or weekly closings are accepted.

\- Payouts are bookkeeping records, not real bank or mobile-money transfers.



\## Code organization



\- SusuGroup contains the savings rules.

\- main.py handles terminal input and displays messages.

\- Keeping these separate lets automated tests check the rules without

&#x20; entering information through the menu.

\- The project uses Python's built-in unittest module.



\## Known limitations



\- All data is kept in memory and disappears when the program exits.

\- There is no login system, database or payment-service connection.

\- Contributions cannot be edited or refunded.

\- Only one savings cycle is supported per session.

\- The report shows current balances and payout history, rather than a

&#x20; permanent transaction-by-transaction contribution ledger.



\## Improvements With More Time



\- Save and reload groups using a file or database.

\- Keep a detailed contribution ledger.

\- Support corrections and refunds with an audit history.

\- Support additional savings cycles.

\- Add automated tests for menu interactions.

\- Provide exportable reports.



\## Development Assistance



I used an AI assistant for step-by-step guidance, code examples and test

design. I ran the program and automated tests locally and built the

project through incremental Git commits.

