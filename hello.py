# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Main function
def main():
    print("Welcome to the Rectangle Area Calculator!")
    
    # Input length and width from the user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # Calculate the area
    area = calculate_area(length, width)
    
    # Display the result
    print(f"The area of the rectangle is: {area} square units")

# Execute the main function
if __name__ == "__main__":
    main()

