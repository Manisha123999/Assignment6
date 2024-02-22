def convert_to_liters(gallons):
    liters = gallons * 3.78541
    return liters

def main():
    while True:
        gallons = float(input("Enter the quantity of gasoline in gallons (negative value to exit): "))
        if gallons < 0:
            break
        liters = convert_to_liters(gallons)
        print("The quantity of gasoline in liters:", liters)

if __name__ == "__main__":
    main()