/* jshint esversion: 6 */

function permAlone(str) {
    let fArray = [1, 1, 2, 6, 24, 120, 720, 5040];

    let factorize = n => {
        if (n < fArray.length)
            return fArray[n];
        let factor = fArray[fArray.length - 1];
        for (let i = fArray.length; i <= n; i++) {
            factor *= i;
            fArray.push(factor);
        }
        return factor;
    };

    let combinate = (n, k) => {
        if (k >= n)
            return 1;
        return factorize(n) / (factorize(k) * factorize(n - k));
    };

    let alone = function (total, duplicate = 0, dArray = []) {
        if (duplicate === 0)
            return factorize(total);
        let maxDup = Math.max(...dArray);
        if (maxDup - 1 > total - maxDup)
            return 0;
        let distinct = total - dArray.reduce((acc, cur) => acc + cur, 0);
        let first = factorize(distinct) *
            combinate(distinct + 1, dArray[0]) * factorize(dArray[0]);
        if (duplicate === 1)
            return first;
        if (duplicate === 2) {
            choice = combinate(distinct + 2, dArray[1] - dArray[0] + 1);
            let second = factorize(distinct) * (distinct + 1) *
                factorize(dArray[0]) * choice * factorize(dArray[1]);
            if (distinct)
                return second +
                    first * combinate(total - dArray[1] + 1, dArray[1]) *
                    factorize(dArray[1]);
            return second;
        }
        /*if (duplicate === 1)
            return alone(total) -
                alone(dArray[0]) * alone(total - dArray[0] + 1);
        if (duplicate === 2)
            return alone(total) -
                alone(dArray[0]) * alone(dArray[1]) *
                alone(total - dArray[0] - dArray[1] + 2) -
                alone(dArray[0]) * alone(total - dArray[0] + 1, 1, [dArray[1]]) -
                alone(dArray[1]) * alone(total - dArray[1] + 1, 1, [dArray[0]]);*/

    };

    let chars = {};
    Array.prototype.forEach.call(str, char => {
        if (chars[char])
            chars[char] += 1;
        else
            chars[char] = 1;
    });
    let dup = 0,
        darr = [];
    Object.keys(chars).forEach(i => {
        if (chars[i] > 1) {
            dup++;
            darr.push(chars[i]);
        }
    });
    return alone(str.length, dup, darr);
}

console.log(permAlone("aabb"));