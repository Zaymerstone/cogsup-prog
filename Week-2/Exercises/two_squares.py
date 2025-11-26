
from expyriment import design, control, stimuli


exp = design.Experiment(name="Square")

fixation = stimuli.FixCross()

control.initialize(exp)

square = stimuli.Rectangle(size=(100, 100), colour=(255, 0, 0), position=(-200, 0))  # left
square2 = stimuli.Rectangle(size=(100, 100), colour=(0, 128, 0), position=(200, 0))  # right


control.start(subject_id=1)


fixation.present(clear=True, update=False)


# exp.clock.wait(1000)


square.present(clear=True, update=False)
square2.present(clear=False, update=True)

# delete this later
for x in range(-200, 105, 5):
    square.position = (x, 0)   # moving square
    square2.position = (200, 0) # stationary square

    # Draw everything to back buffer
    square.present(clear=True, update=False)   # clear previous frame
    square2.present(clear=False, update=False) # add second square

    # Swap buffers once → both appear together
    exp.screen.update()  # equivalent to present with update=True

    exp.clock.wait(20)   # smooth timing

for y in range(200, 920, 5):
    square2.position = (y, 0)   # moving square
    square.position = (105, 0) # stationary square

    # Draw everything to back buffer
    square2.present(clear=True, update=False)   # clear previous frame
    square.present(clear=False, update=False) # add second square

    # Swap buffers once → both appear together
    exp.screen.update()  # equivalent to present with update=True

    exp.clock.wait(20)
    

exp.keyboard.wait()


control.end()