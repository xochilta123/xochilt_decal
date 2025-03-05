def compute_power(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1/ compute_power(x, -y)
    return x * compute_power(x, y - 1)
x = 2
y = 3
print(compute_power(x, y))
#problem 1
readings = [15, 14, 17, 20, 23, 28, 20]
def temperaturerange(readings):
    return(min(readings), max(readings))
print(temperaturerange(readings))
#problem 2
def weekend(day):
    return day == 6 or day == 7
day = 6 #saturday
print(weekend(day))
#problem 3
distance = 70
fuel = 21.5
def fuel_efficiency(distance, fuel):
    return round(distance / fuel, 2)
print(fuel_efficiency(distance, fuel))
#problem 4
nums = [2024, 98, 131, 2, 3, 72]
def minforloop(nums):
    min_value = nums[0]
    for num in nums:
        if num < min_value:
            min_value = num
    return min_value
def maxforloop(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value
print(minforloop(nums))
print(maxforloop(nums))