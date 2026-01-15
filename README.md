# HRC Task Planning using Constraint Programming

## Overall
Task planning for human-robot collaboration in structure assembly

This project addresses task planning for human–robot collaboration (HRC) in structural assembly by formulating the problem as a Flexible Job Shop Scheduling Problem (FJSSP).
The optimization is solved using Constraint Programming (CP) implemented through Google OR-Tools.

This approach allows for efficient allocation and sequencing of human and robot tasks, improving assembly coordination and productivity while mitigating human fatigue.

## Paper:

Wang, Y., & Fang, Y. (2025). Task planning for human–robot collaboration in structural assembly using constraint programming.
Automation in Construction, 179, 106464.
https://doi.org/10.1016/j.autcon.2025.106464

## Description
The graph below illustrates the overall workflow. 
The upper part, highlighted by the green dashed boundary, shows a task classification system based on the robotic potential score (RPS). Using criteria derived from the characteristics of both the tasks and the robot, tasks are classified into two categories: human-or-robot tasks and human-only tasks. 
The lower part, highlighted by the blue dashed boundary, presents a CP-based optimization model for task allocation and sequencing. The task classification outcomes and task dependencies are encoded as constraints, while the processing times for humans and robots and human fatigue are used as input data.

<img width="1184" height="426" alt="image" src="https://github.com/user-attachments/assets/cd70e596-b928-47d1-8ac9-efee7dd4d0cd" />

The following figure is the result of a typical case study. It compares the Pareto outcomes (optimized makespan and total fatigue) for a human-only plan versus 1H1R(1human1robot)–1H3R(1human3robots) across the full range of weight ratios, showing that adding robots generally reduces makespan while fatigue at high w₂/w₁ is largely governed by the human’s non-robot-assignable tasks. It also reveals diminishing marginal returns: the first and second robots deliver much larger makespan reductions than the third, especially in the efficiency-driven region (low w₂).

<img width="1381" height="1108" alt="image" src="https://github.com/user-attachments/assets/3f37e286-291f-4723-a450-9c6361e514f2" />
