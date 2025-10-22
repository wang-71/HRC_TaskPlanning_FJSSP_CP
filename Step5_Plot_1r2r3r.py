import matplotlib.pyplot as plt

import pandas as pd
plt.rcParams['font.family'] = 'Times New Roman'

# Load the Excel file
file_path = 'multirobot_optim_results.xlsx'  # Adjust the path if necessary
sheet_name = 0  # Sheet index for the second sheet

# Read the specific range of cells
w2 =  pd.read_excel(file_path, sheet_name=sheet_name, usecols="A", skiprows=0, nrows=222)
df0 = pd.read_excel(file_path, sheet_name=sheet_name, usecols="B", skiprows=0, nrows=222)
df1 = pd.read_excel(file_path, sheet_name=sheet_name, usecols="F", skiprows=0, nrows=222)
df2 = pd.read_excel(file_path, sheet_name=sheet_name, usecols="J", skiprows=0, nrows=222)
df3 = pd.read_excel(file_path, sheet_name=sheet_name, usecols="N", skiprows=0, nrows=222)

f0 = pd.read_excel(file_path, sheet_name=sheet_name, usecols="C", skiprows=0, nrows=222)
f1 = pd.read_excel(file_path, sheet_name=sheet_name, usecols="G", skiprows=0, nrows=222)
f2 = pd.read_excel(file_path, sheet_name=sheet_name, usecols="K", skiprows=0, nrows=222)
f3 = pd.read_excel(file_path, sheet_name=sheet_name, usecols="O", skiprows=0, nrows=222)

f4 = pd.read_excel(file_path, sheet_name=sheet_name, usecols="D", skiprows=0, nrows=222)*5000
f5 = pd.read_excel(file_path, sheet_name=sheet_name, usecols="H", skiprows=0, nrows=222)*5000
f6 = pd.read_excel(file_path, sheet_name=sheet_name, usecols="L", skiprows=0, nrows=222)*5000
f7 = pd.read_excel(file_path, sheet_name=sheet_name, usecols="P", skiprows=0, nrows=222)*5000

# Extract the data from column C (makespan_data_ur20)
w2_value = w2.squeeze().tolist()
makespan_1r = df0.squeeze().tolist()
makespan_2r = df1.squeeze().tolist()
makespan_3r = df3.squeeze().tolist()
makespan_human = df2.squeeze().tolist()
fatigue_1r = f0.squeeze().tolist()
fatigue_2r = f1.squeeze().tolist()
fatigue_3r = f3.squeeze().tolist()
fatigue_human = f2.squeeze().tolist()

fatigue_1r_s = f4.squeeze().tolist()
fatigue_2r_s = f5.squeeze().tolist()
fatigue_3r_s = f7.squeeze().tolist()
fatigue_human_s = f6.squeeze().tolist()

fig, ax1 = plt.subplots(figsize=(12, 14))

# ax1
ax1.set_xlabel(r'$w_2/w_1$', fontsize=12)
ax1.set_ylabel('Makespan(s)', fontsize=12)

ax1.plot(w2_value, makespan_1r, label='1H1R Makespan', color='tab:blue', linestyle='-')
ax1.plot(w2_value, makespan_2r, label='1H2R Makespan', color='tab:orange', linestyle='-')
ax1.plot(w2_value, makespan_3r, label='1H3R Makespan', color='tab:green', linestyle='-')
ax1.plot(w2_value, makespan_human, label='Human-Only Makespan', color='black', linestyle='-')
ax1.set_xlim(0, 2200)

# y axis
ax1.set_ylim(bottom=0)
ax1.tick_params(axis='y', colors='black')
ax1.spines['left'].set_color('black')
#plt.ylim(0, 2000)  # Adjust the upper limit as needed
plt.ylim(0, 8000)  # Adjust the upper limit as needed

# share x axis using twinx()
ax2 = ax1.twinx()
ax2.set_ylabel('Fatigue', fontsize=12)
ax2.plot(w2, fatigue_1r, label='1H1R Total Fatigue', color='tab:blue', linestyle='--')
ax2.plot(w2, fatigue_2r, label='1H2R Total Fatigue', color='tab:orange', linestyle='--')
ax2.plot(w2, fatigue_3r, label='1H3R Total Fatigue', color='tab:green', linestyle='--')
ax2.plot(w2, fatigue_human, label='Human-Only Total Fatigue', color='black', linestyle='--')
ax2.plot(w2, fatigue_1r_s, label='1H1R Fatigue per Second x5000', color='tab:blue', linestyle=':')
ax2.plot(w2, fatigue_2r_s, label='1H2R Fatigue per Second x5000', color='tab:orange', linestyle=':')
ax2.plot(w2, fatigue_3r_s, label='1H3R Fatigue per Second x5000', color='tab:green', linestyle=':')
ax2.plot(w2, fatigue_human_s, label='Human-Only Fatigue per Second x5000', color='black', linestyle=':')
plt.ylim(0, 18)  # Adjust the upper limit as needed

ax2.set_ylim(bottom=0)
ax2.tick_params(axis='y', colors='black')
ax2.spines['right'].set_color('black')

# More transparent vertical lines
for x in range(0, 2401, 50):
    plt.axvline(x=x, color='gray', linestyle='--', alpha=0.2)  # More transparency

# Combine
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()

ax2.legend(lines_1 + lines_2, labels_1 + labels_2, loc='lower left', ncol=3)  # 合并两组图例

plt.show()