tree = [None, 6, 5, 7, 6, 4]
# tree = [None, 5, 6, 9, 7]
n = len(tree) - 1

def print_table(table):
    for row in table:
        for col in row:
            print(f"{col}", end="\t")
        print()

def traceback(dp_table, i, j) -> list[int]:
    if i > j:  # no segments left
        return []
    if i == j:  # one segment left, I pick it
        return [i + 1]  # Add 1 to convert to 1-indexed
    if j == i + 1:  # two segments left
        return [i + 1] if tree[i + 1] >= tree[j + 1] else [j + 1]

    left_choice = tree[i + 1] + min(dp_table[i + 2][j], dp_table[i + 1][j - 1])
    right_choice = tree[j + 1] + min(dp_table[i + 1][j - 1], dp_table[i][j - 2])

    if left_choice >= right_choice:
        # I choose i
        my_choice = i + 1

        # Check what piece opponent took after I made my choice
        opp_left_choice = dp_table[i + 2][j]
        opp_right_choice = dp_table[i + 1][j - 1]

        if opp_left_choice >= opp_right_choice:
            # They choose new i
            opp_choice = i + 2
            return [my_choice, opp_choice] + traceback(dp_table, i + 2, j)
        else:
            # They choose j
            opp_choice = j + 1
            return [my_choice, opp_choice] + traceback(dp_table, i + 1, j - 1)
    else:
        # I choose j
        my_choice = j + 1

        # Check what piece opponent took after I made my choice
        opp_left_choice = dp_table[i + 1][j - 1]
        opp_right_choice = dp_table[i][j - 2]

        if opp_left_choice >= opp_right_choice:
            # they choose i
            opp_choice = i + 1
            return [my_choice, opp_choice] + traceback(dp_table, i + 1, j - 1)
        else:
            # they choose new j
            opp_choice = j
            return [my_choice, opp_choice] + traceback(dp_table, i, j - 2)





def T(tree):
    
    n = len(tree) - 1
    
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
    
dp_table = T(tree)
sequence = traceback(dp_table, 0, n - 1)
print("Sequence of segments chosen by both players:", sequence)

