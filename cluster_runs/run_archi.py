import sys
sys.path.append('../')
import archi


def main():
    job_number = sys.argv[1]
    n_tasks = int(sys.argv[2])

    controller = archi.Photo_controller(job_number, config_path="/home/amiguel/work/configs/config.yaml",
                                        no_optim=1)

    configs_override = {'base_folder': "/home/amiguel/work/data_files/CHEOPSim_job7724/",
                        "grid_bg": 1800,
                        "initial_detect": 'dynam',
                        "method": "shape+circle",
                        "detect_mode": "offsets+dynam",
                        "optim_processes": n_tasks,
                        "val_range": [1, 20],
                        "low_memory":1,
                        "fine_tune_circle":1,
                        "optimize":1,
                        'uncertainties': 1,
                        'CDPP_type': "DRP",
                        "debug": 1}

    controller.change_parameters(configs_override)
    controller.optimize()
    data_fits = controller.run()

    archi.store_data(data_fits, job_number, **controller.parameters)


if __name__ == '__main__':
    main()
