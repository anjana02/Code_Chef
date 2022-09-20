# Pooja would like to withdraw X Rupees from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 Rupees. Calculate Pooja's account balance after an attempted transaction.

# Input - Positive integer 0 < X <= 2000 - Positive float 0<= Y <= 2000 with two digits of precision

# Output - Output the account balance after the attempted transaction, given as a number with two digits of precision. If there is not enough money in the account to complete the transaction, output the current bank balance.

# Example - Input: 30 120.00 Output: 89.50 Input: 300 120.00 Output: 120.00

# Solution

x, y = map(float, input().split())
if x % 5 == 0 and x + 0.5 <= y:
    y -= x + 0.5
print('%.2f' % y)
    