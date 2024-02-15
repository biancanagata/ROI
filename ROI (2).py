#!/usr/bin/env python
# coding: utf-8

# In[1]:


class RentalPropertyCalculator:
    def __init__(self):
        self.income = {}
        self.expenses = {}
        self.cash_flow = {}
        self.roi = {}

    def get_income(self):
        print("Enter rental property income categories and amounts:")
        self.income['rental_income'] = float(input("Rental Income: $"))
        self.income['laundry_income'] = float(input("Laundry Income: $"))
        self.income['storage_income'] = float(input("Storage Income: $"))
        self.income['misc_income'] = float(input("Miscellaneous Income: $"))

    def get_expenses(self):
        print("\nEnter rental property expenses categories and amounts:")
        self.expenses['tax'] = float(input("Property Tax: $"))
        self.expenses['insurance'] = float(input("Insurance: $"))
        self.expenses['electricity'] = float(input("Electricity: $"))
        self.expenses['gas'] = float(input("Gas: $"))
        self.expenses['water'] = float(input("Water: $"))
        self.expenses['garbage'] = float(input("Garbage: $"))
        self.expenses['misc_expenses'] = float(input("Miscellaneous Expenses: $"))
        self.expenses['hoa'] = float(input("HOA Fees: $"))
        self.expenses['lawn_snow'] = float(input("Lawn/Snow Maintenance: $"))
        self.expenses['vacancy'] = float(input("Vacancy: $"))
        self.expenses['repairs'] = float(input("Repairs: $"))
        self.expenses['capex'] = float(input("Capital Expenditures: $"))
        self.expenses['property_mortgage'] = float(input("Property Mortgage: $"))
        self.expenses['mortgage'] = float(input("Additional Mortgage: $"))

    def calculate_annual_cash_flow(self):
        total_income = sum(self.income.values())
        total_expenses = sum(self.expenses.values())
        annual_cash_flow = total_income - total_expenses
        self.cash_flow['annual_cash_flow'] = annual_cash_flow

    def calculate_roi(self, total_investment):
        annual_cash_flow = self.cash_flow['annual_cash_flow']
        roi = (annual_cash_flow / total_investment) * 100
        self.roi['roi'] = roi


def main():
    rental_calculator = RentalPropertyCalculator()
    rental_calculator.get_income()
    rental_calculator.get_expenses()

    down_payment = float(input("\nEnter the down payment amount: $"))
    closing_costs = float(input("Enter the closing costs amount: $"))
    rehab_budget = float(input("Enter the rehab budget amount: $"))

    total_investment = down_payment + closing_costs + rehab_budget

    rental_calculator.calculate_annual_cash_flow()
    rental_calculator.calculate_roi(total_investment)

    print(f"\nAnnual Cash Flow: ${rental_calculator.cash_flow['annual_cash_flow']}")
    print(f"ROI: {rental_calculator.roi['roi']:.2f}%")


if __name__ == "__main__":
    main()


# In[ ]:




