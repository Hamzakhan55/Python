num = int(Input("Enter a number: "))

prime_num = [2, 3]


def all_prime_numbers(num):
    is_prime = True
    for i in range(3, num):
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_num.append(i)
