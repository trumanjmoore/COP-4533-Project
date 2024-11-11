from typing import List, Tuple

def program3(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 3
    
    Parameters:
    n (int): number of paintings
    W (int): width of the platform
    heights (List[int]): heights of the paintings
    widths (List[int]): widths of the paintings

    Returns:
    int: number of platforms used
    int: optimal total height
    List[int]: number of paintings on each platform
    """
    ############################
    # Add you code here
    ############################
    memo = {} # Memoization dictionary to store min height and platform configuration for subsets of paintings

    
    def get_feasible_subsets(): # Helper to get all subsets that fit within width W
        feasible_subsets = []
        for subset in range(1 << n):  # Generate all subsets using bitmasking; iterates from 0 to 2^n-1
            if subset == 0:
                continue  # Skip empty subset
            subset_width = sum(widths[i] for i in range(n) if subset & (1 << i))
            if subset_width <= W:
                feasible_subsets.append(subset)
        return feasible_subsets

    
   
    feasible_subsets = get_feasible_subsets() # Get feasible subsets of paintings


    def min_height(mask: int) -> Tuple[int, int, List[int]]: # Helper recursive function to find the minimum height arrangement

        if mask == 0:  # Base case: no paintings left for arrangement
            return (0, 0, [])

    
        if mask in memo:  # Check if result is already computed
            return memo[mask]
        
        min_platforms = float('inf')
        min_total_height = float('inf')
        best_arrangement = []

        for subset in feasible_subsets: # Try each feasible subset and calculate the result

            if (mask & subset) == subset:  # Ensure the subset is a part of the current mask
                remaining_mask = mask ^ subset  # Paintings left after placing this subset on a platform
                max_height_in_subset = max(heights[i] for i in range(n) if subset & (1 << i))
                
                # Recursive call
                platforms_used, height, arrangement = min_height(remaining_mask)
                platforms_used += 1
                height += max_height_in_subset

                if height < min_total_height or (height == min_total_height and platforms_used < min_platforms):
                    min_platforms = platforms_used
                    min_total_height = height
                    best_arrangement = [bin(subset).count('1')] + arrangement
                # Update minimum height and arrangement if this is the best found so far


        memo[mask] = (min_platforms, min_total_height, best_arrangement)
        return memo[mask] # Store the result in memo


    # Start the recursive function with all paintings
    total_mask = (1 << n) - 1  # Mask with all paintings included
    m, total_height, num_paintings = min_height(total_mask)
    return m, total_height, num_paintings


if __name__ == '__main__': # Main function
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))
    m, total_height, num_paintings = program3(n, W, heights, widths)
    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)


"""
Given the inputs n (number of paintings), W (width of the platform), heights (heights of the paintings), and widths (widths of the paintings),
program3 generates feasible subsets with bitmasking. 
Then, using a recursive function min_height we find the optimal arrangement of paintings on platforms with the total mask including all paintings.
"""
