# Function to generate admission slots for each year
def create_admission_slots(start_year, end_year):
    # List to store admission slots
    admission_slots = {}

    # Loop through each year from start_year to end_year
    for year in range(start_year, end_year + 1):
        slots = []
        
        # Add some sample months and dates for each year
        # In a real scenario, you could make this dynamic or based on real dates
        for month in ['January', 'February', 'March', 'April', 'May']:
            slots.append(f"{month} {year} - Slot Open")
        
        # Store the slots for the current year
        admission_slots[year] = slots
    
    return admission_slots

# Display the admission slots
def display_admission_slots(slots):
    for year, slots_list in slots.items():
        print(f"\nAdmission Slots for {year}:")
        for slot in slots_list:
            print(slot)

# Main function to run the program
if __name__ == "__main__":
    start_year = 2020
    end_year = 2024

    # Create admission slots
    slots = create_admission_slots(start_year, end_year)
    
    # Display the slots
    display_admission_slots(slots)
