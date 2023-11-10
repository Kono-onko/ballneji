import pandas as pd
import matplotlib.pyplot as plt


data_0907_df = pd.read_csv('csv/0907/0907_omori3kg.CSV', skiprows=2)
data_0915_df = pd.read_csv('csv/0915/0915_omori3kg_1.CSV', skiprows=2)
data_0919_df = pd.read_csv('csv/0919/0919_omori3kg_1.CSV', skiprows=2)
data_0922_df = pd.read_csv('csv/0922/0922_omori3kg_1.CSV', skiprows=2)
# print(data_df)


data_0907 = data_0907_df.rolling(150).mean()
data_0915 = data_0915_df.rolling(150).mean()
data_0919 = data_0919_df.rolling(150).mean()
data_0922 = data_0922_df.rolling(150).mean()

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)

# ax.plot(omorinasi_data_df.index + 220, omorinasi_data_df['torque'], label='nashi')
# ax.plot(ari_data_df['torque'], label='ari')

ax.plot(data_0907.index + 0,data_0907['torque'], label='0907')
ax.plot(data_0915.index - 360,data_0915['torque'], label='0915')
ax.plot(data_0919.index - 300,data_0919['torque'], label='0919')
ax.plot(data_0922.index - 165,data_0922['torque'], label='0922')
# ax.plot(data['torque'], label='idouheikinn')

plt.legend()
plt.show()
