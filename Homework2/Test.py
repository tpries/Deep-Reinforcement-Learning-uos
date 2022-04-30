from GridWorld import GridWorld
from Action import Action
import time
import numpy as np
import random


# choosing action greedily if no random action is chosen bc of epsilon
def choose_action(q, state, eps, n_actions=4):
    if np.random.random() < eps:
        action = np.random.choice([i for i in range(n_actions)])
    else:
        action_values = [q[(state,action)] for action in range(n_actions)]
        action = np.argmax(action_values)
    return action


def n_sarsa(n, gridworld_size=5, multiple_walls=True, n_episodes=100):
    env = GridWorld(gridworld_size, multiple_walls)

    # learning parameters
    alpha = 0.35
    gamma = 0.95
    epsilon = 1.0

    # collecting all states
    states = []
    for i in range(gridworld_size):
        for j in range(gridworld_size):
            states.append((i,j))

    # initiating Q with all zeros
    Q = {}
    for state in states:
        for action in range(4):
            Q[(state,action)] = 0 # np.random.uniform(-0.2,0.2)

    # initializing our memory
    state_memory = np.zeros((n, 2))
    action_memory = np.zeros(n)
    reward_memory = np.zeros(n)
    times = 0

    for _ in range(n_episodes):
        done = False
        score = 0
        episode_lengths = []
        scores = []
        t = 0
        T = np.inf
        state = env.reset()
        action = choose_action(Q, state, epsilon)
        action_memory[t % n] = action
        state_memory[t % n] = state

        while not done:

            state, reward, done = env.step(action)

            if done:
                times += 1
                #print("Solved env! ", times, " times")

            #if t > max((n_episodes-_)/ 100,50):
            #    done = True

            if _ == 0:
                env.visualize()

            score += reward
            state_memory[(t+1) % n] = state
            reward_memory[(t+1) % n] = reward

            if done:
                T = t+1
                episode_lengths.append(t)
                #print("Episode ends at step ",t)

            # choose next action
            action = choose_action(Q,state,epsilon)
            action_memory[(t+1) % n] = action

            tau = t - n + 1
            if tau >= 0:
                G = [gamma**(j-tau-1)*reward_memory[j%n] for j in range(tau+1, min(tau+n, T) + 1)]
                G = np.sum(G)

                if tau + n < T:
                    s = tuple(state_memory[(tau + n) % n])
                    a = action_memory[(tau + n) % n]
                    G += gamma**n * Q[(s, a)]

                s = tuple(state_memory[tau % n])
                a = action_memory[tau % n]

                Q[(s, a)] += alpha * (G-Q[(s, a)])

                #print("Tau ", tau, " | Q: ", state_memory[tau % n], " ", action_memory[tau % n])
            t += 1

        for tau in range(t - n  + 1, T):
            G = [gamma**(j-tau-1)*reward_memory[j % n] for j in range(tau+1, min(tau+n, T) + 1)]
            G = np.sum(G)

            if tau + n < T:
                s = state_memory[(tau+n) % n]
                a = action_memory[(tau+n) % n]
                Q[(s,a)] += alpha*(G-Q[(s,a)])

        scores.append(score)
        epsilon = 1 - (_ / n_episodes)

        if _ % 1000 == 0:
            print("Episode: ", _, " score: ", score, " epsilon: ",
                  epsilon, " episode_length: ", t, " times solved: ", times)
            episode_lengths = []
            scores = []
            times = 0

    return Q, env


def main():
    """
    for i in range(1):
        random_grid_world = GridWorld(5+i, True)
        random_grid_world.visualize()

        random_grid_world.print()
        for i in range(10):
            action = Action(random.randint(1,4))
            #action.print()
            #print(random_grid_world.step(action))
    """
    for i in range(5):
        env_size = 5 + i
        Q, env = n_sarsa(env_size*30, env_size, multiple_walls=True, n_episodes=20000*(i+1))


        for i in range(env_size):
            action_string = ""
            for j in range(env_size):
                for a in range(4):
                    action_string += str(Q[((i,j),a)]) + " "
                action_string += "-"
            action_string += "+++"
            print(action_string)

        done = False
        state = env.reset()
        action = choose_action(Q, state, 0)

        step = 0
        while not done:
            step += 1
            if step == 10:
                print("stop")
                break
            state, reward, done = env.step(action)
            env.visualize(write=True)
            action = choose_action(Q, state, 0)

if __name__ == "__main__":
    main()
