<img width="697" height="295" alt="MQL" src="https://github.com/user-attachments/assets/93df2792-9d97-4b41-bf31-7a1ea258d3e0" />

<img width="1430" height="412" alt="RMS" src="https://github.com/user-attachments/assets/4ad396e7-b983-4c6f-bb20-265a25736280" />

<img width="1437" height="396" alt="EDF" src="https://github.com/user-attachments/assets/5b72ea6c-ffc1-4828-b360-d8474f545026" />


# OS Laboratory Activity 3
## Multilevel Queue and Real-Time CPU Scheduling
 
### Student Information
- Name: Restauro, Kenneth O.
- Course and Section: BCA151 - B186.1
- Instructor: Bahinting, Maria Fe P. 
- Date Submitted: 11/12/2026

### I. Introduction
This laboratory activity focuses on the implementation and simulation of Multilevel Queue (MLQ) and real-time CPU scheduling algorithms using Python and GitHub. Students will explore how MLQ organizes processes into different queues with specific scheduling policies, while Rate Monotonic Scheduling (RMS) and Earliest Deadline First (EDF) manage periodic tasks based on priority and deadline requirements.

### II. Objectives
- Explain the operation of Multilevel Queue, RMS, and EDF scheduling algorithms.
- Implement MLQ scheduling using Round Robin and FCFS.
- Implement preemptive RMS and EDF scheduling simulations using Python.
- Generate and interpret Gantt charts showing process and task execution.
- Calculate CPU utilization, waiting time, turnaround time, and deadline compliance.
- Create and manage a GitHub repository containing Python source code and laboratory documentation.

### III. Scheduling Algorithms
1. Multilevel Queue Scheduling
2. Rate Monotonic Scheduling
3. Earliest Deadline First

### IV. Program Implementation
Explain how each algorithm was implemented.

### V. Test Data
Include the datasets used for MLQ, RMS, and EDF.

#### Multilevel Queue Dataset
| PID | Arrival Time | Burst Time | Queue # |
| :-: | :----------: | :--------: | :-----: |
| P1  | 0            | 5          | 1       |
| P2  | 1            | 4          | 1       |
| P3  | 0            | 6          | 2       |
| P4  | 2            | 3          | 2       |
| P5  | 3            | 2          | 1       |

#### Rate-Monotonic & Earliest Deadlines First Scheduling Dataset
| PID | Completion Time | Burst Time | Deadline |
| :-: | :-------------: | :--------: | :------: |
| P1  | 1               | 4          | 4        |
| P2  | 1               | 5          | 5        |
| P3  | 2               | 10         | 10       |

### VI. Results and Discussion
Include the Gantt charts, execution sequences,
performance metrics, CPU utilization, and
deadline compliance results.

### VII. Algorithm Comparison
MLQ (Multilevel Queue Scheduling) divides processes into separate queues based on their classifications, with each queue having its own scheduling policy and priority. RMS (Rate Monotonic Scheduling) is a fixed-priority real-time scheduling algorithm that assigns higher priority to tasks with shorter periods. EDF (Earliest Deadline First) is a dynamic-priority real-time scheduling algorithm that prioritizes the ready task with the earliest absolute deadline.

### VIII. Conclusion
Summarize the knowledge and skills gained.
