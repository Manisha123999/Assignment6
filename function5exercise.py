def remove_odd_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original list:", numbers)
    even_numbers = remove_odd_numbers(numbers)
    print("Cut-down list (even numbers only):", even_numbers)

if __name__ == "__main__":
    main()