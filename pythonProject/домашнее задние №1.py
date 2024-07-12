
monday = int(input('how much do you spend on monday?'))
tuesday = int(input('how much do you spend on tuesday?'))
wendsday = int(input('how much do you spend on wendsday?'))
thursday = int(input('how much do you spend on thursday?'))
friday = int(input('how much do you spend on friday?'))
saturday = int(input('how much do you spend on saturday?'))
sunday = int(input('how much do you spend on sunday?'))
sum_per_week = monday + tuesday + wendsday + thursday + friday + saturday + sunday
day_amount = 7
average_sum = sum_per_week / day_amount
average_sum = round(average_sum, 1)
print(f'sum_per_week:{sum_per_week} , average_sum:{average_sum}')
