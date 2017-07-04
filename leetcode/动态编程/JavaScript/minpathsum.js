/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function (grid) {
    let sGrid = new Array();
    for (let i = 0; i < grid.length; i++) {
        let row = new Array(grid[i].length);
        row.fill(0);
        sGrid.push(row);
    }
    for (let i = 0; i < grid.length; i++)
        for (let j = 0; j < grid[0].length; j++) {
            if (i && j) {
                sGrid[i][j] =
                    Math.min(sGrid[i - 1][j], sGrid[i][j - 1]) + grid[i][j];
            } else if (i) {
                sGrid[i][j] = sGrid[i - 1][j] + grid[i][j];
            } else if (j) {
                sGrid[i][j] = sGrid[i][j - 1] + grid[i][j];
            } else {
                sGrid[i][j] = grid[i][j];
            }
        }
    return sGrid[grid.length - 1][grid[0].length - 1];
};

var grd = [[1, 2], [1, 1]];
console.log(minPathSum(grd));