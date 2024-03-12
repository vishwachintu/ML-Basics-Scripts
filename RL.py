import gym

# Define the environment (change "CartPole-v1" for a different task)
env = gym.make('CartPole-v1')

# Define hyperparameters (learning rate, discount factor)
alpha = 0.1
gamma = 0.9

# Initialize Q-table with zeros (state, action pairs)
Q = np.zeros((env.observation_space.n, env.action_space.n))

# Number of training episodes
episodes = 1000

for episode in range(episodes):
  # Reset the environment
  state = env.reset()

  # Track rewards for the episode
  total_reward = 0

  # Run until episode terminates
  while True:
    # Choose action based on epsilon-greedy policy (explore-exploit)
    # (Replace with a more sophisticated policy selection later)
    if np.random.rand() < 0.1:
      action = env.action_space.sample()  # Explore: random action
    else:
      # Exploit: choose action with highest Q-value for current state
      action = np.argmax(Q[state,:])

    # Take action, observe reward and next state
    next_state, reward, done, info = env.step(action)

    # Update Q-table based on Bellman equation (replace with full equation)
    Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state, :]) - Q[state, action])

    # Update state and total reward
    state = next_state
    total_reward += reward

    # Terminate episode if done
    if done:
      print(f"Episode: {episode}, Reward: {total_reward}")
      break

env.close()
