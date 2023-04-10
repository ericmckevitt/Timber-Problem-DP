def print_table(table):
    for row in table:
        for col in row:
            print(f"{col}", end="\t")
        print()

def find_chosen_segments(traceback_matrix: list[list[int]]):
    n = len(traceback_matrix)
    chosen_segments = []
    i = 0
    j = n - 1

    while i <= j:
        # If the current value in the traceback matrix is 0, choose the left segment and increment i
        if traceback_matrix[i][j] == 0:
            chosen_segments.append(i + 1)  # +1 because tree is 1-indexed
            i += 1
        # If the current value in the traceback matrix is 1, choose the right segment and decrement j
        else:
            chosen_segments.append(j + 1)  # +1 because tree is 1-indexed
            j -= 1

    return chosen_segments

def T(tree):
    
    n = len(tree) - 1
    
    # Create dp table i rows by j columns. Index 0 is dp table, index 1 is traceback
    dp_table = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(2)]
        
    # loop over the table diagonally
    for l in range(1, n+1):  # l is length of subproblem, which increases by one each iteration
        for i in range(n - l + 1): # i is the starting index of the subproblem in the current iteration
            # j is the ending index of the subproblem in the current iteration
            j = i + l - 1
            
            # Base cases
            if i == j:
                dp_table[0][i][j] = tree[i + 1] # +1 bc tree is 1-indexed
                dp_table[1][i][j] = 0 # choose left if only one option
            elif j == i + 1:
                dp_table[0][i][j] = max(tree[i + 1], tree[j + 1])
                dp_table[1][i][j] = 0 if tree[i + 1] >= tree[j + 1] else 1
            else:
                # Recurrence relation
                left = tree[i+1] + min(dp_table[0][i+2][j], dp_table[0][i+1][j-1])
                right = tree[j+1] + min(dp_table[0][i+1][j-1], dp_table[0][i][j-2])
                dp_table[0][i][j] = max(left, right)

                # Traceback
                if left >= right:
                    dp_table[1][i][j] = 0
                else:
                    dp_table[1][i][j] = 1

    return dp_table

def output_solution(tree, dp_table, traceback_list):
    # Top right of dp_table is solution
    n = len(tree) - 2 # another -1 bc 1 indexed
    print(dp_table[0][0][n])
    for i, elem in enumerate(traceback_list):
        print(elem, end=" ") if i < len(traceback_list) - 1 else print(elem, end="\n")

def main():
    
    # Don't need the number of inputs
    # n_items = int(input().strip())
    # tree = [None]
    # second_line = input()
    # segments = second_line.split(" ")
    # segments = [seg for seg in segments if seg.strip()]  # filter out empty strings and spaces
    # for segment in segments: 
    #     tree.append(int(segment))
    
    tree = [None, 6, 5, 7, 6, 4]
    
    # Solve and print solution
    dp_table = T(tree)
    
    print_table(dp_table[1])
    
    # Print out the traceback 
    sequence = find_chosen_segments(dp_table[1][:][:])
    output_solution(tree, dp_table, sequence)


if __name__ == "__main__":
    main()