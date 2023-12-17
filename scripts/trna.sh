#!/usr/bin/env bash

source /Users/pinar/anaconda3/etc/profile.d/conda.sh

conda activate trnascan

tRNAscan-SE $1 -o $2