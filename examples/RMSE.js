/*jslint white: true*/
/*global println*/

// -------
// RMSE.js
// -------

function assert (b) {
    "use strict";
    if (!b) {
        throw "Assertion Error";}}

function sqre_diff (x, y) {
    "use strict";
    return Math.pow(x - y, 2);}

function rmse_while (a, p) {
    "use strict";
    var s = a.length,
        i = 0,
        v = 0;
    while (i !== s) {
        v += sqre_diff(a[i], p[i]);
        i += 1;}
    return Math.sqrt(v / s);}

println("RMSE.js");

assert(rmse_while([2, 3, 4], [2, 3, 4]) === 0);
assert(rmse_while([2, 3, 4], [3, 4, 5]) === 1);
assert(rmse_while([2, 3, 4], [4, 1, 6]) === 2);
assert(rmse_while([2, 3, 4], [4, 3, 2]) === 1.632993161855452);

println("Done.");
