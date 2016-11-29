selfp := $(abspath $(lastword $(MAKEFILE_LIST)))
selfd := $(notdir $(patsubst %/,%,$(dir $(selfp))))

self  := $(basename $(selfd))

include := /^\#include / { f=$$2; while (getline < f) print; next } { print }

../$(self): module.py Makefile documentation.yml examples.yml; awk '$(include)' $< > $@

doc  := $(self)
list := -l

doc list:; ansible-doc -M .. $($@) | cat
