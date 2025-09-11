import os
import gc
import slicer
import warnings
import numpy as np
from vtk import vtkWindowToImageFilter, vtkPNGWriter
warnings.filterwarnings("ignore")

from utils.utils_slicer import *

def main():
    list_model = [
                  'Others_UNet', 
                #   'Others_ResUNet', 
                #   'Others_nnUNet', 
                #   'Others_TSC_Net', 
                #   'Others_UDADS_Net', 
                #   'Others_FANN', 
                #   'Others_WingsNet', 
                #   'EGA_Net', 
                  
                #   'J_Others_UNet', 
                #   'J_Others_ResUNet', 
                #   'J_Others_nnUNet', 
                #   'J_Others_TSC_Net', 
                #   'J_Others_UDADS_Net', 
                #   'J_Others_FANN', 
                #   'J_Others_WingsNet', 
                #   'J_EGA_Net', 
                  
                #   'Z_label'
                  ]

    list_patient = os.listdir('//10.125.208.30/gpu_server_data/Guhong/Airway/res/Visualization/J_EGA_Net')
    list_patient = [patient[:-14] for patient in list_patient if 'y_data' in patient]
    list_patient = list_patient[12:]
    for n, patient in enumerate(list_patient):
        for m, model in enumerate(list_model):
            print(model)
            set_view(mode='3D')
            load_data(model, patient)
            show_data()
            
            set_color()
            load_view()
            capture(name=f'{n}_{patient}_{m}_{model}.png')
            gc.collect()
            
            set_color_y()
            load_view()
            capture(name=f'{n}_{patient}_{m}_{model}_y.png')
            gc.collect()
            
            set_color_p()
            load_view()
            capture(name=f'{n}_{patient}_{m}_{model}_p.png')
            gc.collect()
            clear_all()
            