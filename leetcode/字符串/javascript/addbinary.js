/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
    //return (Number.parseInt(a, 2) + Number.parseInt(b, 2)).toString(2);
    var minLen = Math.min(a.length, b.length) - 1;
    var maxLen = Math.max(a.length, b.length) - 1;
    var strS = a.length >= b.length ? b : a;
    var strB = a.length >= b.length ? a : b;
    var c = [];
    var carry = 0;
    while (minLen > -1) {
        var temp = parseInt(strB[maxLen--]) + parseInt(strS[minLen--]) + carry;
        switch (temp) {
            case 0:
                c.push('0');
                break;
            case 1:
                c.push('1');
                carry = 0;
                break;
            case 2:
                c.push('0');
                carry = 1;
                break;
            case 3:
                c.push('1');
                carry = 1;
                break;
        }
    }
    while (maxLen > -1 && carry){
        var temp = parseInt(strB[maxLen--]) + carry;
        if (temp === 1){
            c.push('1');
            carry = 0;
        } else {
            c.push('0');
            carry = 1;
        }
    }
    if (carry)
        c.push('1');
    c.reverse();
    return (maxLen > -1 ? strB.slice(0, maxLen + 1) : '') + c.join('');
};

console.log(addBinary('0', '0'));