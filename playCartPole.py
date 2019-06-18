import gym

if __name__ == "__main__":
    env = gym.make("CartPole-v0")
    total_reward = 0.0
    total_steps = 0
    obs = env.reset()
    not_done = True

while not_done:
        action = env.action_space.sample()
        obs, reward, done, _ = env.step(action)
        not_done = not done
        total_reward += reward
        total_steps += 1
print("Episode done in %d steps, total reward %.2f" % (total_steps, total_reward))