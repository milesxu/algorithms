/*jshint esversion: 6 */

function smallestCommons(arr) {
    let a = Math.min(...arr),
        b = Math.max(...arr);
    let all = [],
        multi = 1;
    while (a <= b)
        all.push(a++);
    for (let i = 0; i < all.length; i++) {
        let c = Math.min(multi, all[i]),
            d = Math.max(multi, all[i]);
        multi *= all[i];
        while (c !== 1) {
            let temp = d % c;
            if (temp === 0) {
                multi /= c;
                break;
            } else {
                d = c;
                c = temp;
            }
        }
    }
    return multi;
}


console.log(smallestCommons([1, 5]));