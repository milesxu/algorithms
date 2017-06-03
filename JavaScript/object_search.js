function whatIsInAName(collection, source) {
    // What's in a name?
    var arr = [];
    // Only change code below this line
    let keys = Object.keys(source);
    arr = collection.filter(item => {
        return keys.every(key => item.hasOwnProperty(key) && item[key] === source[key]);
    });

    // Only change code above this line
    return arr;
}

let result = whatIsInAName([{
    first: "Romeo",
    last: "Montague"
}, {
    first: "Mercutio",
    last: null
}, {
    first: "Tybalt",
    last: "Capulet"
}], {
    last: "Capulet"
});

console.log(result);