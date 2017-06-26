/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
    scand = candidates.sort((a, b) => a - b);

    const bSearch = (end, pivot) => {
        let start = 0;
        while (start < end) {
            const mid = (start + end) >> 1;
            if (scand[mid] > pivot)
                end = mid;
            else
                start = mid + 1;
        }
        return start;
    }

    let result = [];
    let [stack, cur, residue] = [
        [], scand.length, target
    ];
    do {
        if (residue && cur) {
            cur = bSearch(cur, residue);
            if (cur) {
                cur--;
                const n = Math.floor(residue / scand[cur]);
                let temp = new Array(n);
                temp.fill(cur);
                stack.push(...temp);
                residue -= n * scand[cur];
            }
        } else {
            if (!residue) {
                let temp = stack.map(i => scand[i]);
                result.push(temp.reverse());
            }
            cur = stack.pop();
            residue += scand[cur];
        }
    } while (stack.length || cur);

    return result;
};

//recursion can also be used
var combinationSum1 = function (candidates, target) {
    let stack = [];
    let result = [];
    let [residue, cur] = [target, 0];
    while (stack.length || cur < candidates.length) {
        if (cur === candidates.length) {
            if (stack.length) {
                cur = stack.pop();
                residue += candidates[cur];
                cur++;
            }
        } else if (!residue) {
            result.push(stack.map(i => candidates[i]));
            cur = candidates.length;
        } else if (residue >= candidates[cur]) {
            stack.push(cur);
            residue -= candidates[cur];
        } else {
            cur++;
        }
    }
    return result;
};

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function (candidates, target) {
    let scand = candidates.filter(i => i <= target).sort((a, b) => a - b);
    let result = [];
    let stack = [];
    let residue = target;
    let i = 0;
    while (stack.length || i < scand.length) {
        if (i === scand.length) {
            if (stack.length) {
                i = stack.pop();
                residue += scand[i];
                i++;
                while (scand[i] === scand[i - 1]) i++;
            }
        } else if (residue >= scand[i]) {
            stack.push(i);
            residue -= scand[i];
            if (!residue) {
                result.push(stack.map(j => scand[j]));
                i = scand.length;
            } else
                i++;
        } else {
            i = scand.length;
        }
    }
    return result;
};

var arr = [2, 3, 6, 7];
//console.log(combinationSum(arr, 7));
//console.log(combinationSum1(arr, 7));
var arr2 = [10, 1, 2, 7, 6, 1, 5];
console.log(combinationSum2(arr2, 8));