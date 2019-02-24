
.PHONY: run
.SECONDARY:

run:
	cat /dev/stdin | python poc.py | c++ -x c++ /dev/stdin
#	c++ -std=c++14
