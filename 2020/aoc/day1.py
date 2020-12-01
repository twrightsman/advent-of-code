def day1_part1(expense_report: str) -> str:
    expenses = {int(expense_line.rstrip()) for expense_line in expense_report.split("\n") if expense_line}
    expense_diffs = [2020 - expense for expense in expenses]
    for expense_diff in expense_diffs:
        if expense_diff in expenses:
            return str(expense_diff * (2020 - expense_diff))

