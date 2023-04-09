from recursive_solution import T as recursive_function
from dp_solution import T as dp_function
from dp_solution import output_solution, find_chosen_segments, print_table
import time
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def generate_tree(n):
    tree = [None]
    for _ in range(n):
        tree.append(random.randint(1, 50))
    return tree

def quadratic_regression(x, y):
    p = np.polyfit(x, y, 2)
    f = np.poly1d(p)
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, f(x))
    r_squared = r_value ** 2
    
    return r_squared

    

def main():
    
    min_n = 2
    max_n = 35
    n_vals_recursive = range(min_n, max_n)
    recursive_times = []
    
    for n_val in n_vals_recursive:
        # Generate random tree
        tree = generate_tree(n_val)
        n = len(tree) - 1
        
        print("\n-----------------")
        print("n_val:", n_val)
        print("-----------------\n")
        
        print("\nRecursive Solution: ", end="")
        start_time = time.perf_counter()
        print(recursive_function(1, n, tree))
        end_time = time.perf_counter()
        
        print(f"Executed in {end_time - start_time:.6f} seconds\n")
        recursive_times.append(end_time - start_time)
        
    print(n_vals_recursive)
    print(recursive_times)
    
    plt.plot(n_vals_recursive, recursive_times)
    plt.title("Recursive Algorithm Runtimes")
    plt.xlabel("n")
    plt.ylabel("Runtime")
    plt.show()
    
    min_n = 10
    max_n = 2000
    num_n = 50
    n_vals_dp = range(min_n, max_n, (max_n - min_n) // num_n)
    dp_times = []
    
    for n_val in n_vals_dp:
        # Generate random tree
        tree = generate_tree(n_val)
        n = len(tree) - 1
        
        print("\n-----------------")
        print("n_val:", n_val)
        print("-----------------\n")
        
        print("DP Solution: ", end="")
        start_time = time.perf_counter()
        print(dp_function(tree)[0][0][n-1])
        end_time = time.perf_counter()
        print(f"Executed in {end_time - start_time:.6f} seconds\n")
        dp_times.append(end_time - start_time)

    plt.plot(n_vals_dp, dp_times)
    plt.title("DP Algorithm Runtimes")
    plt.xlabel("n")
    plt.ylabel("Runtime")
    plt.show()
    
    r_squared = quadratic_regression(n_vals_recursive, recursive_times)
    print("Recursive R-squared value:", r_squared)
    
    r_squared = quadratic_regression(n_vals_dp, dp_times)
    print("DP R-squared value:", r_squared)
    
    

    
    # tree = [None, 33, 28, 35, 25, 29, 34, 28, 32, 33, 28, 35, 25, 29, 34, 28, 32]
    # n = len(tree) - 1
    
    # print("\nRecursive Solution: ", end="")
    # start_time = time.perf_counter()
    # print(recursive_function(1, n, tree))
    # end_time = time.perf_counter()
    
    # print(f"Executed in {end_time - start_time:.6f} seconds\n")
    
    # print("DP Solution: ", end="")
    # start_time = time.perf_counter()
    # print(dp_function(tree)[0][0][n-1])
    # end_time = time.perf_counter()
    # print(f"Executed in {end_time - start_time:.6f} seconds\n")
    
def test():
    tree = generate_tree(1000)
    
    start = time.perf_counter()
    # Solve and print solution
    dp_table = dp_function(tree)
    
    # Print out the traceback 
    sequence = find_chosen_segments(tree, dp_table[1][:][:])
    output_solution(tree, dp_table, sequence)
    
    end = time.perf_counter()
    
    print(f"Runtime: {end - start}")
    

if __name__ == "__main__":
    # main()
    test()