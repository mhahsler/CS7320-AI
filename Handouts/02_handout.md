# Chapter 2: Intelligent Agents

This handout provides an overview of intelligent agents, their components, properties, and different types, drawing on the provided source material.

## What is an Intelligent Agent?

An **agent** is defined as anything that can be viewed as **perceiving its environment through sensors and acting upon that environment through actuators**. The agent's behavior is governed by its **agent function**, which maps every possible percept sequence to an action. The **agent program** is the implementation of this agent function.

The agent itself consists of **hardware** (architecture, including sensors, memory, computational power) and the **agent program**. The hardware typically includes an **event loop** that cycles through sensing the environment, feeding percepts to the agent function, receiving an action, and executing that action via actuators. The agent function decides only on the next action to execute.

Examples of agents include mechanical or electronic control systems (where the agent is called a controller) and software programs that run on a host device, known as **softbots**. A spam checker for emails is an example of a softbot.

## Rationality

**Rationality** in the context of intelligent agents is based on moral theories like **consequentialism** and **utilitarianism**. Consequentialism evaluates actions by their consequences, while utilitarianism aims to maximize happiness and well-being.

A **rational agent** is defined as one that, **for each possible percept sequence, selects an action that maximizes its expected performance measure**, given the evidence from the percept sequence and its built-in knowledge. The performance measure is often referred to as **utility** or **reward**.

Key aspects of rationality include:

*   **Rationality is not perfection**: Rational agents maximize *expected* outcomes, not necessarily the actual outcomes. This is especially important in uncertain environments.
*   **It is rational to explore and learn**: Agents can use percepts to supplement prior knowledge and become more autonomous, improving decision-making. Learning allows the agent program to be modified to enhance performance.
*   **Rationality can be bounded**: Agents may be limited by factors such as available memory, computational power, and sensors. Decisions must be made rationally under these constraints.
*   The general rule for a rational agent is to **pick the action that maximizes the expected utility**.

The notion of rationality is heavily dependent on the definition of the **performance measure**. Different performance measures can lead to different conclusions about whether a specific agent program is rational.

## Problem Specification: PEAS

The **PEAS** framework is used to specify an AI problem. It stands for:

*   **P**erformance measure
*   **E**nvironment
*   **A**ctuators
*   **S**ensors

Typically, when specifying a problem using PEAS, you might start with the **Environment**, describing its components and how agent actions affect it. Then you define the **Performance measure**, which specifies utility and what constitutes rational behavior. Next are the **Actuators**, defining the actions available to the agent. Finally, the **Sensors** are defined, which determine the percepts the agent receives.

Examples provided in the sources include:

*   **Automated Taxi Driver**:
    *   Performance measure: Safe, fast, legal, comfortable trip, maximize profits. This can be a complex multi-objective problem.
    *   Environment: Roads, other traffic, pedestrians, customers.
    *   Actuators: Steering wheel (or mechanics to turn wheels), accelerator, brake, signal, horn, possibly communication with passenger.
    *   Sensors: Cameras, sonar, speedometer, GPS, odometer, engine sensors, keyboard (or voice activation for communication).
*   **Spam Filter**:
    *   Performance measure: Accuracy (minimizing false positives and false negatives).
    *   Environment: A user's email account, email server.
    *   Actuators: Mark as spam, delete, etc.. These interact with the email server.
    *   Sensors: Incoming messages, other information about the user's account. This includes the message text.
*   **Modern Robot Vacuum**:
    *   Performance measure: Time to clean 95%, whether it gets stuck.
    *   Environment: Rooms, obstacles, dirt, people/pets.
    *   Actuators: (List not fully provided in source, but would include movement, vacuum, etc.).
    *   Sensors: (List not fully provided in source, but would include proximity sensors, dirt sensors, mapping sensors).

The PEAS description helps in defining the agent function and creating a rational agent.

## Environment Types

The **environment** for the agent function is typically considered to be **everything outside of the agent function itself**, including the sensors and actuators. Sensors often preprocess raw data (like images) into high-level percepts for the agent function, and actuators handle low-level execution based on high-level instructions from the agent function.

Environments can be classified based on several key characteristics:

*   **Fully Observable vs. Partially Observable**: In a **fully observable** environment, the agent's sensors provide access to the complete state of the environment. The agent can "see" the whole environment. In a **partially observable** environment, the agent cannot see all aspects of the environment and may need to remember or infer the rest. A self-driving car not being able to see around a corner is an example of partial observability.
*   **Deterministic vs. Stochastic**: In a **deterministic** environment, the next state is completely determined by the current state and the agent's action. Changes are predictable. In a **stochastic** environment, changes cannot be fully determined; there is randomness. Stochastic environments can have unreliable percepts (stochastic sensor model) or stochastic transition functions. A **strategic** environment is a type of stochastic environment where there are adversarial agents whose actions introduce randomness. Playing a game against another player is strategic.
*   **Known vs. Unknown**: In a **known** environment, the agent knows the rules of the environment, including how actions affect the state (the transition function). In an **unknown** environment, the agent cannot predict the outcome of actions and may need to learn the transition function.
*   **Static vs. Dynamic**: In a **static** environment, the environment does not change while the agent is deliberating. A board game where the opponent doesn't move while you think is static. In a **dynamic** environment, the environment changes while the agent is deliberating. A self-driving car's environment is dynamic because other cars keep moving while it plans. A **semidynamic** environment is static but the agent's performance depends on how fast it acts, often incorporating a time element or stopwatch. Chess with a clock is semidynamic.
*   **Discrete vs. Continuous**: In a **discrete** environment, there are fixed, distinct numbers of percepts, actions, and states. Time can also be discrete. In a **continuous** environment, these aspects can vary along a spectrum (e.g., continuous speed, position). AI typically deals more with discrete environments.
*   **Episodic vs. Sequential**: In an **episodic** environment, the agent's experience is divided into independent episodes. The agent's action in one episode does not affect future episodes. In a **sequential** environment, the current action can affect future decisions and outcomes. The consequences of actions matter in the long term. Chess is sequential because early moves impact the later game.
*   **Single Agent vs. Multi-agent**: In a **single agent** environment, only one agent operates. In a **multi-agent** environment, multiple agents exist, often working together or against each other. Multi-agent environments can often be modeled as single-agent environments by treating other agents as part of a strategic/stochastic environment.

Examples of environments classified by these characteristics:

*   **Vacuum cleaner world**: Fully Observable, Deterministic, Episodic, Static, Discrete, Single agent.
*   **Chess with a clock**: Fully Observable, Strategic/Stochastic*, Sequential, Semidynamic, Discrete, Multi* (often modeled as Single*). (*Strategic/Stochastic and Multi-agent aspects come from including the opponent as part of the environment).
*   **Taxi driving**: Partially Observable, Stochastic + Strategic, Sequential, Dynamic, Continuous, Multi*.

Algorithms for intelligent agents are designed to handle different combinations of observability, uncertainty (stochasticity), and knowledge of the transition function.

## Agent Types

Different types of agent functions define different types of agents. Prototypical agent types include:

1.  **Simple Reflex Agent**:
    *   Acts based only on the **current percept**.
    *   Uses a set of **condition-action rules** (if-then rules) to choose actions.
    *   **Does not have memory** and ignores past percepts.
    *   Its performance depends on the designer creating good rules. The agent itself may not know about the performance measure.
    *   The interaction is a sequence of percept-action pairs (p0, a0, p1, a1, ...).
    *   Example: A simple vacuum cleaner that sucks if dirty, moves right if in A, moves left if in B.

2.  **Model-based Reflex Agent**:
    *   Adds **memory** by maintaining a **state variable** to track aspects of the environment not currently observable.
    *   Uses a **transition function** to model how the environment evolves over time and how actions change the state.
    *   Updates its internal state using the transition function and the new percept.
    *   Uses the **current percept and its internal state** to decide on actions. This provides more information for better decisions.
    *   State representation can be **Atomic** (a simple label for a black box state) or **Factored** (a set of attribute values called fluents). Factored states allow for richer reasoning. The set of all possible states is the state space.
    *   The transition function (T(s, a) = s') maps a current state and action to a next state.
    *   The interaction is a sequence of percept, state, action triplets (p0, s0, a0, p1, s1, a1, ...).
    *   Example: A vacuum cleaner that remembers where it has already been using a map as state information. A smart thermostat compared to an old-school one (which is simple reflex).

3.  **Goal-based Agent**:
    *   Shares the state and transition function machinery with the model-based agent.
    *   Has a defined **goal state** that it aims to reach.
    *   The agent's task is to find a sequence of actions to get from the current state to the goal state.
    *   Often uses **planning** (finding a sequence of actions) and **search algorithms** to find the optimal plan.
    *   A natural performance measure is the **cost to reach the goal**, and the agent seeks to minimize this cost.
    *   Once the goal state is reached, the agent is finished.
    *   Example: An agent solving a maze (goal state is the exit). Route planning for a self-driving car.

4.  **Utility-based Agent**:
    *   Shares machinery (state, transition function) with model-based and goal-based agents but operates differently.
    *   Instead of just a goal state, it assigns a level of **desirability (utility or reward)** to each state or sequence of states.
    *   Chooses actions to **maximize the expected utility** over time.
    *   The performance measure is typically the **discounted sum of expected utility** over potentially infinite time horizons.
    *   Implements rational behavior directly by choosing actions that lead to the most preferred outcomes.
    *   Techniques like **Markov Decision Processes (MDPs)** and **Reinforcement Learning** are used for this type of agent.
    *   Example: A smart thermostat that tries to maintain a comfortable temperature over time. A Mars rover trying to avoid states with low battery. Ensuring a passenger has a pleasant ride in a self-driving car.

5.  **Learning Agent**:
    *   Any of the agent types (reflex, model-based, goal-based, utility-based) can incorporate **learning**.
    *   A **learning element** modifies the agent program (the "performance element") to improve performance based on experience.
    *   A **critic** receives feedback from the environment's outcome and compares it to a **performance standard**, providing a signal to the learning element.
    *   A **problem generator** can suggest exploratory actions to discover better strategies than the current performance element might choose. Learning agents are useful when writing a good agent function manually is difficult.

Real-world applications like self-driving cars are often complex systems composed of **multiple interacting agents** of different types (e.g., simple reflex for emergency braking, model-based for tracking other cars, goal-based for route planning, utility-based for passenger comfort). This leads to complex multi-agent environments.

***

**What You Should Know**:

*   What an **agent function** is and how it interacts with the environment via percepts and actions.
*   What **states** are and the concept of a **transition function**.
*   How environments differ in terms of **observability, uncertainty (stochastic behavior), and whether the transition function is known**.
*   How to **identify different types of agents** (Simple Reflex, Model-based Reflex, Goal-based, Utility-based, Learning) based on their characteristics and how they decide on actions.