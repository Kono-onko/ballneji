import pandas as pd
import matplotlib.pyplot as plt

normal_5kg_d1_data_df = pd.read_csv('csv/1101/1101_5kg_d1_5min_1.CSV', skiprows=2)
kiridashi_df = normal_5kg_d1_data_df[normal_5kg_d1_data_df['speed'] > 7950]
kiridashi2_df = kiridashi_df[kiridashi_df['speed'] < 8040]

print(normal_5kg_d1_data_df)
print(kiridashi_df)
print(kiridashi2_df)

fig = plt.figure(figsize=(10,5))
#torque
ax = fig.add_subplot(2,2,1)
ax.plot(normal_5kg_d1_data_df.index + 0, normal_5kg_d1_data_df['torque'], label='normal_5kg')

ax = fig.add_subplot(2,2,2)
ax.plot(kiridashi2_df.index + 0, kiridashi2_df['torque'], label='kiridashi2')

#speed
ax = fig.add_subplot(2,2,3)
ax.boxplot(normal_5kg_d1_data_df['torque'])

ax = fig.add_subplot(2,2,4)
ax.boxplot(kiridashi2_df['torque'])

plt.legend()
plt.show()


