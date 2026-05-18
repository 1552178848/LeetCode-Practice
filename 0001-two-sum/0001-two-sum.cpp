class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for(int i = 0; i < nums.size(); i++)
        {
            int res = target - nums[i];
            if(seen.find(res) != seen.end())
            {
                return {seen[res], i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};