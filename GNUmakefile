CHALLENGES := welcome execute hello twoplustwo firstarg

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

run/%:
	@echo === Next challenge: $*
	@test/$* --help; false

