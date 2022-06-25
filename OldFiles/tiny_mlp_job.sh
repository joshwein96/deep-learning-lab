#!/usr/local_rwth/bin/zsh

#SBATCH --job-name=tiny_mlp

#SBATCH --mem=1GB

#SBATCH --time=0-0:15

#SBATCH --account=lect0085

#SBATCH --output=output.%J.txt

#SBATCH --cpus-per-task=1

#SBATCH --gres=gpu:pascal:1

python3 /home/mx572424/DLL/tiny_mlp.py
