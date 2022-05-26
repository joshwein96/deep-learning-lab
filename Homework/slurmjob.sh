#!/usr/local_rwth/bin/zsh
 
# ask for 10 GB memory
#SBATCH --mem-per-cpu=10240M   #M is the default and can therefore be omitted, but could also be K(ilo)|G(iga)|T(era)
 
# name the job
#SBATCH --job-name=TestSlurm
 
# declare the merged STDOUT/STDERR file
#SBATCH --output=output.%J.txt

export CONDA_ROOT=$HOME/miniconda3
. $CONDA_ROOT/etc/profile.d/conda.sh
export PATH="$CONDA_ROOT/bin:$PATH" 
### begin of executable commands
/home/up087847/miniconda3/envs/dllab/bin/python /home/up087847/DLLab/SlurmTest.py