# Funzione per verificare se un numero è primo
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Scrivi i numeri primi in un file
with open('results.txt', 'w') as f:
    for num in range(1, 251):
        if is_prime(num):
            f.write(f"{num}\n")

# Stampa i numeri primi sulla console
with open('results.txt', 'r') as f:
    print(f.read())
