#!/bin/bash
#
### REPLACE _JOB_NAME_ and _EMAIL_ADDRESS_
#
#SBATCH --job-name=Ph_CHEOPS
#SBATCH -o ../slurm_outputs/slurm-%j.out-%N # name of the stdout, using the job number (%j) and the first node (%N)
#SBATCH -e ../slurm_errors/slurm-%j.err-%N # name of the stderr, using job and first node values
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=10
# SBATCH -w, --nodelist=cnode1 # node name where the job should run

#
# Notification by email
# SBATCH --mail-type=END,FAIL
# SBATCH --mail-user=amiguel@astro.up.pt
#
### Other possible options
### SBATCH -w, --nodelist=cnode1 # node name where the job should run
### SBATCH --nodes=1 				# number of nodes to use
### SBATCH --ntasks=1				# number of tasks
### SBATCH --cpus-per-task=4		# number of CPUs per task

srun hostname
python3.4  ~/work/cluster_runs/run_archi.py $SLURM_JOBID $SLURM_NTASKS
