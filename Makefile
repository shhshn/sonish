
SHELL := /bin/bash
DIR := sonish
PYTHON := python3
CPP := c++ -x c++

.PHONY: test
.SECONDARY:

%:
	$(PYTHON) $(DIR)/dev.py -f $@.py | $(CPP) /dev/stdin -o $@

test/demo:
	$(PYTHON) $(DIR)/poc.py <$@.py | $(CPP) /dev/stdin -o $@

test: test/demo
	diff -q <($(PYTHON) $<.py) <(./$<)

clean:
	rm -f test/demo
