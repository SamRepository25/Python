# Import the sys module to work with command-line arguments
import sys

# Check if the user has entered at least one name
# If only the file name is present, display the usage message and exit
if len(sys.argv) == 1:
    print("Usage: python input_handling.py <Full Name>")
    sys.exit()

# Join all command-line arguments into a single full name
# Example:
# python input_handling.py B SIMAK AHMED
# full_name = "B SIMAK AHMED"
full_name = " ".join(sys.argv[1:])

# Convert the full name to lowercase
# Replace spaces with dots
# Append the company email domain
email = full_name.lower().replace(" ", ".") + "@company.com"

# Display the output
print("\n--- Your Profile ---")
print("Full Name:", full_name)
print("Generated Email:", email)


"""
Description:
This program accepts a user's full name from the command line
using the sys.argv list. It combines all the entered words
into a single full name, converts the name to lowercase,
replaces spaces with dots (.), and generates a company email
address by appending "@company.com".
"""