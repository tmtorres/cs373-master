all:

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  Netflix.html
	rm -f  Netflix.log
	rm -f  RunNetflix.tmp
	rm -f  RunNetflix.out
	rm -f  TestNetflix.out
	rm -rf __pycache__

diff: RunNetflix.py RunNetflix.in RunNetflix.out
	RunNetflix.py < RunNetflix.in > RunNetflix.tmp
	diff RunNetflix.out RunNetflix.tmp

Netflix.html: Netflix.py
	pydoc -w Netflix

Netflix.log:
	git log > Netflix.log

RunNetflix.out: RunNetflix.py RunNetflix.in
	-coverage3 run --branch RunNetflix.py < RunNetflix.in > RunNetflix.out
	coverage3 report -m

TestNetflix.out: TestNetflix.py
	-coverage3 run --branch TestNetflix.py
	coverage3 report -m
