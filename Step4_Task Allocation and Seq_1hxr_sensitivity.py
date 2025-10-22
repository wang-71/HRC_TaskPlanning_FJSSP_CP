
from ortools.sat.python import cp_model
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time
import json
import pandas as pd
import numpy as np

# Enter number of robots
num_robots = int(input("Number of robots: "))

# Agents: Humans + dynamic number of robots
agents = ['Human'] + [f'Robot{i+1}' for i in range(num_robots)]

file_path = "Step 2_Input Parameters.json"  # Replace with the input data file
with open(file_path, 'r') as file:
    data = json.load(file)

human_time_task_1_17 = data["human_time_task_1_17"]
fatigue_task_1_17 = data["fatigue_task_1_17"]

human_time_task_18_21 = data["human_time_task_18_21"]
fatigue_task_18_21 = data["fatigue_task_18_21"]

human_time_task_22_25 = data["human_time_task_22_25"]
fatigue_task_22_25 = data["fatigue_task_22_25"]

human_time_task_26_41 = data["human_time_task_26_41"]
fatigue_task_26_41 = data["fatigue_task_26_41"]

human_time_task_42_57 = data["human_time_task_42_57"]
fatigue_task_42_57 = data["fatigue_task_42_57"]

human_time_task_58_60 = data["human_time_task_58_60"]
fatigue_task_58_60 = data["fatigue_task_58_60"]

human_time_task_61 = data["human_time_task_61"]
fatigue_task_61 = data["fatigue_task_61"]

human_time_task_62_64 = data["human_time_task_62_64"]
fatigue_task_62_64 = data["fatigue_task_62_64"]

human_time_task_65 = data["human_time_task_65"]
fatigue_task_65 = data["fatigue_task_65"]

human_time_task_66_68 = data["human_time_task_66_68"]
fatigue_task_66_68 = data["fatigue_task_66_68"]

human_time_task_69_71 = data["human_time_task_69_71"]
fatigue_task_69_71 = data["fatigue_task_69_71"]

robot_time_task_1_14 = data["robot_time_task_1_14"]
robot_time_task_15_17 = data["robot_time_task_15_17"]

robot_time_task_18_21 = data["robot_time_task_18_21"]
robot_time_task_22_25 = data["robot_time_task_22_25"]

robot_time_task_26_38 = data["robot_time_task_26_38"]
robot_time_task_39_41 = data["robot_time_task_39_41"]

robot_time_task_42_54 = data["robot_time_task_42_54"]
robot_time_task_55_57 = data["robot_time_task_55_57"]

robot_time_task_58_60 = data["robot_time_task_58_60"]
robot_time_task_61 = data["robot_time_task_61"]

robot_time_task_62_64 = data["robot_time_task_62_64"]
robot_time_task_65 = data["robot_time_task_65"]

robot_time_task_66_68 = data["robot_time_task_66_68"]
robot_time_task_69_71 = data["robot_time_task_69_71"]

task_times = {}
index = 0
extra_factor = float(input("extra_factor: "))

# Task 1-17
for i in range(17):
    task_times[index] = {
        'Human': human_time_task_1_17[i]
    }
    for robot in range(1, num_robots + 1):
        task_times[index][f'Robot{robot}'] = robot_time_task_1_14[i] * extra_factor if i < 14 else robot_time_task_15_17[i - 14] * extra_factor
    index += 1

# Task 18-21
for i in range(4):
    task_times[index] = {
        'Human': human_time_task_18_21[i]
    }
    for robot in range(1, num_robots + 1):
        task_times[index][f'Robot{robot}'] = robot_time_task_18_21[i] * extra_factor
    index += 1

# Task 22-25
for i in range(4):
    task_times[index] = {
        'Human': human_time_task_22_25[i]
    }
    for robot in range(1, num_robots + 1):
        task_times[index][f'Robot{robot}'] = robot_time_task_22_25[i] * extra_factor
    index += 1

# Task 26-41
for i in range(16):
    task_times[index] = {
        'Human': human_time_task_26_41[i]
    }
    for robot in range(1, num_robots + 1):
        task_times[index][f'Robot{robot}'] = robot_time_task_26_38[i] * extra_factor if i < 13 else robot_time_task_39_41[i - 13] * extra_factor
    index += 1

# Task 42-57
for i in range(16):
    task_times[index] = {
        'Human': human_time_task_42_57[i]
    }
    for robot in range(1, num_robots + 1):
        task_times[index][f'Robot{robot}'] = robot_time_task_42_54[i] * extra_factor if i < 13 else robot_time_task_55_57[i - 13] * extra_factor
    index += 1

# Task 58-60
for i in range(3):
    task_times[index] = {
        'Human': human_time_task_58_60[i]
    }
    for robot in range(1, num_robots + 1):
        task_times[index][f'Robot{robot}'] = robot_time_task_58_60[i] * extra_factor
    index += 1

# Task 61
task_times[index] = {
    'Human': human_time_task_61[0]
}
for robot in range(1, num_robots + 1):
    task_times[index][f'Robot{robot}'] = robot_time_task_61[0] * extra_factor
index += 1

# Task 62-64
for i in range(3):
    task_times[index] = {
        'Human': human_time_task_62_64[i]
    }
    for robot in range(1, num_robots + 1):
        task_times[index][f'Robot{robot}'] = robot_time_task_62_64[i] * extra_factor
    index += 1

# Task 65
task_times[index] = {
    'Human': human_time_task_65[0]
}
for robot in range(1, num_robots + 1):
    task_times[index][f'Robot{robot}'] = robot_time_task_65[0] * extra_factor
index += 1

# Task 66-68
for i in range(3):
    task_times[index] = {
        'Human': human_time_task_66_68[i]
    }
    for robot in range(1, num_robots + 1):
        task_times[index][f'Robot{robot}'] = robot_time_task_66_68[i] * extra_factor
    index += 1

# Task 69-71
for i in range(3):
    task_times[index] = {
        'Human': human_time_task_69_71[i]
    }
    for robot in range(1, num_robots + 1):
        task_times[index][f'Robot{robot}'] = robot_time_task_69_71[i] * extra_factor
    index += 1

# Integrate `task_difficulty`
task_difficulty = {}
index = 0
fatigue_scaling_factor = 100

# Task 1-17
for i in range(17):
    task_difficulty[index] = {
        'Human': fatigue_task_1_17[i] * fatigue_scaling_factor,

    }
    index += 1

# Task 18-21
for i in range(4):
    task_difficulty[index] = {
        'Human': fatigue_task_18_21[i] * fatigue_scaling_factor,

    }
    index += 1

# Task 22-25
for i in range(4):
    task_difficulty[index] = {
        'Human': fatigue_task_22_25[i] * fatigue_scaling_factor,

    }
    index += 1

# Task 26-41
for i in range(16):
    task_difficulty[index] = {
        'Human': fatigue_task_26_41[i] * fatigue_scaling_factor,

    }
    index += 1

# Task 42-57
for i in range(16):
    task_difficulty[index] = {
        'Human': fatigue_task_42_57[i] * fatigue_scaling_factor,

    }
    index += 1

# Task 58-60
for i in range(3):
    task_difficulty[index] = {
        'Human': fatigue_task_58_60[i] * fatigue_scaling_factor,

    }
    index += 1

# Task 61
task_difficulty[index] = {
    'Human': fatigue_task_61[0] * fatigue_scaling_factor,

}
index += 1

# Task 62-64
for i in range(3):
    task_difficulty[index] = {
        'Human': fatigue_task_62_64[i] * fatigue_scaling_factor,

    }
    index += 1

# Task 65
task_difficulty[index] = {
    'Human': fatigue_task_65[0] * fatigue_scaling_factor,

}
index += 1

# Task 66-68
for i in range(3):
    task_difficulty[index] = {
        'Human': fatigue_task_66_68[i] * fatigue_scaling_factor,

    }
    index += 1

# Task 69-71
for i in range(3):
    task_difficulty[index] = {
        'Human': fatigue_task_69_71[i] * fatigue_scaling_factor,
    }
    index += 1

# Examine both task time and fatigue
print("Task Times:", task_times)
print("Task Difficulty:", task_difficulty)

num_tasks = 71

model = cp_model.CpModel()

# Scaling factor
scaling_factor = 1
task_times_int = {task: {agent: int(round(time_value * scaling_factor)) for agent, time_value in times.items()} for task, times in task_times.items()}

# Variables
task_start = {}
task_end = {}
task_assigned = {}

for task in range(num_tasks):
    for agent in agents:
        suffix = f'{task}_{agent}'
        task_assigned[(task, agent)] = model.NewBoolVar(f'assigned_{suffix}')
        task_start[(task, agent)] = model.NewIntVar(0, 100000000, f'start_{suffix}')
        task_end[(task, agent)] = model.NewIntVar(0, 100000000, f'end_{suffix}')

for task in range(num_tasks):
    for agent in agents:
        model.Add(task_end[(task, agent)] == task_start[(task, agent)] + task_times_int[task][agent]).OnlyEnforceIf(task_assigned[(task, agent)])

# Constraint 1: Each task is assigned to exactly one agent
for task in range(num_tasks):
    model.Add(sum(task_assigned[(task, agent)] for agent in agents) == 1)

# Constraint 2: NoOverlap
for agent in agents:
    intervals = []
    for task in range(num_tasks):
        start = task_start[(task, agent)]
        end = task_end[(task, agent)]
        interval = model.NewOptionalIntervalVar(start, task_times_int[task][agent], end, task_assigned[(task, agent)], f'interval_{task}_{agent}')
        intervals.append(interval)
    model.AddNoOverlap(intervals)

dependencies = {
    57: [0, 1, 2, 3, 4, 17, 18],  
    58: [5, 6, 7, 8, 9, 18, 19],  
    59: [10, 11, 12, 13, 14, 19, 20],  
    60: [15, 16, 20, 40],        
    61: [0, 1, 2, 3, 4, 21, 22], 
    62: [5, 6, 7, 8, 9, 22, 23],  
    63: [10, 11, 12, 13, 14, 23, 24], 
    64: [15, 16, 24, 56],        
    65: [0, 1, 2, 3, 4, 5, 25, 26, 27, 28, 29],
    66: [5, 6, 7, 8, 9, 10, 30, 31, 32, 33, 34],    
    67: [10, 11, 12, 13, 14, 15, 35, 36, 37, 38, 39], 
    68: [0, 1, 2, 3, 4, 5, 41, 42, 43, 44, 45], 
    69: [5, 6, 7, 8, 9, 10, 46, 47, 48, 49, 50],  
    70: [10, 11, 12, 13, 14, 15, 51, 52, 53, 54, 55], 
}

# Add dependency constraints across agents
for task, prereqs in dependencies.items():
    for prereq in prereqs:
        for agent in agents:
            for prev_agent in agents:
                # Ensure task starts only after all prerequisites end, regardless of agent assignment
                model.Add(task_start[(task, agent)] >= task_end[(prereq, prev_agent)]).OnlyEnforceIf(task_assigned[(task, agent)]).OnlyEnforceIf(task_assigned[(prereq, prev_agent)])

# Dynamically disable robots for certain tasks (e.g., tasks 1-16)

# # UR5e under FMDR
# for task in list(range(57)) + [60] + list(range(64, 71)):
#     for robot in range(1, num_robots + 1):  # Loop through all robots
#         model.Add(task_assigned[(task, f'Robot{robot}')] == 0)

# # UR10e under FMDR
# for task in list(range(17)) + list(range(25, 57)) + [60] + list(range(64, 71)):
#     for robot in range(1, num_robots + 1):  # Loop through all robots
#         model.Add(task_assigned[(task, f'Robot{robot}')] == 0)

# UR20 under FMDR
for task in list(range(16)) + list(range(25, 57)) + [60] + list(range(64, 71)):
    for robot in range(1, num_robots + 1):  # Loop through all robots
        model.Add(task_assigned[(task, f'Robot{robot}')] == 0)

results =[]

total_difficulty = model.NewIntVar(0, 1000000, 'total_difficulty')
model.Add(total_difficulty == sum(
    int(task_difficulty[task]['Human']) * task_assigned[(task, 'Human')]
    for task in range(num_tasks)))

max_end_time = model.NewIntVar(0, 100000000, 'max_end_time')
model.AddMaxEquality(max_end_time, [task_end[(task, agent)] for task in range(num_tasks) for agent in agents])


# Senstivity analysis by entering w2 values
# In this example, from 0 to 2000 with a gap of 10
# Attention: There is a scaling factor of 100 for w2
for w2 in np.arange(0, 20, 0.1):
    w1 = 1
    model.Minimize(w1 * max_end_time + w2 * total_difficulty)

    solver = cp_model.CpSolver()

    # Record start time
    start_time = time.time()

    status = solver.Solve(model)

    # Record stop time
    status = solver.Solve(model)

    end_time = time.time()

    # calculate running time
    elapsed_time = end_time - start_time

    if status == cp_model.OPTIMAL:
        results.append({
            'w2': w2 * fatigue_scaling_factor,
            'Makespan': solver.Value(max_end_time) / scaling_factor,
            'Total Fatigue': solver.Value(total_difficulty) / fatigue_scaling_factor,
            'Elapsed Time (seconds)': elapsed_time
        })

        # Notes
        print(f"Optimization results generated when w2 = {w2 * fatigue_scaling_factor}:")
        print(f"  - Makespan: {solver.Value(max_end_time) / scaling_factor}")
        print(f"  - Total Fatigue: {solver.Value(total_difficulty) / fatigue_scaling_factor}")
        print(f"  - Elapsed Time: {elapsed_time} seconds")
        print("-" * 50)

# Save as DataFrame
results_df = pd.DataFrame(results)

# Export to Excel 
output_file_path = "optimization_results.xlsx"
results_df.to_excel(output_file_path, index=False)

output_file_path