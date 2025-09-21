#include <vector>
#include <map>
#include <set>
#include <unordered_map>
using namespace std;

class MovieRentingSystem {
private:
    // movie -> set of (price, shop) for unrented movies
    unordered_map<int, set<pair<int, int>>> unrented;
    
    // set of (price, shop, movie) for rented movies
    set<tuple<int, int, int>> rented;
    
    // (shop, movie) -> price
    map<pair<int, int>, int> prices;
    
public:
    MovieRentingSystem(int n, vector<vector<int>>& entries) {
        for (auto& entry : entries) {
            int shop = entry[0];
            int movie = entry[1];
            int price = entry[2];
            
            prices[{shop, movie}] = price;
            unrented[movie].insert({price, shop});
        }
    }
    
    vector<int> search(int movie) {
        vector<int> result;
        
        if (unrented.find(movie) != unrented.end()) {
            for (auto& [price, shop] : unrented[movie]) {
                result.push_back(shop);
                if (result.size() == 5) break;
            }
        }
        
        return result;
    }
    
    void rent(int shop, int movie) {
        int price = prices[{shop, movie}];
        
        // Remove from unrented
        unrented[movie].erase({price, shop});
        
        // Add to rented
        rented.insert({price, shop, movie});
    }
    
    void drop(int shop, int movie) {
        int price = prices[{shop, movie}];
        
        // Remove from rented
        rented.erase({price, shop, movie});
        
        // Add back to unrented
        unrented[movie].insert({price, shop});
    }
    
    vector<vector<int>> report() {
        vector<vector<int>> result;
        
        for (auto& [price, shop, movie] : rented) {
            result.push_back({shop, movie});
            if (result.size() == 5) break;
        }
        
        return result;
    }
};