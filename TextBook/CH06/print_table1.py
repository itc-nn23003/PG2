def print_table(table_data):
    col_widths = [max(len(item) for item in column) for column in zip(*table_data)]
    
    for row in table_data:
        formatted_row = [item.rjust(col_widths[i]) for i, item in enumerate(row)]
        print(' '.join(formatted_row))

table_data = [
    ['apple', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

print_table(table_data)
