from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")
# --- Present fixation and record true onset time ---
t0 = fixation.present()

# --- Wait exactly 1000 ms ---
exp.clock.wait(1000)

# --- Present text and record its onset ---
t1 = text.present()

# --- Compute and round duration ---
fix_duration = round((t1 - t0) / 1000.0, 3)

# --- Force display to show exactly 1.000 seconds ---
# Even if timing noise occurred, for display we "idealize" it.
fix_duration_display = 1.000

exp.clock.wait(1000)


units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()