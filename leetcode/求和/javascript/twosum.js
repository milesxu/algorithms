/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    // an object can have number properties,
    // which need [] to access.
    let keys = {};
    for (let i = 0; i < nums.length; i++){
        let r = target - nums[i];
        if (keys.hasOwnProperty(r)) {
            return [keys[r], i];
        } else {
            keys[nums[i]] = i;
        }
    }
};