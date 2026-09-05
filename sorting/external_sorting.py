# External sort algorithm (class example adapted to handlers)

## Function for counting the records in a file
## @params: archive
## @return: total
def count_regs(archive):
    total = 0
    with open(archive, 'r', encoding='utf-8') as file:
        for _ in file:
            total += 1
    return total


## Function for searching the minimum non-used record
## @params: archive, index
## @return: minimum record
def search_minimum_non_used(archive, index):
    minimum = None

    with open(archive, 'r', encoding='utf-8') as file:
        for line in file:
            field = line.strip().split(',')

            if field[0] == "1":
                continue

            value = field[index]
            try:
                value = int(value)
            except ValueError:
                pass

            if minimum is None or value < minimum[1]:
                minimum = (field, value)

    return minimum[0] if minimum else None


## Function for marking a record as used
## @params: archive, id_reg
## @return: None
def mark_as_used(archive, id_reg):
    new_lines = []
    with open(archive, 'r', encoding='utf-8') as file:
        for line in file:
            field = line.strip().split(',')
            if field[1] == id_reg:
                field[0] = "1"
            new_lines.append(','.join(field))

    with open(archive, 'w', encoding='utf-8') as file:
        for line in new_lines:
            file.write(line + '\n')


## Function for ordering a file using external sorting.
## The input file has the format: <control>,<id>,<fields...>
## @params: archive_input, archive_output, index
## @return: None
def organize_external(archive_input, archive_output, index):
    total_regs = count_regs(archive_input)
    with open(archive_output, 'w', encoding='utf-8') as output_file:
        for _ in range(total_regs):
            min_reg = search_minimum_non_used(archive_input, index)
            if min_reg is None:
                break
            output_file.write(','.join(min_reg) + '\n')

            mark_as_used(archive_input, min_reg[1])