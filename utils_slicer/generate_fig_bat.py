import os
import gc
import sys
import time
import slicer

from utils.utils_slicer import *
import time

model = sys.argv[1]
patient = sys.argv[2]

set_view(mode='3D')
load_data(model, patient)
time.sleep(3)
show_data()
time.sleep(3)

set_color()
time.sleep(3)
load_view(patient=patient)
time.sleep(3)
capture(name=f'{patient}_{model}.png')
time.sleep(3)

set_color_y()
time.sleep(3)
load_view(patient=patient)
time.sleep(3)
capture(name=f'{patient}_{model}_y.png')
time.sleep(3)

set_color_p()
time.sleep(3)
load_view(patient=patient)
time.sleep(3)
capture(name=f'{patient}_{model}_p.png')
time.sleep(3)

clear_all()
time.sleep(3)
slicer.util.exit()