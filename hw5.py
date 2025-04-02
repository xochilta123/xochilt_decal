# 1. pwd
# 2. ls
# 3. cd brianna_decal, git pull origin main
#4. 1) cd.. 2) cp -r homework.py ../brianna_decal
# 5. cat homework.py
#6. nano homework.py
#7 . git add homework.py, git commit -m "homework.py changes", git push origin main
#8
#2 HW3 F review
#2.1 
#def checkdatatype(input_data):
   # return type(input_data)._name_
#2.2
def checkEvenOdd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
print(checkEvenOdd(2))
print(checkEvenOdd(7))
#2.3
def sumofintegers(int_list):
    total = 0
    for num in int_list:
        total += num
    return total
print(sumofintegers([1,2,3,4]))