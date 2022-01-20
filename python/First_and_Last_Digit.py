Test_case = int(input())
while Test_case >0:
    num = (input()) 
    reverse = num[::-1]
    reverse = int(reverse)
    num = int(num)
    first_digit = reverse % 10
    last_digit = num%10
    sum = first_digit + last_digit
    print(sum)
    Test_case = Test_case -1
    