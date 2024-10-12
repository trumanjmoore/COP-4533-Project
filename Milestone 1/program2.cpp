#include <iostream>
#include <vector>
#include <tuple>
/* Solution to program 2
* @param n the number of paintings
* @param W the maximum width of the platform
* @param heights the heights of the paintings
* @param widths the widths of the paintings
* @return a tuple containing the number of platforms used, the optimal total height, and the number of paintings on each platform
*/
std::tuple<int, int, std::vector<int>> program2(int n, int W, std::vector<int> heights, std::vector<int> widths){
    int curr_width = 0; //keeps the width of the paintings on the current platform
    int cost = 0; // total cost
    int m = 1; // number of platforms
    int min_index = 0; // index of the local min
    std::vector<int> platform_paintings; //number of paintings on each platform
    for(int i = 0; i < n; i++){
        if(i != 0 && heights.at(i) > heights.at(i-1)){ //checks if this index is the local min
            min_index = i+1;
            m += 1;
            platform_paintings.push_back(1);
            curr_width = widths.at(i);
            break; //if it is the local min, break from the decreasing loop to go to the increasing loop
        }
        else if(curr_width + widths.at(i) > W){ //if adding the painting would go beyond the width
            m += 1;
            cost += heights.at(i); //because the paintings are decreasing in height, this will be the max for this platform
            curr_width = widths.at(i);
            platform_paintings.push_back(1);// create a new platform
        }
        else{
            if(i == 0){ //if this is the first painting
                cost += heights.at(i); //painting with the most height, so it is added to the cost
                platform_paintings.push_back(1);
            }
            else{
                platform_paintings.at(m-1)++; //increase the number of paintings on this platform
            }
            curr_width += widths.at(i);
        }
    }

    for(int i = min_index; i<n; i++){
        if(curr_width + widths.at(i) > W){ //if adding the painting would go beyond the width
            m += 1;
            cost += heights.at(i-1); //because the paintings are now increasing in height, the last painting will be the max for this platform
            curr_width = widths.at(i);
            platform_paintings.push_back(1); //create new platform
        }
        else{
            if(i == n-1){ //if this is the last painting
                cost += heights.at(i); //because heights have been increasing, will have the most height on its platform
                platform_paintings.at(m-1)++; //increase the number of paintings on this platform
            }
            else{
                platform_paintings.at(m-1)++; //increase the number of paintings on this platform
            }
            curr_width += widths.at(i);
        }
    }
    return std::make_tuple(m, cost, platform_paintings); // replace with your own result.
}
int main(){
    int n, W;
    std::cin >> n >> W;
    std::vector<int> heights(n);
    std::vector<int> widths(n);
    for(int i = 0; i < n; i++){
        std::cin >> heights[i];
    }
    for(int i = 0; i < n; i++){
        std::cin >> widths[i];
    }
    auto result = program2(n, W, heights, widths);

    std::cout << std::get<0>(result) << std::endl;
    std::cout << std::get<1>(result) << std::endl;
    for(int i = 0; i < std::get<0>(result); i++){
        std::cout << std::get<2>(result)[i] << std::endl;
    }
    return 0; 
}