from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)

control.start(subject_id=1)

fixation.present(clear=True, update=False) # update parameter must be false here so our back buffer contains the fixation cross
exp.clock.wait(500)

square.present(clear=False, update=True)
exp.keyboard.wait()

control.end()