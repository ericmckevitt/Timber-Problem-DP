# Add None so that it is 1-indexed, as requested by problem definition.
# tree = [None, 33, 28, 35, 25, 29, 34, 28, 32, 33, 100, 35, 25, 29, 34, 28, 32]

# Recursive solution
def T(i: int, j: int, tree) -> int:
    
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
    
    # Consider both choices, and the opponent's response
    choose_i: int = tree[i] + min( T(i + 2, j, tree), T(i + 1, j - 1, tree) )
    choose_j: int = tree[j] + min( T(i + 1, j - 1, tree), T(i, j - 2, tree) )
    
    return max(choose_i, choose_j)

def main():
    tree = [None, 33, 28, 35, 25, 29, 34, 28, 32, 33, 100, 35, 25, 29, 34, 28, 32]
    n = len(tree) - 1
    result = T(1, n, tree)
    print(result)
    
    # print( 2 ** (n - 1) )

if __name__ == "__main__":
    main()