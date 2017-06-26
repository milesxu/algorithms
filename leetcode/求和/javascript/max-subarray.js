/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
    //linear implementation
    let [maxS, bound] = [nums[0], nums[0]];
    for (let i = 1; i < nums.length; i++) {
        if (bound < 0)
            bound = nums[i];
        else
            bound += nums[i];
        if (maxS < bound)
            maxS = bound;
    }
    return maxS;
};

// dynamic programming implementation
var maxSubArrayDP = function (nums) {
    let dp = new Array(nums.length);
    dp.fill(0);
    dp[0] = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (dp[i - 1] > 0)
            dp[i] = dp[i - 1] + nums[i];
        else
            dp[i] = nums[i];
    }
    return Math.max(...dp);
}

// divide and conquer implementation
var maxSubArrayDAC = function (nums) {
    const dac = (low, high) => {
        if (high - low === 1)
            return {
                maxL: nums[low], // largest sum begin at left point
                max: nums[low],  // largest sum of sub array
                maxR: nums[low], // largest sum end at right point
                sum: nums[low]  // sum of whole array
            };
        const mid = (low + high) >> 1;
        const left = dac(low, mid);
        const right = dac(mid, high);
        return {
            maxL: Math.max(left.maxL, left.sum + right.maxL),
            max: Math.max(left.maxR + right.maxL, left.max, right.max),
            maxR: Math.max(right.maxR, left.maxR + right.sum),
            sum: left.sum + right.sum
        };
    };
    return dac(0, nums.length).max;
}


var arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4];
//console.log(maxSubArray(arr));
console.log(maxSubArrayDAC(arr));