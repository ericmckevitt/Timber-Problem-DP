tree = [None, 6, 5, 7, 6, 4]
n = len(tree) - 1

def print_table(table):
    for row in table:
        for col in row:
            print(f"{col}", end="\t")
        print()
        
def traceback(dp_table, i, j):
    if i > j:
        return []
    if i == j:
        return [i + 1]  # Add 1 to convert to 1-indexed
    if j == i + 1:
        return [i + 1] if tree[i + 1] > tree[j + 1] else [j + 1]

    left_choice = tree[i + 1] + min(dp_table[i + 2][j], dp_table[i + 1][j - 1])
    right_choice = tree[j + 1] + min(dp_table[i + 1][j - 1], dp_table[i][j - 2])

    if left_choice > right_choice:
        return [i + 1] + traceback(dp_table, i + 2, j)
    else:
        return [j + 1] + traceback(dp_table, i, j - 2)


def T(i: int, j: int) -> int:
    
    # Create dp table i rows by j columns
    dp_table = [[0 for _ in range(n)] for _ in range(n)]
        
    # loop over the table diagonally
    for l in range(1, n+1):  # l is length of subproblem, which increases by one each iteration
        for i in range(n - l + 1): # i is the starting index of the subproblem in the current iteration
            # j is the ending index of the subproblem in the current iteration
            j = i + l - 1
            
            # Base cases
            if i == j:
                dp_table[i][j] = tree[i + 1] # +1 bc 1-indexed
            elif j == i + 1:
                dp_table[i][j] = max(tree[i + 1], tree[j + 1])
            else:
                # Recurrence relation
                dp_table[i][j] = max(tree[i+1] + min(dp_table[i+2][j], dp_table[i+1][j-1]),
                                        tree[j+1] + min(dp_table[i+1][j-1], dp_table[i][j-2]))
    
    print_table(dp_table)
    print()
    
    return dp_table
    
dp_table = T(5, 5)
sequence = traceback(dp_table, 0, n - 1)
print("Optimal sequence of segments:", sequence)
