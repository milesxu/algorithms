/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function (nums, target) {
    let snum = nums.sort((a, b) => a - b);
    let result = [];
    let [i, len] = [0, nums.length - 1];
    while (len - i > 2 &&
        snum[i] < target - snum[len] - snum[len - 1] - snum[len - 2])
        i++;
    const avg = Math.round(target / 4);
    const a = i;
    while (i < len - 2 && snum[i] <= avg) {
        if (i > a && snum[i] === snum[i - 1]) {
            i++;
            continue;
        }
        let [j, jbound] = [i + 1, Math.round((target - snum[i]) / 3)];
        while (j < len - 1 && snum[j] <= jbound) {
            if (j > i + 1 && snum[j] === snum[j - 1]) {
                j++;
                continue;
            }
            let [start, end] = [j + 1, len];
            const test = target - snum[i] - snum[j];
            while (start < end) {
                if (start > j + 1 && snum[start] === snum[start - 1]) {
                    start++;
                    continue;
                }
                if (end < len && snum[end] === snum[end + 1]) {
                    end--;
                    continue;
                }
                const s = snum[start] + snum[end];
                if (s < test)
                    start++;
                else {
                    if (s === test)
                        result.push([snum[i], snum[j], snum[start], snum[end]]);
                    end--;
                }
            }
            j++;
        }
        i++;
    }
    return result;
};

var arr = [1, 0, -1, 0, -2, 2];
console.log(fourSum(arr, 0));