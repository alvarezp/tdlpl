CHALLENGES := welcome execute hello twoplustwo firstarg firstarg-int

COMPLETION := $(CHALLENGES:%=done/%.done)

.PHONY: progress
progress: $(COMPLETION)

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

