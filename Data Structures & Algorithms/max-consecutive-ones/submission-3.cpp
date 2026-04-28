class Solution {
private:
    enum class Approach {
        BruteForce,
        SinglePass
    };

    static constexpr Approach kApproach = Approach::SinglePass;

    int bruteForce(const vector<int>& nums) {
        int count, max_count;
        max_count = 0;
        for (int i = 0; i < nums.size(); i++) {
            count = 0;
            for (int j = i; j < nums.size(); j++) {
                if (nums[j] == 0) {
                    break;
                }
                else {
                    count++;
                }
            }
            max_count = max(max_count, count);
        }
        return max_count;
    }

    int singlePass(const vector<int>& nums) {
        int count, max_count;
        count = max_count = 0;
        for (int num : nums) {
            if (num == 1) {
                count++;
            }
            else {
                count = 0;
            }
            max_count = max(count, max_count);
        }
        return max_count;
    }
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        switch (kApproach) {
            case Approach::BruteForce:
            return bruteForce(nums);

            case Approach::SinglePass:
            return singlePass(nums);
        }
        return singlePass(nums);
    }
};