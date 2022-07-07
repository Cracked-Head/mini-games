import sys
def collatz(num):
    if num%2 == 0:
        num //= 2
    else:
        num = num * 3 + 1
    return num
        
try:
    num = int(input('Enter a number: '))
except ValueError:
    print('Invalid Input')
    sys.exit()
while True:
    print(num)
    if num==1:
        sys.exit()
    num = collatz(num)
