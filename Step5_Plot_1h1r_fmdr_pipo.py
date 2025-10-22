import matplotlib.pyplot as plt

import pandas as pd
plt.rcParams['font.family'] = 'Times New Roman'

# Load the Excel file
file_path = 'multirobot_optim_results.xlsx'  # Adjust the path if necessary
# 1 is fmdr
# 2 is pipo
sheet_name = 2  # Sheet index for the second sheet

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
makespan_ur5e = df0.squeeze().tolist()
makespan_ur10e = df1.squeeze().tolist()
makespan_ur20 = df2.squeeze().tolist()
makespan_human = df3.squeeze().tolist()

fatigue_ur5e = f0.squeeze().tolist()
fatigue_ur10e = f1.squeeze().tolist()
fatigue_ur20 = f2.squeeze().tolist()
fatigue_human = f3.squeeze().tolist()

fatigue_ur5e_s = f4.squeeze().tolist()
fatigue_ur10e_s = f5.squeeze().tolist()
fatigue_ur20_s = f6.squeeze().tolist()
fatigue_human_s = f7.squeeze().tolist()

# print(w2_value)
# print(makespan_ur5e)
# print(makespan_ur10e)
fig, ax1 = plt.subplots(figsize=(12, 14))

# ax1 for makespan
ax1.set_xlabel(r'$w_2/w_1$', fontsize=12) 
ax1.set_ylabel('Makespan(s)', fontsize=12)  
ax1.plot(w2_value, makespan_ur5e, label='Human+UR5e Makespan', color='tab:blue', linestyle='-')
ax1.plot(w2_value, makespan_ur10e, label='Human+UR10e Makespan', color='tab:orange', linestyle='-')
ax1.plot(w2_value, makespan_ur20, label='Human+UR20 Makespan', color='tab:green', linestyle='-')
ax1.plot(w2_value, makespan_human, label='Human-Only Makespan', color='black', linestyle='-')
ax1.set_xlim(0, 2200)

# left y 
ax1.set_ylim(bottom=0)
ax1.tick_params(axis='y', colors='black')  
ax1.spines['left'].set_color('black')
plt.ylim(0, 8000)  # Adjust the upper limit as needed

# `ax1.twinx()` share the same x axis
ax2 = ax1.twinx()
ax2.set_ylabel('Fatigue', fontsize=12)  # right y
ax2.plot(w2, fatigue_ur5e, label='Human+UR5e Total Fatigue', color='tab:blue', linestyle='--')
ax2.plot(w2, fatigue_ur10e, label='Human+UR10e Total Fatigue', color='tab:orange', linestyle='--')
ax2.plot(w2, fatigue_ur20, label='Human+UR20 Total Fatigue', color='tab:green', linestyle='--')
ax2.plot(w2, fatigue_human, label='Human-Only Total Fatigue', color='black', linestyle='--')

ax2.plot(w2, fatigue_ur5e_s, label='Human+UR5e Fatigue per Second x5000', color='tab:blue', linestyle=':',linewidth=2)
ax2.plot(w2, fatigue_ur10e_s, label='Human+UR10e Fatigue per Second x5000', color='tab:orange', linestyle=':',linewidth=2.5)
ax2.plot(w2, fatigue_ur20_s, label='Human+UR20 Fatigue per Second x5000', color='tab:green', linestyle=':',linewidth=2)
ax2.plot(w2, fatigue_human_s, label='Human-Only Fatigue per Second x5000', color='black', linestyle=':',linewidth=2)
plt.ylim(0, 18)  # Adjust the upper limit as needed

#ax2.set_ylim(bottom=0)
ax2.tick_params(axis='y', colors='black')  
ax2.spines['right'].set_color('black')

# More transparent vertical lines
for x in range(0, 2401, 50):
    plt.axvline(x=x, color='gray', linestyle='--', alpha=0.2)  # More transparency

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()

ax2.legend(lines_1 + lines_2, labels_1 + labels_2, loc='lower left', ncol=3)  # 合并两组图例

# Title
# plt.title('w2 vs Makespan and Fatigue (UR5,UR10,UR20) Marker')

# Show plot
plt.show()
