from ortools.sat.python import cp_model
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time
import json

# Define two agents, Human and Robot
agents = ['Human', 'Robot']


# Read Input Data
file_path = "Step 2_Input Parameters.json"  # Replace with your Dataset
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract time and fatigue data
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

# Task 1-17
for i in range(17):
    task_times[index] = {'Human': human_time_task_1_17[i], 'Robot': robot_time_task_1_14[i] if i < 14 else robot_time_task_15_17[i - 14]}
    index += 1

# Task 18-21
for i in range(4):
    task_times[index] = {'Human': human_time_task_18_21[i], 'Robot': robot_time_task_18_21[i]}
    index += 1

# Task 22-25
for i in range(4):
    task_times[index] = {'Human': human_time_task_22_25[i], 'Robot': robot_time_task_22_25[i]}
    index += 1

# Task 26-41
for i in range(16):
    task_times[index] = {'Human': human_time_task_26_41[i], 'Robot': robot_time_task_26_38[i] if i < 13 else robot_time_task_39_41[i - 13]}
    index += 1

# Task 42-57
for i in range(16):
    task_times[index] = {'Human': human_time_task_42_57[i], 'Robot': robot_time_task_42_54[i] if i < 13 else robot_time_task_55_57[i - 13]}
    index += 1

# Task 58-60
for i in range(3):
    task_times[index] = {'Human': human_time_task_58_60[i], 'Robot': robot_time_task_58_60[i]}
    index += 1

# Task 61
task_times[index] = {'Human': human_time_task_61[0], 'Robot': robot_time_task_61[0]}
index += 1

# Task 62-64
for i in range(3):
    task_times[index] = {'Human': human_time_task_62_64[i], 'Robot': robot_time_task_62_64[i]}
    index += 1

# Task 65
task_times[index] = {'Human': human_time_task_65[0], 'Robot': robot_time_task_65[0]}
index += 1

# Task 66-68
for i in range(3):
    task_times[index] = {'Human': human_time_task_66_68[i], 'Robot': robot_time_task_66_68[i]}
    index += 1

#Task 69-71
for i in range(3):
    task_times[index] = {'Human': human_time_task_69_71[i], 'Robot': robot_time_task_69_71[i]}
    index += 1

# Intigrate human fatigue `task_difficulty_human`
task_difficulty_human = {}
index = 0
fatigue_scaling_factor = 100

# Task 1-17 
for i in range(17):
    task_difficulty_human[index] = fatigue_task_1_17[i] * fatigue_scaling_factor
    index += 1

# Task 18-21 
for i in range(4):
    task_difficulty_human[index] = fatigue_task_18_21[i] * fatigue_scaling_factor
    index += 1

# Task 22-25 
for i in range(4):
    task_difficulty_human[index] = fatigue_task_22_25[i] * fatigue_scaling_factor
    index += 1

# Task 26-41 
for i in range(16):
    task_difficulty_human[index] = fatigue_task_26_41[i] * fatigue_scaling_factor
    index += 1

# Task 42-57 
for i in range(16):
    task_difficulty_human[index] = fatigue_task_42_57[i] * fatigue_scaling_factor
    index += 1

# Task 58-60 
for i in range(3):
    task_difficulty_human[index] = fatigue_task_58_60[i] * fatigue_scaling_factor
    index += 1

# Task 61 
task_difficulty_human[index] = fatigue_task_61[0] * fatigue_scaling_factor
index += 1

# Task 62-64 
for i in range(3):
    task_difficulty_human[index] = fatigue_task_62_64[i] * fatigue_scaling_factor
    index += 1

# Task 65 
task_difficulty_human[index] = fatigue_task_65[0] * fatigue_scaling_factor
index += 1

# Task 66-68 
for i in range(3):
    task_difficulty_human[index] = fatigue_task_66_68[i] * fatigue_scaling_factor
    index += 1

# Task 69-71 
for i in range(3):
    task_difficulty_human[index] = fatigue_task_69_71[i] * fatigue_scaling_factor
    index += 1

# Examine time and fatigue
print("Task Times:", task_times)
print("Task Difficulty Human:", task_difficulty_human)

num_tasks = len(task_difficulty_human)

# Build OR-Tools model
model = cp_model.CpModel()

# Use scaling factor to get integers
scaling_factor = 1
task_times_int = {task: {agent: int(round(time_value * scaling_factor)) for agent, time_value in times.items()} for task, times in task_times.items()}

# Create Variables
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

######### UR5 ##########
# # UR5 Constrain tasks 1 to 13 to be completed only by humans
# for task in range(13):
#     model.Add(task_assigned[(task, 'Robot')] == 0)

######### UR10 ##########
# # UR10 1-8 human only
# for task in range(71):
#     model.Add(task_assigned[(task, 'Robot')] == 0)

######### UR20 ##########
# UR20 Task 1-16, 61, 65-71 Human Only
for task in range(14):
    model.Add(task_assigned[(task, 'Robot')] == 0)
#
# for task in [60]:  # Task numbers are zero-indexed
#     model.Add(task_assigned[(task, 'Robot')] == 0)  # Ensure robots can't be assigned to these tasks
#
# for task in range(64,71):
#     model.Add(task_assigned[(task, 'Robot')] == 0)

# for task in list(range(16)) + [60] + list(range(64, 71)):
#     model.Add(task_assigned[(task, 'Robot')] == 0)


# Constraint 1: Allocate job to one agent only
for task in range(num_tasks):
    model.Add(sum(task_assigned[(task, agent)] for agent in agents) == 1)

# Constraint 2: No Overlap
for agent in agents:
    intervals = []
    for task in range(num_tasks):
        start = task_start[(task, agent)]
        end = task_end[(task, agent)]
        interval = model.NewOptionalIntervalVar(start, task_times_int[task][agent], end, task_assigned[(task, agent)], f'interval_{task}_{agent}')
        intervals.append(interval)
    model.AddNoOverlap(intervals)

dependencies = {
    57: [0, 1, 2, 3, 4, 17, 18],  # task 58 correspond to task 57 in code
    58: [5, 6, 7, 8, 18, 19],     # task 59 correspond to task 58 in code
    59: [10, 11, 12, 13, 14, 19, 20],  # task 60 correspond to task 59 in code
    60: [15, 16, 20, 40],         # task 61 correspond to task 60 in code
    61: [0, 1, 2, 3, 4, 21, 22],  # task 62 correspond to task 61 in code
    62: [5, 6, 7, 8, 22, 23],     # task 63 correspond to task 62 in code
    63: [10, 11, 12, 13, 23, 24], # task 64 correspond to task 63 in code
    64: [15, 16, 24, 56],         # task 65 correspond to task 64 in code
    65: [0, 1, 2, 3, 4, 25, 26, 27, 28, 29],  # task 66 correspond to task 65 in code
    66: [5, 6, 7, 8, 30, 31, 32, 33, 34],     # task 67 correspond to task 66 in code
    67: [10, 11, 12, 13, 14, 35, 36, 37, 38, 39],  # task 68 correspond to task 67 in code
    68: [0, 1, 2, 3, 4, 41, 42, 43, 44, 45],  # task 69 correspond to task 68 in code
    69: [5, 6, 7, 8, 9, 46, 47, 48, 49, 50],  # task 70 correspond to task 69 in code
    70: [10, 11, 12, 13, 14, 51, 52, 53, 54, 55],  # task 71 correspond to task 70 in code
}

for task, prereqs in dependencies.items():
    for prereq in prereqs:
        for agent in agents:
            for prev_agent in agents:
                model.Add(task_start[(task, agent)] >= task_end[(prereq, prev_agent)]).OnlyEnforceIf(task_assigned[(task, agent)]).OnlyEnforceIf(task_assigned[(prereq, prev_agent)])

# Objective Function: makespan + total fatigue

total_difficulty = model.NewIntVar(0, 1000000, 'total_difficulty')
model.Add(total_difficulty == sum(int(task_difficulty_human[task]) * task_assigned[(task, 'Human')] for task in range(num_tasks)))

max_end_time = model.NewIntVar(0, 100000000, 'max_end_time')
model.AddMaxEquality(max_end_time, [task_end[(task, agent)] for task in range(num_tasks) for agent in agents])

w1 = 1
w2 = 0

model.Minimize(w1 * max_end_time + w2 * total_difficulty)

# Running time
start_time = time.time()
solver = cp_model.CpSolver()
status = solver.Solve(model)
end_time = time.time()

optimization_time = end_time - start_time

print(optimization_time)

# Initialize tasks_data to store task information
tasks_data = []

# Initialize tasks_data to store task information
tasks_data = []

if status == cp_model.OPTIMAL:
    print('Minimum makespan + total difficulty:', solver.ObjectiveValue() / scaling_factor)
    print('Makespan:', solver.Value(max_end_time) / scaling_factor)
    print('Total Difficulty:', solver.Value(total_difficulty) / scaling_factor)

    task_assignment = {agent: [] for agent in agents}

    task_count = {agent: 0 for agent in agents}

    human_total_difficulty = 0

    for task in range(num_tasks):
        for agent in agents:
            if solver.Value(task_assigned[(task, agent)]):
                start = solver.Value(task_start[(task, agent)])
                end = solver.Value(task_end[(task, agent)])
                #print(f'Task {task + 1} assigned to {agent} starts at {start / scaling_factor:.2f} and ends at {end / scaling_factor:.2f}')

                # Add task allocation results to "tasks_data" 
                tasks_data.append((task, agent, start, end))

                task_assignment[agent].append(f"Task {task + 1}")

                task_count[agent] += 1

                if agent == 'Human':
                    human_total_difficulty += task_difficulty_human[task]

    # Print agent task allocation results
    print("\nDetailed Task Assignments:")
    for agent, tasks in task_assignment.items():
        print(f"{agent} is responsible for the following tasks: {', '.join(tasks)}")

    # Print human total fatigue
    print(f"\nTotal Difficulty for Human: {human_total_difficulty:.2f}")

    # Print task allocation results
    print("\nNumber of tasks completed by each agent:")
    for agent, count in task_count.items():
        print(f"{agent} completed {count} tasks")

else:
    print('No optimal solution found.')


# Gantt chart plot
fig, gnt = plt.subplots(figsize=(10, 6))

# Set axis limits
gnt.set_xlim(0, round(solver.Value(max_end_time) * 1.03 / scaling_factor))
gnt.set_ylim(-1, num_tasks + 1)  # Adjust ylim to give extra space at bottom and top

# Set labels
gnt.set_xlabel('Time')
gnt.set_ylabel('Task')

# Set yticks with task numbers (starting from 1)
gnt.set_yticks(range(num_tasks))
gnt.set_yticklabels([f'Task {task + 1}' for task in range(num_tasks)])  # Change from Task 0-9 to Task 1-10

# Plot tasks with different colors for each agent
for task, agent, start, end in tasks_data:
    start_scaled = start / scaling_factor  # recover time
    end_scaled = end / scaling_factor      
    duration = end_scaled - start_scaled   
    if agent == 'Human':
        gnt.barh(task, duration, left=start_scaled, color='blue', edgecolor='black', align='center', label='Human' if task == 0 else "")
    elif agent == 'Robot':
        gnt.barh(task, duration, left=start_scaled, color='orange', edgecolor='black', align='center', label='Robot' if task == 0 else "")

# Add legend
human1_patch = mpatches.Patch(color='blue', label='Human')
robot1_patch = mpatches.Patch(color='orange', label='Robot')
plt.legend(handles=[human1_patch, robot1_patch])

# Set the title
plt.title('Gantt Chart of Human-Robot Collaboration in Structure Assembly')

# Show the plot
plt.show()
