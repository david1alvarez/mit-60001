annual_salary = float(input("enter your annual salary: "))
portion_saved = float(input("What portion are you saving? Please enter from 0 to 1 with 0 being 0% and 1 being 100%: "))
total_cost = float(input("What is your total budget for the house?: "))



def down_payment_months(salary, saving_percent, total):
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    months = 0

    while current_savings < (total * portion_down_payment):
        months += 1
        current_savings += ((current_savings*r)/12)
        current_savings += (salary/12)*saving_percent
    
    return months

print("You will need to save for", down_payment_months(annual_salary, portion_saved, total_cost), "months")