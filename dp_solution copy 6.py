from typing import List, Tuple


tree = [None, 6, 5, 7, 6, 4]
n = len(tree) - 1

def print_table(table):
    for row in table:
        for col in row:
            print(f"{col}", end="\t")
        print()

def traceback(dp_table: List[List[int]], tree: List[int]) -> List[Tuple[int, int]]:
    i, j = 1, len(tree) - 1
    choices = []

    while i <= j:
        if i == j:
            choices.append((i, tree[i]))
            break

        left_choice = tree[i] + min(dp_table[i+2-1][j] if i+2 <= j else 0, dp_table[i+1-1][j-1])
        right_choice = tree[j] + min(dp_table[i+1-1][j-1], dp_table[i][j-2-1] if j-2 >= i else 0)

        if left_choice >= right_choice:
            choices.append((i, tree[i]))
            i += 1

            # Next player's move
            if i+1 <= j and dp_table[i+1-1][j] < dp_table[i-1][j-1]:
                i += 1
            else:
                j -= 1

        else:
            choices.append((j, tree[j]))
            j -= 1

            # Next player's move
            if j-1 >= i and dp_table[i][j-1-1] < dp_table[i+1-1][j]:
                j -= 1
            else:
                i += 1

    return choices

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

print_table(dp_table)
# Call the traceback function with the dp_table and tree.
choices = traceback(dp_table, tree)

# Print the choices made by both parties.
# print("Choices: ", choices)

