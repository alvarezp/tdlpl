CHALLENGES := execute hello twoplustwo firstarg firstarg-int square remainder
CHALLENGES += factorial

COMPLETION := $(CHALLENGES:%=done/%.done)

LANG := $(lastword $(shell grep '^language' configuration 2>/dev/null))
MIME := $(lastword $(shell grep '^mimetype' configuration 2>/dev/null))
EXT := $(lastword $(shell grep '^extension' configuration 2>/dev/null))

.PHONY: progress
progress: configuration $(COMPLETION)
	@cat test/messages/completion

.PHONY : fail/%
fail/%:
	@echo "::: TRY AGAIN, your program did not meet the requirement."
	@echo
	@test/$* --help; true
	@echo
	@$(MAKE) -s remind_filename/$*
	@false;

done/%.done: test/% run/%
	@echo === $*: executing...
	@mkdir -p done
	@$< || $(MAKE) -s fail/$*
	@echo "::: CONGRATULATIONS, you passed the '$*' challenge!"
	@echo

.PHONY: header-missing/%
header-missing/%:
	@echo "::: ERROR: Your program is missing the hashbang (#!) signature"
	@echo "    and, thus, it was not identified as a valid $* script."
	@echo
	@echo "You must find the correct hashbang header and place it on the"
	@echo "top of your script. It will not run otherwise."
	@echo
	@echo "See the following Wikipedia article:"
	@echo " - https://en.wikipedia.org/wiki/Hashbang"
	@echo
	@false

.PHONY : check-hashbang/%
check-hashbang/%:
	@file -b --mime-type $* | grep -q "$(MIME)" || \
		$(MAKE) -s header-missing/$(LANG)

configuration:
	@cat test/messages/welcome
	@false

run/%: %.php configuration
	@echo === $*: preparing...
	@$(MAKE) -s check-hashbang/$*.php
	@mkdir -p run
	@cp $< $@
	@chmod +x $@

run/%: %.py configuration
	@echo === $*: preparing...
	@$(MAKE) -s check-hashbang/$*.py
	@mkdir -p run
	@cp $< $@
	@chmod +x $@

run/%: %.rb configuration
	@echo === $*: preparing...
	@$(MAKE) -s check-hashbang/$*.rb
	@mkdir -p run
	@cp $< $@
	@chmod +x $@

run/%: %.c configuration
	@echo === $*: preparing...
	@mkdir -p run
	@c99 -o run/$* $< -l c -l l -l pthread -l m -l rt -l y

.PHONY: remind_filename/%
remind_filename/%:
	@echo Your program must be called $*.$(EXT) and placed in the current \
		directory.
	@echo
	@true

run/%:
	@echo === Next challenge: $*
	@test/$* --help; true;
	@echo
	@$(MAKE) -s remind_filename/$*
	@false

