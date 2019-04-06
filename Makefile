
.PHONY: default run
.SECONDARY:

default:
	python3 dev.py -f demo.py

run:
	cat /dev/stdin | python3 poc.py | c++ -x c++ /dev/stdin
#	c++ -std=c++14
