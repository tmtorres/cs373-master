/*global print*/
/*jslint white: true*/

// -------------
// Exceptions.js
// -------------

function assert (b) {
    "use strict";
    if (!b) {
        throw "Assertion Error";}}

function f (b) {
    "use strict";
    if (b) {
        throw "abc";}
    return 0;}

print("Exceptions.js\n");

try {
    assert(f(false) === 0);}
catch (e) {
    assert(false);}

try {
    assert(f(true) === 1);
    assert(false);}
catch (e) {
    assert((typeof e) === "string");
    assert(e          === "abc");}

print("Done.\n");
