from expyriment import design, control, stimuli

# ----- Setup -----
exp = design.Experiment(name="Buffer Demo with Colors - Fixed")
control.initialize(exp)

# Make the fixation cross bigger & thicker so it's easy to see
fixcross = stimuli.FixCross(colour=(255, 0, 0), size=(120, 120), line_width=8)  # red cross
circle = stimuli.Circle(radius=50, colour=(0, 255, 0))                         # filled green circle

control.start()

# --- 1) Show only the cross first (just for demonstration) ---
fixcross.present(clear=True, update=True)
exp.clock.wait(1000)

# --- 2) Now draw the circle first in the BACK buffer, then draw the cross on top ---
circle.present(clear=True, update=True)   # draw circle to back buffer, but don't show yet
fixcross.present(clear=True, update=True) # add cross on top, then swap buffers -> both visible

# Wait for a key press, then exit
exp.keyboard.wait()
control.end()
