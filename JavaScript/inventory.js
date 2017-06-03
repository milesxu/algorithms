function updateInventory(arr1, arr2) {
    // All inventory must be accounted for or you're fired!
    let index = {};
    for (let i = 0; i < arr1.length; i++) {
        index[arr1[i][1]] = i;
    }
    arr2.forEach(item => {
        if (index.hasOwnProperty(item[1])) {
            let id = index[item[1]];
            arr1[id][0] += item[0];
        } else {
            arr1.push(item);
        }
    });
    return arr1.sort((a, b) => {
        if (a[1] < b[1]) return -1;
        if (a[1] > b[1]) return 1;
        return 0;
    });
}

// Example inventory lists
var curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
];

var newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];

console.log(updateInventory(curInv, newInv));