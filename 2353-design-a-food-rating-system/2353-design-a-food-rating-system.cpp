class FoodRatings {
    unordered_map<string, pair<string, int>> foodInfo;  // food -> {cuisine, rating}
    unordered_map<string, map<pair<int, string>, int>> cuisineMap;  // cuisine -> sorted map
    
public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for(int i = 0; i < foods.size(); i++) {
            foodInfo[foods[i]] = {cuisines[i], ratings[i]};
            cuisineMap[cuisines[i]][{-ratings[i], foods[i]}] = 1;
        }
    }
    
    void changeRating(string food, int newRating) {
        auto& [cuisine, oldRating] = foodInfo[food];
        cuisineMap[cuisine].erase({-oldRating, food});
        cuisineMap[cuisine][{-newRating, food}] = 1;
        foodInfo[food].second = newRating;
    }
    
    string highestRated(string cuisine) {
        return cuisineMap[cuisine].begin()->first.second;
    }
};