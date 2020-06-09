starting_salary = float(input("Enter the starting salary: "))

def savings(salary, saving_percent, months_saved):
    current_savings = 0
    r = 0.04
    months = 0
    semi_annual_raise = 0.07

    while months < months_saved:
        months += 1
        current_savings += ((current_savings*r)/12)
        current_savings += (salary/12)*saving_percent
        if months % 6 == 0:
            salary += salary*semi_annual_raise

    return current_savings

def calculate_saving_rate(starting_salary): 
    portion_down_payment = 0.25
    savings_error_allowance = 100
    house_price = 1000000
    target_months = 36
    # to be divided by 10000 to get decimal representation
    saving_rate_low = 1
    saving_rate_high = 10000

    bisection_search_steps = 0
    guess_savings = 0

    while abs(guess_savings - house_price*portion_down_payment) > savings_error_allowance:
        if savings(starting_salary, saving_rate_high/10000, target_months) < house_price*portion_down_payment - 100:
            print("It is not possible to pay the down payment in three years.")
            return
        bisection_search_steps += 1

        guess_rate = (saving_rate_high + saving_rate_low)/2
        guess_savings = savings(starting_salary, guess_rate/10000, target_months)
        if guess_savings < house_price*portion_down_payment - savings_error_allowance:
            saving_rate_low = guess_rate
        elif guess_savings > house_price*portion_down_payment + savings_error_allowance:
            saving_rate_high = guess_rate
    
    print("Best savings rate:",guess_rate/10000)
    print("Steps in bisection search:", bisection_search_steps)

calculate_saving_rate(starting_salary)