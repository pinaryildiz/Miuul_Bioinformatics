from snakemake.shell import shell

file = snakemake.input.file
result = snakemake.output.result

shell(f"""barrnap {file} > {result} """)