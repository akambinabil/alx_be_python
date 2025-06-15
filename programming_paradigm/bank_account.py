# bank_account.py

class BankAccount:
    """
    Represents a bank account with deposit, withdrawal, and balance display functionalities.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new bank account.

        Args:
            initial_balance (float, optional): The initial balance of the account. Defaults to 0.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self._account_balance = initial_balance  # Using a convention for a "protected" attribute

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self._account_balance += amount
        print(f"Deposited: ${amount:.2f}") # Formatting to two decimal places

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if funds are sufficient.

        Args:
            amount (float): The amount to withdraw. Must be positive.

        Returns:
            bool: True if withdrawal is successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if self._account_balance >= amount:
            self._account_balance -= amount
            print(f"Withdrew: ${amount:.2f}") # Formatting to two decimal places
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """
        Displays the current balance of the account.
        """
        print(f"Current Balance: ${self._account_balance:.2f}") # Formatting to two decimal places

