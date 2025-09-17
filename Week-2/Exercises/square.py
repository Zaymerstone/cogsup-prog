
from expyriment import design, control, stimuli


exp = design.Experiment(name="Square")


control.initialize(exp)


fixation = stimuli.FixCross()

square = stimuli.Rectangle((50, 50), colour=(0,0,255))


control.start(subject_id=1)


fixation.present(clear=True, update=True)


exp.clock.wait(1000)


square.present(clear=True, update=True)
fixation.present(clear=False, update=True)


exp.keyboard.wait(500)

square.present(clear=True, update=True)
control.end()