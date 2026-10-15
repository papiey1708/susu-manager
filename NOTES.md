\# Assumptions and Decisions



\## Group membership



\- One group is managed per session.

\- Members receive payouts in joining order.

\- Names cannot be empty.

\- Names are compared ignoring capitalization and surrounding spaces.

\- "Ama" and " ama " identify the same member.

\- Members can join until the first valid contribution is recorded.

\- That first contribution locks membership.

\- Members cannot be removed or renamed.



\## Contributions and money



\- The weekly amount is fixed when the group is created.

\- Amounts must be positive and finite.

\- Inputs allow no more than two decimal places.

\- Money input uses a decimal point, for example 50.00.

\- Decimal reads inputs exactly; integer pesewas store the money.

\- Partial payments and multiple payments per week are allowed.

\- A payment cannot exceed the member's outstanding balance.

\- Only payments for the current week are accepted.

\- Past and future week payments are rejected.

\- Members continue contributing after receiving their payout.



\## Closing weeks



\- A group without members cannot close a week.

\- If anyone owes money, closing is refused and outstanding balances are reported.

\- Refusing to close leaves the week, contributions and payout history unchanged.

\- Once everyone has paid, the full pot is recorded for the next recipient.

\- The week advances and current contribution balances reset.

\- One cycle lasts as many weeks as there are members.

\- The cycle ends after every member receives one payout.

\- The final report shows the advanced week number and marks the cycle complete.

\- Completed cycles reject further contributions and weekly closings.

\- Payouts are records only; no real money is transferred.



\## Code organization



\- susu.py contains the savings rules and report generation.

\- main.py handles the text menu and user input.

\- Separating these allows the rules to be tested without menu interaction.

\- Tests use Python's built-in unittest module.

\- No third-party packages are required.



\## Known limitations



\- Data is held in memory and disappears when the program exits.

\- There is no database, login system or payment-service connection.

\- Contributions cannot be corrected or refunded.

\- Only one savings cycle is supported per session.

\- Reports show current balances and payout history.

\- There is no permanent contribution transaction ledger.



\## Improvements with more time



\- Save and reload data using a file or database.

\- Keep a detailed contribution ledger.

\- Support corrections and refunds with an audit history.

\- Support additional savings cycles.

\- Add automated tests for menu interactions.

\- Export reports to files.



\## Development assistance



I used an AI assistant for step-by-step guidance, code examples and test design.

I ran the program and automated tests locally.

I developed the project through incremental Git commits.

