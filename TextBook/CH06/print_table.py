def print_table(table_data):
    num_rows = len(table_data)
    num_cols = len(table_data[0])

    col_widths = [0] * num_cols

    for col in range(num_cols):
        for row in range(num_rows):
            col_widths[col] = max(col_widths[col], len(table_data[row][col]))

    for row in table_data:
        formatted_row = [row[col].rjust(col_widths[col]) for col in range(num_cols)]
        print(' '.join(formatted_row))

table_data = [
    ['apple', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

print_table(table_data)
