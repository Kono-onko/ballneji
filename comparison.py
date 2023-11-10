import pandas as pd
import matplotlib.pyplot as plt


#ashi_data_df = pd.read_csv('csv/1011/1011_omorinashi_1.CSV', skiprows=2)
ari3kg_data_df = pd.read_csv('csv/1011/1011_omori3kg_1.CSV', skiprows=2)
ari5kg_data_df = pd.read_csv('csv/1011/1011_omori5kg_1.CSV', skiprows=2)
# print(data_df)


#nashi_data = nashi_data_df.rolling(56).mean()
ari3kg_data = ari3kg_data_df.rolling(56).mean()
ari5kg_data = ari5kg_data_df.rolling(56).mean()

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)

# ax.plot(omorinasi_data_df.index + 220, omorinasi_data_df['torque'], label='nashi')
# ax.plot(ari_data_df['torque'], label='ari')

#ax.plot(nashi_data.index + 0,nashi_data['torque'], label='nashi')
ax.plot(ari3kg_data.index - 0,ari3kg_data['torque'], label='3kg')
ax.plot(ari5kg_data.index - 320,ari5kg_data['torque'] + 40, label='5kg')
#ax.plot(ari3kg_data.index - 0,ari3kg_data['speed'], label='3kg')
#ax.plot(ari5kg_data.index - 0,ari5kg_data['speed'], label='5kg')
# ax.plot(data['torque'], label='idouheikinn')

plt.legend()
plt.show()
