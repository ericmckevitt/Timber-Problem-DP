

# def T(i: int, j: int) -> int:
    
#     # Use lambda function to set values to None where i > j
#     valid_cell = lambda i, j: None if i > j else False
    
#     # Create dp table i rows by j columns
#     dp_table = [[valid_cell(row, col) for col in range(j) ] for row in range(i) ]
    
#     for row in dp_table:
#         print(row)

# tree = [None, 5, 6, 9, 7]
tree = [None, 6, 5, 7, 6, 4]
n = len(tree) - 1

def print_table(table):
    for row in table:
        for col in row:
            print(f"{col}", end="\t")
        print()

def T(i: int, j: int) -> int:
    
    # Use lambda function to set values to None where i > j
    valid_cell = lambda i, j: None if i > j else False
    
    # Create dp table i rows by j columns
    dp_table = [[0 for _ in range(n) ] for _ in range(n) ]
    
    # Apply the lambda function to each index of the dp_table
    for row in range(n):
        for col in range(n):
            dp_table[row][col] = valid_cell(row, col)
            
    # Apply base cases
    for row in range(n):
        for col in range(n):
            
            # Base case 1:
            if row == col:
                dp_table[row][col] = tree[row + 1] # +1 bc 1-indexed
                
            # Base case 2: 
            if col == row + 1:
                dp_table[row][col] = max(tree[row + 1], tree[col + 1])
    
    print_table(dp_table)
    
T(5, 5)