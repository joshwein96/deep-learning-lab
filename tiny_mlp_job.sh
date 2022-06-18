#!/usr/local_rwth/bin/zsh

#SBATCH --job-name=tiny_mlp

#SBATCH --output=tiny_mlp_output.txt

#SBATCH --mem=8GB

#SBATCH --account=lect0085

python3 /home/mx572424/DLL/tiny_mlp.py
