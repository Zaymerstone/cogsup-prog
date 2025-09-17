
from expyriment import design, control, stimuli


exp = design.Experiment(name="Square")

fixation = stimuli.FixCross()

control.initialize(exp)

square = stimuli.Rectangle(size=(100, 100), colour=(255, 0, 0), position=(-200, 0))  # left
square2 = stimuli.Rectangle(size=(100, 100), colour=(0, 128, 0), position=(200, 0))  # right


control.start(subject_id=1)


fixation.present(clear=True, update=True)


exp.clock.wait(1000)


square.present(clear=True, update=False)
square2.present(clear=False, update=True)

exp.keyboard.wait()


control.end()