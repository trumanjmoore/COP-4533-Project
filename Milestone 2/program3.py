
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

    
    memo_table = {} # store results of subproblems in a dictionary


    def min_height(idx: int, remaining_width: int, platforms: List[int], platform_counts: List[int]) -> Tuple[int, int, List[int]]:
        
        if idx == n: # base case - all paintings placed
            return len(platforms), sum(platforms), platform_counts
        

        # check if this state has been memo_tableized
        state = (idx, remaining_width, tuple(platforms)) 
        if state in memo_table:
            return memo_table[state]
        

        # option 1 - place the current painting on a new platform
        new_platforms = platforms + [heights[idx]]
        new_counts = platform_counts + [1]  # New platform with 1 painting
        platforms_used, total_height, arrangement = min_height(idx + 1, W - widths[idx], new_platforms, new_counts)

        
        # option 2 - try to add the painting to an existing platform if possible
        if platforms and widths[idx] <= remaining_width: # check if painting can be added to the last platform
            alt_platforms = platforms[:]
            alt_platforms[-1] = max(alt_platforms[-1], heights[idx])
            alt_counts = platform_counts[:]
            alt_counts[-1] += 1  # increment the painting count on the current platform

            new_platforms_used, new_total_height, new_arrangement = min_height(idx + 1, remaining_width - widths[idx], alt_platforms, alt_counts)

            # update if this configuration provides a better minimum height
            if new_total_height < total_height or (new_total_height == total_height and new_platforms_used < platforms_used):
                platforms_used, total_height, arrangement = new_platforms_used, new_total_height, new_arrangement

      
        # store the result in memoization table
        memo_table[state] = (platforms_used, total_height, arrangement)
        return memo_table[state]

    # start recursion with the first painting and empty platform setup
    total_platforms, total_height, num_paintings = min_height(0, W, [], [])
    return total_platforms, total_height, num_paintings


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))
    m, total_height, num_paintings = program3(n, W, heights, widths)
    print(m)
    print(total_height)
    for count in num_paintings:
        print(count)


"""
Algorithm3 explores all possible ways to arrange the paintings onto platforms 
while respecting the width constraint - using recursion and memoization to optimize 
the total height. It considers each painting either on a new platform or added 
to an existing platform and finds the configuration that minimizes the total height.
The time complexity is Θ(n⋅2^(n-1)) due to the recursive evaluation of subsets.
"""
