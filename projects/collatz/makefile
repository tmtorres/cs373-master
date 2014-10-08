all:

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  Collatz.html
	rm -f  Collatz.log
	rm -f  RunCollatz.tmp
	rm -f  RunCollatz.out
	rm -f  TestCollatz.out
	rm -rf __pycache__

diff: RunCollatz.py RunCollatz.in RunCollatz.out
	RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	diff RunCollatz.out RunCollatz.tmp

Collatz.html: Collatz.py
	pydoc3.4 -w Collatz

Collatz.log:
	git log > Collatz.log

RunCollatz.out: RunCollatz.py RunCollatz.in
	-coverage3 run --branch RunCollatz.py < RunCollatz.in > RunCollatz.out
	coverage3 report -m

TestCollatz.out: TestCollatz.py
	-coverage3 run --branch TestCollatz.py
	coverage3 report -m
