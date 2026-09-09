# Direct merge sort for fixed-length direct-access files.
import os

# Configuration dictionary for each type of entity.
DIRECT_FIELD_CONFIG ={

    "clients": {
        "record_len": 60,
        "field_ranges": {
            "id": (1, 5),
            "name": (5, 35),
            "mail": (35, 55),
            "shop_id": (55, 59),
        },
        "field_types": {
            "id": "int",
            "name": "str",
            "mail": "str",
            "shop_id": "int",
        },
        "output_file": "Clients_direct_sorted.txt",
    },

    "users": {
        "record_len": 75,
        "field_ranges": {
            "id": (1, 5),
            "name": (5, 35),
            "mail": (35, 55),
            "rol": (55, 70),
            "shop_id": (70, 74),
        },
        "field_types": {
            "id": "int",
            "name": "str",
            "mail": "str",
            "rol": "str",
            "shop_id": "int",
        },
        "output_file": "Users_direct_sorted.txt",
    },

    "shops": {
        "record_len": 90,
        "field_ranges": {
            "id": (1, 5),
            "name": (5, 35),
            "description": (35, 85),
            "admin_user_id": (85, 89),
        },
        "field_types": {
            "id": "int",
            "name": "str",
            "description": "str",
            "admin_user_id": "int",
        },
        "output_file": "Shops_direct_sorted.txt",
    },
}


## Function for converting a string value to its corresponding type (int, float, or str)
## @params: value, field_type
## @return: the converted value (int, float, or str)
def _convert_value(value, field_type):
    text = str(value).strip()
    # If statement for checking the field type
    if field_type == "int":
        # Try/except for converting the text to an integer,
        # If it fails return 0
        try:
            return int(text)
        except ValueError:
            return 0
    # If statement for checking the field type
    if field_type == "float":
        # Try/except for converting the text to a float,
        # If it fails return 0.0
        try:
            return float(text)
        except ValueError:
            return 0.0
    return text


## Function for reading all valid (active) records from a direct-access file
## @params: archive (filename), record_len (length of each register)
## @return: list of valid register strings
def _read_valid_records(archive, record_len):
    # If statement for checking if the file exists
    if not os.path.exists(archive):
        raise FileNotFoundError(f"File {archive} does not exist.")

    with open(archive, 'r', encoding='utf-8') as file:
        content = file.read()

    # If statement for checking if the file is empty
    if not content:
        return []

    records = []
    # While loop for reading the entire file content,
    # Reading each register of length record_len
    for i in range(0, len(content), record_len):
        register = content[i:i + record_len]
        # If statement for checking if the register has the correct length
        if len(register) < record_len:
            continue
        # If statement for checking if the register is active (active flag = "0" means deleted)
        if register[0] == "0":
            continue
        records.append(register)

    return records


## Function for extracting the value of a specific field from a register
## @params: register (string), field_name, field_ranges (dict), field_types (dict)
## @return: the field value converted to its corresponding type
def _field_value(register, field_name, field_ranges, field_types):
    start, end = field_ranges[field_name]
    # Returns the value of the field in the register, converted to the correct type
    return _convert_value(register[start:end], field_types[field_name])


## Function for merging two sorted arrays of records into a single sorted array
## @params: left (sorted list), right (sorted list), field_name, field_ranges, field_types
## @return: merged sorted list of records
def _merge_direct(left, right, field_name, field_ranges, field_types):
    # Array to store the merged records
    merged = []
    # Indexes for the left and right arrays
    left_index = 0
    right_index = 0

    # While loop to merge the left and right arrays,
    # Comparing the values of the field_name
    while left_index < len(left) and right_index < len(right):
        left_value = _field_value(left[left_index], field_name, field_ranges, field_types)
        right_value = _field_value(right[right_index], field_name, field_ranges, field_types)

        # If statement to compare the values of the field_name,
        # And append the smaller one to the merged array
        if left_value <= right_value:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are any remaining records in the left array,
    # Append them to the merged array
    if left_index < len(left):
        merged.extend(left[left_index:])
    # If there are any remaining records in the right array,
    # Append them to the merged array
    if right_index < len(right):
        merged.extend(right[right_index:])

    return merged


## Function for sorting an array of records using direct merge sort algorithm
## @params: records (list), field_name, field_ranges, field_types
## @return: sorted list of records
def direct_merge_sort(records, field_name, field_ranges, field_types):
    # If statement for checking if the list has one or zero elements,
    # If so, return the records as they are already sorted
    if len(records) <= 1:
        return records
    # Split the records into two halves
    middle = len(records) // 2

    # Recursive call to direct_merge_sort on the left and right halves,
    # And merge the sorted halves using _merge_direct
    left = direct_merge_sort(records[:middle], field_name, field_ranges, field_types)
    right = direct_merge_sort(records[middle:], field_name, field_ranges, field_types)

    # Return the merged sorted records
    return _merge_direct(left, right, field_name, field_ranges, field_types)


## Function for reading valid records from an input file, sorting them, and writing to an output file
## @params: archive_input (input filename), archive_output (output filename),
##           field_name (field to sort by), record_len, field_ranges, field_types
## @return: list of sorted records
def organize_direct(archive_input, archive_output, field_name, record_len, field_ranges, field_types):
    # Read the valid records from the input file
    records = _read_valid_records(archive_input, record_len)
    # Sort the records using direct_merge_sort
    sorted_records = direct_merge_sort(records, field_name, field_ranges, field_types)

    with open(archive_output, 'w', encoding='utf-8') as output_file:
        # While loop for writing the sorted records to the output file
        for register in sorted_records:
            output_file.write(register)

    return sorted_records

# Functions for sorting each type of record using direct merge sort

## Function for sorting clients using direct merge sort
## @params: field_name (default "id")
## @return: sorted list of client records
def sort_clients_direct(field_name="id"):
    config = DIRECT_FIELD_CONFIG["clients"]
    return organize_direct(
        "Clients_direct.txt",
        config["output_file"],
        field_name,
        config["record_len"],
        config["field_ranges"],
        config["field_types"],
    )

## Function for sorting users using direct merge sort
## @params: field_name (default "id")
## @return: sorted list of user records
def sort_users_direct(field_name="id"):
    config = DIRECT_FIELD_CONFIG["users"]
    return organize_direct(
        "Users_direct.txt",
        config["output_file"],
        field_name,
        config["record_len"],
        config["field_ranges"],
        config["field_types"],
    )


## Function for sorting shops using direct merge sort
## @params: field_name (default "id")
## @return: sorted list of shop records
def sort_shops_direct(field_name="id"):
    config = DIRECT_FIELD_CONFIG["shops"]
    return organize_direct(
        "Shops_direct.txt",
        config["output_file"],
        field_name,
        config["record_len"],
        config["field_ranges"],
        config["field_types"],
    )

# We used return false at the end of an statement for close the process Con la logica de esta estructura de comentarios
