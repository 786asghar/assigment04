
import random 


N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100


def main():
    print("This program generates random numbers :")
    print(" Generate and print N_NUMBERS random numbers between MIN_VALUE and MAX_VALUE")

    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=' ')
if __name__ == '__main__':
    main()