CHALLENGES := welcome execute hello twoplustwo firstarg firstarg-int square

COMPLETION := $(CHALLENGES:%=done/%.done)

.PHONY: progress
progress: $(COMPLETION)
	@echo
	@echo CONGRATULATIONS! You have reached the end of the TDLPL
	@echo challenges.
	@echo
	@echo This is what we have so far. If you would like to contribute to
	@echo the project here are some hints:
	@echo
	@echo To create a new challenge create a test under the test/ directory
	@echo and add it to the CHALLENGES variable to the GNUmakefile.
	@echo
	@echo To support a new programming language, edit the GNUmakefile to
	@echo add the corresponding rule that prepares the runnable file. The
	@echo runnable file goes into the run/ directory. Announce the new
	@echo supported language in test/welcome.
	@echo

done/%.done: test/% run/%
	@echo === $*: executing...
	@mkdir -p done
	@$< || { echo "::: Result: FAILED"; $< --help; false; }
	@echo "::: Result: SUCCESS!"
	@echo

run/%: %.py
	@echo === $*: preparing...
	@mkdir -p run
	@cp $^ $@
	@chmod +x $@

run/%: %.rb
	@echo === $*: preparing...
	@mkdir -p run
	@cp $^ $@
	@chmod +x $@

run/%:
	@echo === Next challenge: $*
	@test/$* --help; false

