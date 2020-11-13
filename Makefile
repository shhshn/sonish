
SHELL := /bin/bash
DIR := sonish
PYTHON := python3
CPP := c++ -x c++

.SECONDARY:

.PHONY: default
default: test/demo.compile
	test/demo

.PHONY: test
test: $(subst .py,.diff,$(wildcard test/*.py))

.PHONY: clean
clean:
	rm -f $(basename $(wildcard test/*.py))

%.diff: %.compile
	diff -q <($(PYTHON) $*.py) <($*)
%.compile:
	$(PYTHON) $(DIR)/dev.py -f $(basename $@).py >/tmp/$(notdir $(basename $@)) && \
	$(CPP) /tmp/$(notdir $(basename $@)) -o $(basename $@) -fconcepts
%.debug:
	$(PYTHON) $(DIR)/dev.py -f $(basename $@).py >/tmp/$(notdir $(basename $@))

#test/demo.compile:
#	$(PYTHON) $(DIR)/poc.py <$(basename $@).py | $(CPP) /dev/stdin -o $(basename $@) -fconcepts
