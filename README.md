\# Susu Manager



A Python text-menu program for managing one rotating savings group.



Members contribute a fixed weekly amount. Once everyone has paid in full,

the pot is recorded as paid to the next member in joining order.



\## Requirements



\- Python 3.10 or newer.

\- No third-party packages are needed.



\## How to run



Open PowerShell in the project folder.



Run the interactive program:

&#x20;   py main.py



Run the assignment example:

&#x20;   py susu.py



If your computer uses python instead of py, substitute python in these commands.



\## Menu options



1\. Add a member.

2\. Record a contribution.

3\. Close the current week.

4\. Show the report.

5\. Exit.



Add every member before recording the first contribution.

Enter amounts in GHS using a decimal point, such as 50.00.



\## How to run the tests



From the project folder, run:

&#x20;   py -m unittest -v



The suite contains 16 automated tests, including partial payments,

blocked weekly closing, invalid payments, payout order and exact money.



\## Example



Ama, Kofi and Esi each owe GHS 50.00 for week 1.

Ama and Kofi pay 50.00 each. Esi pays 30.00.

Closing is refused because Esi owes 20.00.

Esi pays the remaining 20.00.

Closing succeeds and Ama receives a recorded payout of GHS 150.00.

Week 2 begins, with Kofi next.



\## Money handling



Decimal reads monetary inputs exactly.

Amounts are stored and calculated as integer pesewas.

GHS 50.00 is stored as 5000 pesewas.

Floating-point money calculations are not used.



\## Project files



\- susu.py: savings rules, reporting and example.

\- main.py: interactive text menu.

\- test\_susu.py: 16 automated tests.

\- NOTES.md: assumptions, decisions and improvements.

\- .gitignore: excludes temporary Python files.



\## Limitations



Data is held in memory and is lost when the program exits.

Payouts are records only; no real money is transferred.

Each session supports one group and one savings cycle.



See NOTES.md for further details.

