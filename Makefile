top:; @date
Makefile:;
SHELL := bash

include := /^\#include / { f=$$2; while (getline < f) print; next } { print }

README.md.in: Makefile; @echo -e '$(readme)' | sed 's/^ //' > $@
README.md: README.md.in; awk '$(include)' $< > $@
README.html: README.md; pandoc -s --highlight-style kate -o $@ $<
readme: README.html;
.PHONY: readme

add_disk := vsphere add disk
add_nic := vsphere add nic
extraconfig := vsphere extraconfig
status := vsphere status

fcb := ```
# `
h  := \#
h1 := $h
h2 := $h$h
h3 := $h$h$h

define module
$(h2) $($1)
$(h3) documentation
$(fcb)yaml
$(h1)include library/vsphere_$1.d/documentation.yml
$(fcb)

$(h3) examples
$(fcb)yaml
$(h1)include library/vsphere_$1.d/examples.yml
$(fcb)

endef

modules :=
modules += add_disk
modules += add_nic
modules += extraconfig
modules += status

define readme_nl
$(h1) Provide some pysphere modules
Auto generated README from modules documentation

$(foreach _,$(modules),$(call module,$_))
endef

define nl


endef

readme := $(subst $(nl),\n,$(readme_nl))
