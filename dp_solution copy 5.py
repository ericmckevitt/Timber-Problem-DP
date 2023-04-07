tree = [None, 6, 5, 7, 6, 4]
n = len(tree) - 1

def print_table(table):
    for row in table:
        for col in row:
            print(f"{col}", end="\t")
        print()

def traceback(dp_table, i, j) -> list[int]:
    if i > j: # no segments left
        return []
    if i == j: # one segment left, I pick it
        print(f"Last piece! I chose index {i+1}, which is {tree[i+1]}")
        return [i + 1]  # Add 1 to convert to 1-indexed
    if j == i + 1: # two segments left
        print(f"Last two! i: {i+1}, j: {j+1}. Corresponds to {tree[i + 1]}, {tree[j + 1]}")
        return [i + 1] if tree[i + 1] > tree[j + 1] else [j + 1]

    left_choice = tree[i + 1] + min(dp_table[i + 2][j], dp_table[i + 1][j - 1])
    right_choice = tree[j + 1] + min(dp_table[i + 1][j - 1], dp_table[i][j - 2])

    if left_choice >= right_choice:
        # I choose i
        my_choice = i
        
        # Check what piece opponent took 
        opp_i_choice = dp_table[i + 2][j]
        opp_j_choice = dp_table[i + 1][j - 1]
        
        if opp_i_choice >= opp_j_choice:
            # they chose new i 
            opp_choice = my_choice + 1
            print(f"I chose index {my_choice+1}, which is: {tree[my_choice+1]}")
            print(f"They chose index {opp_choice+1}, which is: {tree[opp_choice+1]}")
            return [my_choice+1, opp_choice+1] + traceback(dp_table, i+2, j)
        else:
            # they chose j
            opp_choice = j
            print(f"I chose index {my_choice+1}, which is: {tree[my_choice+1]}")
            print(f"They chose index {opp_choice+1}, whic is: {tree[opp_choice+1]}")
            return [my_choice+1, opp_choice+1] + traceback(dp_table, i+1, j-1)
    else:
        
        # I choose j
        my_choice = j
        
        # Check what piece opponent took 
        opp_i_choice = dp_table[i + 1][j - 1]
        opp_j_choice = dp_table[i][j - 2]
        
        if opp_i_choice >= opp_j_choice:
            # they chose i
            opp_choice = i
            return [my_choice+1, opp_choice+1] + traceback(dp_table, i+1, j-1)
        else:
            # they chose new j
            opp_choice = my_choice - 1
            return [my_choice+1, opp_choice+1] + traceback(dp_table, i, j-2)



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
print("Sequence of segments chosen by both players:", sequence)

