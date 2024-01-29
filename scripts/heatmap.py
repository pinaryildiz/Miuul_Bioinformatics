import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ipr_concat = "/Users/pinar/PycharmProjects/Miuul_Bioinformatics/data/ipr_concat.csv"
out_file = "/Users/pinar/PycharmProjects/Miuul_Bioinformatics/data/ipr_heatmap1.png"

def plot_heatmap(df):
    sns.set_style("darkgrid", {'axes.grid': False})
    plt.figure(figsize=(20,6))

    ax=sns.heatmap(df, cmap=sns.cubehelix_palette(start=0.8, rot=-0.9, as_cmap=True),
                   square=True,
                   annot=df.values,
                   fmt='g',
                   linewidths=.6,
                   # annot=True,
                   cbar_kws={"shrink": .5},
                   annot_kws={"size": 8})

    plt.savefig(out_file, format="png", bbox_inches='tight', dpi=800)
    return plt.show()

df = pd.read_csv(ipr_concat, header="infer", sep="\t")
df = df.groupby(["ipr", "sp"]).size().reset_index().sort_values(by=[0], ascending=False)
df = df.rename(columns={0: "count"})[:15]
df = df.pivot(index="ipr", columns="sp", values="count").fillna(0)

plot_heatmap(df)