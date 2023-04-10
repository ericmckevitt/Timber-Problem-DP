def print_table(table: list[list[int]]) -> None:
    for row in table:
        for col in row:
            print(f"{col}", end="\t")
        print()

def T(tree: list) -> list[list[int]]:
    
    # number of segments
    n = len(tree) - 1
    
    # Create dp table i rows by j columns
    dp_table = [[0 for _ in range(n) ] for _ in range(n) ]
        
    # loop over the table diagonally
    for l in range(1, n+1):  # l is length of subproblem, which increases by one each iteration
        for i in range(n - l + 1): # i is the starting index of the subproblem in the current iteration
            # j is the ending index of the subproblem in the current iteration
            j = i + l - 1
            
            # Base case 1: l_i if i == j
            if i == j:
                dp_table[i][j] = tree[i + 1] # +1 bc 1-indexed
                continue
                
            # Base case 2: max(l_i, l_j) if j = i + 1 
            if j == i + 1:
                dp_table[i][j] = max(tree[i + 1], tree[j + 1])
                continue
            
            # Recurrence relation
            i_choice = tree[i+1] + min(dp_table[i+2][j], dp_table[i+1][j-1])
            j_choice = tree[j+1] + min(dp_table[i+1][j-1], dp_table[i][j-2])
            dp_table[i][j] = max(i_choice, j_choice)
            
    return dp_table

tree = [None, 6, 5, 7, 6, 4]
dp_table = T(tree)
print_table(dp_table)