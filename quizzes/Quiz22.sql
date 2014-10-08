/*
CS373: Quiz #22 (10 pts) <Mukund>
*/

/* -----------------------------------------------------------------------
 1. Consider a relation R(A, B) with r tuples, all unique within R, and a
    relation S(B, C) with s tuples, all unique within S.
    Let t represent the number of tuples in R natural join S.
    Under what conditions will t be a minimum? What is that minimum?
    Under what conditions will t be a maximum? What is that maximum?
    (4 pts)

None of the values in R.B are in S.B.
0

There's only one value in R.B and S.B.
r*s
*/

/* -----------------------------------------------------------------------
 2. What is the output of the following?
    (5 pts)

A B C
1 6 7
2 7 8
2 7 9
3 8 null
*/

create table R (A int, B int);
create table S (A int, C int);

insert into R values (1, 6);
insert into R values (2, 7);
insert into R values (3, 8);

insert into S values (4, 6);
insert into S values (1, 7);
insert into S values (2, 8);
insert into S values (2, 9);

select * from R left join S using (A);
