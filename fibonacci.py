import math

def fibonacci():
    while True:
        try:
            n = int(input("Masukkan jumlah suku Fibonacci yang diinginkan: "))
            if n <= 0:
                print("Mohon masukkan angka positif!")
                continue
            break
        except ValueError:
            print("Mohon masukkan angka yang valid!")
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    print(f"Deret Fibonacci sampai suku ke-{n}:")
    print(fib)

def main():
    fibonacci()
        

if __name__ == "__main__":
    print("Selamat datang di Program Python!")
    main()
