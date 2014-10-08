/*jslint forin: true, plusplus: true, white: true*/
/*global println*/

// ------------
// Iteration.js
// ------------

function assert (b) {
    "use strict";
    if (!b) {
        throw "Assertion Error";}}

println("Iteration.js");

var a;
var b;
var i;
var j;
var k;
var s;

i = 0;
s = 0;
while (i !== 10) {
    s += i;
    ++i;}
assert(i === 10);
assert(s === 45);

i = 0;
s = 0;
do {
    s += i;
    ++i;}
while (i !== 10);
assert(i === 10);
assert(s === 45);

s = 0;
for (i = 0; i !== 10; ++i) {
    s += i;}
assert(i === 10);
assert(s === 45);

a = [2, 3, 4];
b = [5, 6, 7];
s = 0;
for (i = 0, j = 0; i !== 3; ++i, ++j) {
    s += a[i] + b[j];}
assert(s === 27);

a = [2, 3, 4];
s = 0;
a.forEach(
    function (v) {
        "use strict";
        assert((typeof v) === "number");
        s += v;});
assert(s === 9);

a = [2, 3, 4];
s = 0;
for (k in a) {
    assert((typeof k) === "string");
    s += parseInt(k, 10);}
assert(s === 3);

a = {x : 2, y : 3, z : 4};
s = 0;
for (k in a) {
    assert((typeof k) === "string");
    s += a[k];}
assert(s === 9);

println("Done.");
