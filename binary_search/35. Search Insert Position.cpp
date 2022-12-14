class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int mid, left = 0;
        int right = nums.size() - 1;
        while(left <= right){
            mid = (right - left)/2 + left;
            if(nums[mid] < target){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        return left;
    }
};