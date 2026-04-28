class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max_count = 0;

        for (int i = 0; i < nums.size(); i++) {
            int count = 0;
            for (int j = i; j < nums.size(); j++) {
                if (nums[j] == 0) {
                    break;
                }
                else {
                    count++;
                }
            }
            if (count > max_count) {
                max_count = count;
            }
        }
        return max_count;
    }
};