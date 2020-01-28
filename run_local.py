
import matplotlib.pyplot as plt
import numpy as np
import archi
from matplotlib.lines import Line2D
import matplotlib 


def main():
    job_number = 1
    n_tasks = 2

    controller = archi.Photo_controller(job_number, config_path="/home/amiguel/archi/configuration_files/config.yaml",
                                        no_optim=1)
    if 1:
        configs_override = {'base_folder': "/home/amiguel/archi/data_files/CHEOPSim_job7796/",
                            "grid_bg": 0,
                            "initial_detect": 'dynam',
                            "method": "shape",
                            "detect_mode": "dynam",
                            "optim_processes": n_tasks,
                            "val_range": [1, 10],
                            "low_memory":0,
                            "fine_tune_circle":1,
                            "optimize":1,
                            'uncertainties': 1,
                            'CDPP_type': "DRP",
                            "debug": 1,
                            "plot_realtime": 0}

        controller.change_parameters(configs_override)
    controller.optimize()
    data_fits = controller.run()

if __name__ == '__main__':
    main()
