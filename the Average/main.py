def calculate_average(numbers):
    total_sum = sum(numbers)  
    average = total_sum / len(numbers) 
    return average

numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print("The average is:", result)
