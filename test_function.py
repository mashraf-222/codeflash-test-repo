def slow_function(n):
    """A function that can be optimized"""
    result = 0
    for i in range(n):
        result += i * i
    return result

def main():
    print(slow_function(1000))

if __name__ == "__main__":
    main()
