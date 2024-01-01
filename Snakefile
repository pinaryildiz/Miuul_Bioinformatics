rule all:
    input: "output/G_intestinalis.tRNA"

rule tRNAscan:
    input: "resource/G_intestinalis.fasta"
    output: "output/tRNA_scan_result.txt"
    shell: """tRNAscan-SE {input} -o {output} """

rule tRNAscan_stats:
    input:
        genome= "resource/G_intestinalis.fasta"
    output:
        tRNA= "output/G_intestinalis.tRNA",
        stats= "output/G_intestinalis.stats"
    params:
        threads= 2
    conda:
        "env/env.yaml"
    script:
        "scripts/tRNAscan_stats.py"


