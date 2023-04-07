# Add None so that it is 1-indexed, as requested by problem definition.
tree = [None, 5, 6, 9, 7]
# tree = [None, 6, 5, 7, 6, 4]

# Monitor the sequence of indices that were chosen from the tree
sequence = []

# Recursive solution
def T(i: int, j: int) -> int:
    print("recursive call made")
    
    # If there is only one piece left
    if j == i: 
        # I take it
        return tree[i]
    
    # If there are two pieces left
    if j == i + 1:
        # Break ties by choosing i
        if tree[i] == tree[j]:
            return tree[i]
        
        # I take whichever is biggest
        return max([tree[i], tree[j]])
    
    # Consider opponent moves
    choose_i: int = tree[i] + min( T(i + 2, j), T(i + 1, j - 1) )
    choose_j: int = tree[j] + min( T(i + 1, j - 1), T(i, j - 2) )
    
    return max(choose_i, choose_j)

def main():
    n = len(tree) - 1
    result = T(1, n)
    print(result)
    print(sequence)

if __name__ == "__main__":
    main()