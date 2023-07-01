# budget.py
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for transaction in self.ledger:
            description = transaction["description"][:23]
            amount = transaction["amount"]
            items += f"{description:<23}{amount:>7.2f}\n"
            total += amount
        output = title + items + f"Total: {total:.2f}"
        return output


def create_spend_chart(categories):
    # Calculate the percentage spent in each category
    total_withdrawals = sum(category.get_balance() for category in categories)
    percentages = [category.get_balance() / total_withdrawals * 100 for category in categories]

    # Create the horizontal axis labels
    axis_labels = ""
    for i in range(100, -10, -10):
        axis_labels += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                axis_labels += "o  "
            else:
                axis_labels += "   "
        axis_labels += "\n"

    # Create the category labels
    category_labels = ""
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        category_labels += " " * 5
        for category in categories:
            if i < len(category.name):
                category_labels += category.name[i] + "  "
            else:
                category_labels += "   "
        category_labels += "\n"

    # Create the title and combine all parts into the final chart
    title = "Percentage spent by category\n"
    chart = title + axis_labels + "    " + "-" * (3 * len(categories) + 1) + "\n" + category_labels

    return chart


# main.py
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())

clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
main(module='test_module', exit=False)
