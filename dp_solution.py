# tree = [None, 5, 6, 9, 7]
tree = [None, 6, 5, 7, 6, 4]
n = len(tree) - 1

def print_table(table):
    for row in table:
        for col in row:
            print(f"{col}", end="\t")
        print()

def T(i: int, j: int) -> int:
    
    # Create dp table i rows by j columns
    dp_table = [[None for _ in range(n) ] for _ in range(n) ]
        
    # loop over the table from bottom row to top row
    for row in range(n - 1, -1, -1):
        for col in range(n):
            
            # i must be less than j
            if row > col:
                continue
            
            # Base case 1: l_i if i == j
            if row == col:
                dp_table[row][col] = tree[row + 1] # +1 bc 1-indexed
                continue
                
            # Base case 2: max(l_i, l_j) if j = i + 1 
            if col == row + 1:
                dp_table[row][col] = max(tree[row + 1], tree[col + 1])
                continue
            
            # Recurrence relation
            dp_table[row][col] = max(tree[row+1] + min(dp_table[row+2][col], dp_table[row+1][col-1]),
                                        tree[col+1] + min(dp_table[row+1][col-1], dp_table[row][col-2]))
            
        print()
    print_table(dp_table)
    print()
    
T(5, 5)