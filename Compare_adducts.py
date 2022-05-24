import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap

fig, ax = plt.subplots(2, sharex=True)
df = pd.read_csv(r"C:\Users\Mohammed\OneDrive - University of Warwick\Mass spec\Protacs\dbet1\adducts_comparison2.csv", index_col=[0])
print(df.columns)
count_cl = df[['Assigned peaks','Total peaks','Direct cleavages', 'Cross ring cleavages']]

cmap = plt.get_cmap('viridis')
new_cmap = truncate_colormap(cmap, 0, 0.9)

count_cl.plot(ax=ax[1],kind='bar', colormap = new_cmap, ylim=(0,160),  figsize=(10,6), width=0.8, ylabel='Counts')

labels = df.index.str.split('(', 1).str[0]
labels = labels.str.split(' ').str[-1]
charges = ['+']*4 +['-']
charges = charges*3
labels = labels+charges


colors = ['b', 'b', 'b','b','b',
          'r', 'r', 'r','r','r',
          'purple', 'purple', 'purple','purple','purple']

df['Moiety coverge (%)'] = (df['Moieties']/df['Total moieties'])*100

# frag_eff.T.plot(ax=ax[0],kind='bar',label='index',colormap = 'inferno', ylim=(0,100), width=0.3, ylabel='Fragmentation efficiency (%)')

ax[0].bar(range(len(df)), df['Moiety coverge (%)'], color=colors, width=0.3)
ax[0].set_ylim(0,120)
ax[0].set_ylabel('Moiety coverge (%)')

rects = ax[0].patches



for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax[0].text(
        rect.get_x() + rect.get_width() / 2, height + 5, label, ha="center", va="bottom"
    )

for xtick, color in zip(ax[1].get_xticklabels(), colors):
    xtick.set_color(color)
plt.setp(ax[1].xaxis.get_majorticklabels(), rotation=45, ha="right", rotation_mode="anchor" )


# plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.tight_layout()

plt.savefig(r"C:\Users\Mohammed\OneDrive - University of Warwick\Mass spec\Protacs\dbet1\adducts_comparison2.png", dpi=900)

plt.show()


# a = df.index.str.extract('.*\((.*)\).*')
# cid = '<' + a[a=='CID'].dropna() + '{"color": "blue"}>'
# irmpd = '<' + a[a=='IRMPD'].dropna() + '{"color": "red"}>'
# uvpd = '<' + a[a=='UVPD'].dropna() + '{"color": "purple"}>'
# aa = pd.concat([cid,irmpd,uvpd])
# aa = aa[0].to_list()
# b = df.index.str.split('(', 1).str[0]
#
#
# df['label3'] = b +' ' +aa
# df.set_index('label3', inplace=True, drop=True)
# count_cl = df[['Assigned peaks','Total peaks','Direct cleavages', 'Cross ring cleavages']]
#
# cmap = plt.get_cmap('viridis')
# new_cmap = truncate_colormap(cmap, 0, 0.9)
#
# count_cl.plot(ax=ax,kind='bar', colormap = new_cmap, ylim=(0,160),  figsize=(10,6), width=0.8)
# plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha="right", rotation_mode="anchor" )
# # plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
# plt.tight_layout()
# plt.show()
# print(df)
