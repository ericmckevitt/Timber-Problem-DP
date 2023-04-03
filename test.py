from typing import List, Tuple

# Add None so that it is 1-indexed, as requested by problem definition.
tree = [None, 5, 6, 9, 7]

# Monitor the sequence of indices that were chosen from the tree
sequence = []

def T(i: int, j: int) -> Tuple[int, List[int]]:
    if j == i:
        return tree[i], [i]
    
    if j == i + 1:
        if tree[i] > tree[j]:
            return tree[i], [i]
        else:
            return tree[j], [j]
    
    choose_i_val, choose_i_seq = T(i + 2, j)
    choose_j_val, choose_j_seq = T(i + 1, j - 1)
    
    choose_i = tree[i] + min(choose_i_val, choose_j_val)
    choose_j = tree[j] + min(choose_j_val, choose_i_val)
    
    if choose_i > choose_j:
        return choose_i, [i] + (choose_i_seq if choose_i_val < choose_j_val else choose_j_seq)
    else:
        return choose_j, [j] + (choose_j_seq if choose_j_val < choose_i_val else choose_i_seq)

def main():
    n = len(tree) - 1
    result, sequence = T(1, n)
    print(result)
    print(sequence)

if __name__ == "__main__":
    main()
