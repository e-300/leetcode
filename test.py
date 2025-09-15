def fibonacci_generator():
    print("Generator started")
    a, b = 0, 1
    yield a
    print("After first yield")
    yield b
    print("After second yield")
    
    while True:
        a, b = b, a + b
        print(f"Computing next: {a}")
        yield a

def process_fibonacci(gen, limit):
    result = []
    for num in gen:
        if num > limit:
            break
        result.append(num)
        print(f"Added {num} to result")
    return result

# Test code
fib_gen = fibonacci_generator()
print("Created generator")
numbers = process_fibonacci(fib_gen, 5)
print(f"Final result: {numbers}")