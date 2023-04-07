tree = [None, 6, 5, 7, 6, 4]
n = len(tree) - 1

def print_table(table):
    for row in table:
        for col in row:
            print(f"{col}", end="\t")
        print()

def T(i: int, j: int) -> int:
    
    # Create dp table i rows by j columns
    dp_table = [[0 for _ in range(n) ] for _ in range(n) ]
        
    # loop over the table from bottom row to top row
    for i in range(n - 1, -1, -1):
        for j in range(n):
            
            # i must be less than j
            if i > j:
                continue
            
            # Base case 1: l_i if i == j
            if i == j:
                dp_table[i][j] = tree[i + 1] # +1 bc 1-indexed
                continue
                
            # Base case 2: max(l_i, l_j) if j = i + 1 
            if j == i + 1:
                dp_table[i][j] = max(tree[i + 1], tree[j + 1])
                continue
            
            # Recurrence relation
            dp_table[i][j] = max(tree[i+1] + min(dp_table[i+2][j], dp_table[i+1][j-1]),
                                        tree[j+1] + min(dp_table[i+1][j-1], dp_table[i][j-2]))
            
        print()
    print_table(dp_table)
    print()
    
T(5, 5)