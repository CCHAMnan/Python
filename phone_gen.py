smart = {
    "010": {"digit": 6, "length": 8},
    "015": {"digit": 6, "length": 8},
    "016": {"digit": 6, "length": 8},
    "069": {"digit": 6, "length": 8},
    "070": {"digit": 6, "length": 8},
    "081": {"digit": 6, "length": 8},
    "086": {"digit": 6, "length": 8},
    "087": {"digit": 6, "length": 8},
    "093": {"digit": 6, "length": 8},
    "096": {"digit": 7, "length": 9},
    "098": {"digit": 6, "length": 8},
}

# Initialize an empty list to store all possible numbers
all_possible_numbers = []

# Iterate through the dictionary
for key, value in smart.items():
    digit = value["digit"]
    length = value["length"]

    # Generate all possible combinations for the current entry with leading zeros
    possible_combinations = [str(i).zfill(digit) for i in range(10 ** digit)]

    # Append the possible combinations with the key prefix to the final list
    all_possible_numbers.extend([key + combo for combo in possible_combinations])

# # Print the first few numbers as an example
# for number in all_possible_numbers[:10]:
#     print(number)

with open("phone_numbers.txt", "w") as f:
    f.writelines("\n".join(all_possible_numbers))
