for i in range(1, 101):
    if not i % 3 == 0 and not i % 5 == 0:
        print(i)
    if i % 3 == 0:
        print('Fizz')
    if i % 5 == 0:
        print('Buzz')
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
