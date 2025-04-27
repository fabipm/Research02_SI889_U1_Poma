
accounts = {
    'alice': 1000,
    'bob': 500
}

def deposit(account_name, amount):
    if account_name not in accounts:
        raise ValueError("Account not found.")
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    accounts[account_name] += amount
    print(f"Deposited {amount} to {account_name}. New balance: {accounts[account_name]}")

def withdraw(account_name, amount):
    if account_name not in accounts:
        raise ValueError("Account not found.")
    if amount <= 0:
        raise ValueError("Amount must be positive.")
    if accounts[account_name] < amount:
        raise ValueError("Insufficient funds.")
    accounts[account_name] -= amount
    print(f"Withdrew {amount} from {account_name}. New balance: {accounts[account_name]}")

def main():
    deposit('alice', 200)
    withdraw('bob', 100)

if __name__ == "__main__":
    main()
