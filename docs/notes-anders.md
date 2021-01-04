# Anders' notes

#### ⭐ is how relevant it is to our projects

# Concept to look at
 - Sparse rewards: A sparse reward task is typically characterized by a meagre amount of states in the state space that return a feedback signal. A typical situation is a situation where an agent has to reach a goal and only receives a positive reward signal when he is close enough to the target.


# Definition of concept
### Task
- A task is an instance of the reinforcement learning (RL) problem
- **Continuing tasks** are tasks that continue forever, without end
- **Episodic tasks** are tasks with a well-defined starting and ending point.
  - In this case, we refer to a complete sequence of interaction, from start to finish, as an **episode**.
  - Episodic tasks come to an end whenever the agent reaches a **terminal state**.

### Discount factor/rate
- Discount factor is gamma(γ)
- How much the agents cares about rewards in the distant future relative to those in the immediate future
- γ =  [0, 1], tips: starting point 0.9
- Lager gamma are the more the agent cars about the distant future


# ML-agents 
- ## [All documentation](https://github.com/Unity-Technologies/ml-agents/tree/master/docs)
- ## [Getting Started](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Getting-Started.md)
- ## [Training Parameter](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-Configuration-File.md)
- ## [TensorBoard](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Using-Tensorboard.md)
- ## [Toolkit Glossary](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Glossary.md)
- ## [Migrating ml-agents updates](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Migrating.md)
# Video
### Reward(conceptually)(⭐⭐⭐)
1. Reward: https://www.youtube.com/watch?v=pVIFc72VYH8
2. Cumulative Reward: https://www.youtube.com/watch?v=ysriH65lV9o
3. Discounted Return: https://www.youtube.com/watch?v=opXGNPwwn7g



### Markov Decision Process(MDP)(example)(⭐)
##### ml-agents use POMDPs not [MDP](https://github.com/Unity-Technologies/ml-agents/issues/84) in 2017
1. https://www.youtube.com/watch?v=NBWbluSbxPg
2. https://www.youtube.com/watch?v=CUTtQvxKkNw
3. https://www.youtube.com/watch?v=UlXHFbla3QI


