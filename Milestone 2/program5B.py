from typing import List, Tuple

def program5B(n: int, W: int, heights: List[int], widths: List[int]) -> Tuple[int, int, List[int]]:
    """
    Solution to Program 5B
    
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

    
    # DP array to store minimum height and where the split was made
    dp = [float('inf')] * (n + 1)  # dp[i] = min height required for first i paintings
    split_point = [-1] * (n + 1)   # split_point[i] = index where last platform starts
    dp[0] = 0  # base case: no paintings, zero height

    # prefix sums for width and height
    prefix_widths = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_widths[i] = prefix_widths[i - 1] + widths[i - 1]

    # bottom-up DP calculation
    for i in range(1, n + 1):
        max_height = 0

        # try placing a platform from j to i-1
        for j in range(i, 0, -1):
            max_height = max(max_height, heights[j - 1])  # max height for platform j to i-1
            platform_width = prefix_widths[i] - prefix_widths[j - 1]  # width from j to i-1
            if platform_width > W:
                break  # if width exceeds platform width, stop
            
            # Check if using platform j to i-1 gives a better solution
            if dp[j - 1] + max_height < dp[i]:
                dp[i] = dp[j - 1] + max_height
                split_point[i] = j - 1  # record where this platform starts

    # reconstruct the solution
    platforms = []
    i = n
    while i > 0:
        start = split_point[i]
        platforms.append(i - start)
        i = start

    platforms.reverse()  # reverse to get the order from left to right

    return len(platforms), dp[n], platforms


if __name__ == '__main__':
    n, W = map(int, input().split())
    heights = list(map(int, input().split()))
    widths = list(map(int, input().split()))

    m, total_height, num_paintings = program5B(n, W, heights, widths)

    print(m)
    print(total_height)
    for i in num_paintings:
        print(i)


"""
Algorithm5B uses dynamic programming to find the minimum total height for arranging
paintings on platforms with a fixed width constraint. By calculating the minimum
height for each subarray of paintings from 0 to i, it tracks the optimal splits 
for each platform configuration. This process ensures minimal height while respecting 
width constraints. The complexity is Θ(n^2) due to evaluating each subarray.
"""
