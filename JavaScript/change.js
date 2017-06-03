/* jshint esversion: 6 */

function checkCashRegister(price, cash, cid) {
    var change;
    // Here is your change, ma'am.
    /*var due = cash - price;
    var total = cid.reduce((acc, cur) => acc + cur[1], 0);
    if (total < due)
        change = 'Insufficient Funds';
    else if (total === due)
        change = 'Closed';
    else {
        change = [];
        let steps = [0.01, 0.05, 0.10, 0.25, 1, 5, 10, 20, 100];
        while (due) {
            let id = steps.findIndex(item => item > due);
            if (id === -1) {
                id = steps.length - 1;
            } else if (id > 1) {
                id -= 1;
            }
            let temp = Math.floor(due / steps[id]);
            temp = Math.min(temp * steps[id], cid[id][1]);
            due -= temp;
            change.push([cid[id][0], temp]);
        }
    }*/
    let due = cash - price;
    var total = cid.reduce((acc, cur) => acc + cur[1], 0).toFixed(2);
    if (parseFloat(total) === due)
        return 'Closed';
    change = [];
    let steps = [0.01, 0.05, 0.10, 0.25, 1, 5, 10, 20, 100];
    let id = steps.length - 1;
    while (id > -1 && due) {
        if (steps[id] <= due) {
            let temp = Math.floor(due / steps[id]);
            temp = Math.min(temp * steps[id], cid[id][1]);
            if (temp) {
                due = parseFloat((due - temp).toFixed(2));
                change.push([cid[id][0], temp]);
            }
        }
        id--;
    }
    if (due) return "Insufficient Funds";
    return change;
}

// Example cash-in-drawer array:
// [["PENNY", 1.01],
// ["NICKEL", 2.05],
// ["DIME", 3.10],
// ["QUARTER", 4.25],
// ["ONE", 90.00],
// ["FIVE", 55.00],
// ["TEN", 20.00],
// ["TWENTY", 60.00],
// ["ONE HUNDRED", 100.00]]

/*console.log(checkCashRegister(19.50, 20.00, [
    ["PENNY", 1.01],
    ["NICKEL", 2.05],
    ["DIME", 3.10],
    ["QUARTER", 4.25],
    ["ONE", 90.00],
    ["FIVE", 55.00],
    ["TEN", 20.00],
    ["TWENTY", 60.00],
    ["ONE HUNDRED", 100.00]
]));*/

/*console.log(checkCashRegister(19.50, 20.00, [
    ["PENNY", 0.50],
    ["NICKEL", 0],
    ["DIME", 0],
    ["QUARTER", 0],
    ["ONE", 0],
    ["FIVE", 0],
    ["TEN", 0],
    ["TWENTY", 0],
    ["ONE HUNDRED", 0]
]));

console.log(checkCashRegister(19.50, 20.00, [
    ["PENNY", 1.01],
    ["NICKEL", 2.05],
    ["DIME", 3.10],
    ["QUARTER", 4.25],
    ["ONE", 90.00],
    ["FIVE", 55.00],
    ["TEN", 20.00],
    ["TWENTY", 60.00],
    ["ONE HUNDRED", 100.00]
]));

console.log(checkCashRegister(3.26, 100.00, [
    ["PENNY", 1.01],
    ["NICKEL", 2.05],
    ["DIME", 3.10],
    ["QUARTER", 4.25],
    ["ONE", 90.00],
    ["FIVE", 55.00],
    ["TEN", 20.00],
    ["TWENTY", 60.00],
    ["ONE HUNDRED", 100.00]
]));

console.log(checkCashRegister(3.26, 100.00, [
    ["PENNY", 1.01],
    ["NICKEL", 2.05],
    ["DIME", 3.10],
    ["QUARTER", 4.25],
    ["ONE", 90.00],
    ["FIVE", 55.00],
    ["TEN", 20.00],
    ["TWENTY", 60.00],
    ["ONE HUNDRED", 100.00]
]));*/

console.log(checkCashRegister(19.50, 20.00, [
    ["PENNY", 0.01],
    ["NICKEL", 0],
    ["DIME", 0],
    ["QUARTER", 0],
    ["ONE", 1.00],
    ["FIVE", 0],
    ["TEN", 0],
    ["TWENTY", 0],
    ["ONE HUNDRED", 0]
]));