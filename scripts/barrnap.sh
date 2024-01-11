#!/usr/bin/env bash

source /Users/pinar/anaconda3/etc/profile.d/conda.sh

conda activate barrnap

barrnap $1 > $2

#./scripts/barrnap.sh resource/Genome/G_intestinalis.fasta output/barrnap_results/G_intestinalis.gff