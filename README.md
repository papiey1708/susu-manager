\# Susu Manager



A Python command-line program for managing one rotating savings group.



Each member contributes the same fixed amount every week. Once everyone

has paid in full, the pot is recorded as paid to the next member in joining

order.



\## Requirements



\- Python 3.10 or newer.

\- No third-party packages are required.



\## Run the program



Open a terminal in the project folder and run:



```powershell

py main.py

```



If your computer uses the `python` command instead, run:



```text

python main.py

```



Enter the weekly contribution, then use the menu:



1\. Add a member.

2\. Record a contribution.

3\. Close the current week.

4\. Show the report.

5\. Exit.



Add all members before recording the first payment.



Data stays in memory and is lost when the program exits.

Payouts are recorded only; no actual money is transferred.



\## Run the tests



From the project folder, run:



```powershell

py -m unittest -v

```



Alternatively:



```text

python -m unittest -v

```



There are 16 automated tests covering group creation, exact money

calculations, member validation, partial payments, overpayments,

invalid amounts, week validation, blocked weekly closing, payout

order, membership locking, cycle completion and reports.



\## Run the demonstration



```powershell

py susu.py

```



The demonstration follows the assignment example:



\- Ama, Kofi and Esi each owe GHS 50.00.

\- Ama and Kofi pay GHS 50.00; Esi pays GHS 30.00.

\- Closing the week is refused because Esi owes GHS 20.00.

\- Esi pays the remaining GHS 20.00.

\- Ama receives a recorded payout of GHS 150.00.

\- Week 2 begins with Kofi next.



\## Project files



\- `susu.py`: group rules, money handling, reports and demonstration.

\- `main.py`: interactive text menu.

\- `test\_susu.py`: automated tests.

\- `NOTES.md`: assumptions, decisions and possible improvements.



\## Money handling



Amounts are read using Python's Decimal type, then stored as integer

pesewas. For example, GHS 50.00 is stored as 5000 pesewas.

Calculations do not use floating-point money values.



See NOTES.md for the project's assumptions and limitations.

