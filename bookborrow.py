# Borrow records dictionary (name -> books borrowed)
borrow_records = {
    'Ajinkya': 3,
    'rehan': 0,
    'yash': 5,
    'raj': 2,
    'om': 0,
    'ayush': 5,
    'jay': 1
}

# Function to compute the average number of books borrowed
def compute_average(records):
    total = sum(records.values())
    count = len(records)
    return int(total / count)

# Function to find the max and min number of books borrowed (excluding 0 from min)
def find_max_min(records):
    non_zero_values = [val for val in records.values() if val > 0]
    max_borrow = max(non_zero_values)  # Exclude 0 from max
    min_borrow = min(non_zero_values)  # Exclude 0 from min
    return max_borrow, min_borrow

# Function to count how many members borrowed 0 books
def count_zero_borrowers(records):
    return list(records.values()).count(0)

# Function to find the most frequently borrowed book count (mode), excluding 0
def find_mode(records):

    from collections import Counter
    non_zero_values = [val for val in records.values() if val > 0]
    freq = Counter(non_zero_values)
    most_common = freq.most_common(1)[0][0]
    return most_common

# Display menu and handle user choices
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Compute average number of books borrowed")
        print("2. Find book with highest and lowest borrowings (excluding 0 from min)")
        print("3. Count members who have not borrowed any books")
        print("4. Most frequently borrowed book count (mode), excluding 0")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            average = compute_average(borrow_records)
            print("Average books borrowed:", average)
        
        elif choice == '2':
            max_borrow, min_borrow = find_max_min(borrow_records)
            print("Maximum books borrowed by any member:", max_borrow)
            print("Minimum books borrowed by any member (excluding zero):", min_borrow)
        
        elif choice == '3':
            zero_count = count_zero_borrowers(borrow_records)
            print("Members who borrowed 0 books:", zero_count)
        
        elif choice == '4':
            mode_borrow = find_mode(borrow_records)
            print("Most frequently borrowed count (mode, excluding zero):", mode_borrow)
        
        elif choice == '5':
            print("Exiting the program...")
            break  # Exit the program
            
        else:
            print("Invalid choice. Please try again.")

# Run the menu system
menu()
