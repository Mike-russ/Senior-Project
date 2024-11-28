import matplotlib.pyplot as plt

def plot_monthly_balance(months, balances):
    plt.figure(figsize=(10, 6))  # Set the figure size
    
    colors = ['green' if balance >= 0 else 'red' for balance in balances]
    plt.bar(months, balances, color=colors)
    
    plt.title('Monthly Balance Overview', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Balance', fontsize=12)
    plt.xticks(rotation=45)

    # Set dynamic y-axis limits with padding
    min_balance = min(balances)
    max_balance = max(balances)
    plt.ylim(min_balance - (0.1 * abs(min_balance)), max_balance + (0.1 * abs(max_balance)))

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.axhline(0, color='black', linewidth=1, linestyle='-')

    for i, balance in enumerate(balances):
        plt.text(i, balance + 50, str(balance), ha='center')

    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()


def plot_income(months, incomes):
    plt.figure(figsize=(10, 6))
    
    plt.bar(months, incomes, color='blue')
    
    plt.title('Monthly Income Overview', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Total Income', fontsize=12)
    plt.xticks(rotation=45)

    # Set dynamic y-axis limits with padding
    min_income = min(incomes)
    max_income = max(incomes)
    plt.ylim(min_income - (0.1 * abs(min_income)), max_income + (0.1 * abs(max_income)))

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    for i, income in enumerate(incomes):
        plt.text(i, income + 50, str(income), ha='center')

    plt.tight_layout()
    plt.show()

def plot_spending(spending_types, spendings):
    plt.figure(figsize=(10, 6))
    
    plt.bar(spending_types, spendings, color='orange')
    
    plt.title('Spending Overview by Type for Selected Month', fontsize=16)
    plt.xlabel('Spending Type', fontsize=12)
    plt.ylabel('Total Spending', fontsize=12)
    plt.xticks(rotation=45)

    # Set dynamic y-axis limits with padding
    min_spending = min(spendings)
    max_spending = max(spendings)
    plt.ylim(min_spending - (0.1 * abs(min_spending)), max_spending + (0.1 * abs(max_spending)))

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    for i, spending in enumerate(spendings):
        plt.text(i, spending + 50, str(spending), ha='center')

    plt.tight_layout()
    plt.show()

def plot_time_comparison(initial_amount, time_to_payoff, time_to_save, payment, interestRate):
    months = range(1, max(time_to_payoff, time_to_save) + 1)

    # Calculate the remaining loan balance over time
    remaining_balance = [
        initial_amount * ((1 + interestRate / 12) ** month) - payment * month for month in months
    ]
    
    # Calculate savings amount starting from the goal and decreasing
    saving_amount = [initial_amount - payment * month for month in months]

    plt.figure(figsize=(12, 6))

    # Plot remaining loan balance
    plt.plot(months, remaining_balance, label='Remaining Loan Balance', color='blue', marker='o')
    
    # Plot decreasing savings
    plt.plot(months, saving_amount, label='Savings Remaining', color='orange', marker='x')

    # Add horizontal line at zero for reference
    plt.axhline(y=0, color='black', linewidth=0.8)
    
    # Mark when the loan is paid off
    plt.axvline(x=time_to_payoff, color='blue', linestyle='--', label='Loan Paid Off')

    # Mark when savings reach zero
    plt.axvline(x=time_to_save, color='orange', linestyle='--', label='Savings Goal Reached')

    plt.title('Remaining Loan Balance vs. Savings Over Time')
    plt.xlabel('Months')
    plt.ylabel('Amount ($)')
    plt.ylim(-initial_amount * 0.1, initial_amount * 1.1) 
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Show the graph
    plt.show()

# def plot_expenses(months, spend):
#     plt.bar(months, spend)

#     plt.title('Monthly Expenses Overview', fontsize=16)
#     plt.xlabel('Month', fontsize=12)
#     plt.ylabel('Category', fontsize=12)
#     plt.xticks(rotation=45)

#     min_balance = min(spend)
#     max_balance = max(spend)
#     plt.ylim(min_balance - (0.1 * abs(min_balance)), max_balance + (0.1 * abs(max_balance)))

#     plt.grid(axis='y', linestyle='--', alpha=0.7)
#     plt.axhline(0, color='black', linewidth=1, linestyle='-')

#     for i, spend in enumerate(spend):
#         plt.text(i, spend + 50, str(spend), ha='center')

#     plt.tight_layout()
#     plt.show()