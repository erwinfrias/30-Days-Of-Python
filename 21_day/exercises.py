# =============================
# Exercises: Level 1
# =============================
from math import sqrt
from collections import Counter


class Statistics:
    def __init__(self, data):
        self.data = sorted(data)

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    # ---------- Central Tendency ----------
    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        return self.data[mid]

    def mode(self):
        freq = Counter(self.data).most_common(1)[0]
        return {"mode": freq[0], "count": freq[1]}

    # ---------- Variability ----------
    def var(self):
        mean = self.mean()
        return round(sum((x - mean) ** 2 for x in self.data) / self.count(), 1)

    def std(self):
        return round(sqrt(self.var()), 1)

    # ---------- Frequency Distribution ----------
    def freq_dist(self):
        total = self.count()
        freq = Counter(self.data)
        return [
            (round((count / total) * 100, 1), value)
            for value, count in freq.most_common()
        ]

    # ---------- Summary ----------
    def describe(self):
        return f"""Count: {self.count()}
        Sum:  {self.sum()}
        Min:  {self.min()}
        Max:  {self.max()}
        Range:  {self.range()}
        Mean:  {self.mean()}
        Median:  {self.median()}
        Mode:  ({self.mode()['mode']}, {self.mode()['count']})
        Variance:  {self.var()}
        Standard Deviation:  {self.std()}
        Frequency Distribution: {self.freq_dist()}"""

ages = [
    31, 26, 34, 37, 27, 26, 32, 32, 26, 27,
    27, 24, 32, 33, 27, 25, 26, 38, 37, 31,
    34, 24, 33, 29, 26
]

data = Statistics(ages)
print(data.describe())

# =============================
# Exercises: Level 2
# =============================

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}   # {description: amount}
        self.expenses = {}  # {description: amount}

    def add_income(self, description, amount):
        self.incomes[description] = self.incomes.get(description, 0) + amount

    def add_expense(self, description, amount):
        self.expenses[description] = self.expenses.get(description, 0) + amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f"""
        Account Holder: {self.firstname} {self.lastname}
        Total Income: {self.total_income()}
        Total Expense: {self.total_expense()}
        Account Balance: {self.account_balance()}
        """

person = PersonAccount("Erwin", "Frias")

person.add_income("Salary", 3000)
person.add_income("Freelance", 1200)

person.add_expense("Rent", 900)
person.add_expense("Groceries", 250)

print(person.account_info())