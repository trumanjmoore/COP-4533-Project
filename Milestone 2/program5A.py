
from typing import List, Tuple

    
def program5A(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 5A
    
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
    costs = {} # stores already seen subproblems, used for memoization

    def min_cost(p):
        if p == 0:
            return 0, 0, [] # base case, returns a lists with no paintings

        if p in costs:
            return costs[p]  # if the subproblem has already been seen, return the stored value

        num_platforms_p = 0  # number of platforms used
        platform_paintings_p = []  # number of paintings on each platform
        platform_height = 0  # height of the tallest painting on the platform
        curr_width = 0  # width of the platform
        min_cost_p = float('inf')  # the minimum cost for this index p

        # go through all possible permutations of paintings and platforms
        for j in range(p, 0, -1):
            curr_width += widths[j - 1]  # add the width of painting
            platform_height = max(platform_height, heights[j - 1])  # get the tallest painting on the platform

            if curr_width > W:
                break  # if the platform width is greater that the max width, the configuration is not possible

            # add this platforms cost to the cost of paintings before this platform to get the total cost so far
            prev_num_platforms, prev_cost, prev_platform_paintings = min_cost(j - 1)
            curr_cost = prev_cost + platform_height
            curr_num_platforms = prev_num_platforms + 1
            curr_platform_paintings = prev_platform_paintings + [p - j + 1]  # Number of paintings on the new platform

            # if this cost is less that the min cost so far, update the minimum seen value
            if curr_cost < min_cost_p:
                min_cost_p = curr_cost
                num_platforms_p = curr_num_platforms
                platform_paintings_p = curr_platform_paintings

        # store the values in the memoization list
        costs[p] = (num_platforms_p, min_cost_p, platform_paintings_p)
        return costs[p]

    # starting at n, recursively find the min cost of all permutations of paintings
    num_platforms, final_min_cost, platform_paintings = min_cost(n)
    return num_platforms, final_min_cost, platform_paintings


if __name__ == '__main__':
    # n, W = map(int, input().split())
    # heights = list(map(int, input().split()))
    # widths = list(map(int, input().split()))
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program5A(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)
    