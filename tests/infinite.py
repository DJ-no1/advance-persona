a = 1
while True:
    print(a)

    a += 1

    # Perform a CPU-intensive calculation to warm up the CPU
    x = 0
    for i in range(1000000):
        x += (i ** 2) % 1234567