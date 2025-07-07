# 47 Game theory

**Game theory** is a branch of mathematics that studies **strategic decision-making** in situations where the outcome for each participant depends on the choices of all participants. It provides a powerful framework for analyzing interactions between **rational agents**, with applications ranging from economics and political science to biology and artificial intelligence.

## Key Concepts

*   **Players:** The individuals or entities making decisions.
*   **Strategies:** The complete plan of action a player will take in a game.
*   **Payoffs:** The outcomes or rewards for each player based on the combination of strategies chosen by all players.
*   **Equilibrium:** A state where no player has an incentive to unilaterally change their strategy, given the strategies of the other players.

## Types of Games

*   **Cooperative vs. Non-cooperative Games:** In cooperative games, players can form binding agreements; in non-cooperative games, they cannot.
*   **Symmetric vs. Asymmetric Games:** In symmetric games, the payoffs for playing a particular strategy depend only on the other strategies employed, not on who is playing them.
*   **Zero-Sum vs. Non-Zero-Sum Games:** In zero-sum games, one player's gain is another's loss (the sum of payoffs is zero). In non-zero-sum games, both players can gain or lose.
*   **Simultaneous vs. Sequential Games:** In simultaneous games, players make decisions at the same time; in sequential games, players make decisions in a specific order.

## The Prisoner's Dilemma

The **Prisoner's Dilemma** is a classic example of a non-zero-sum, non-cooperative game that illustrates why two rational individuals might not cooperate, even if it appears that it is in their best interest to do so. The scenario involves two suspects arrested for a crime, interrogated separately, and offered a deal:

*   If both confess, they each get a moderate sentence.
*   If one confesses and the other doesn't, the confessor goes free, and the other gets a harsh sentence.
*   If neither confesses, they both get a light sentence.

The dominant strategy for each prisoner is to confess, even though mutual cooperation (neither confessing) would yield a better outcome for both.

## Nash Equilibrium

Introduced by **John Nash**, a **Nash Equilibrium** is a set of strategies, one for each player, such that no player can improve their payoff by unilaterally changing their strategy, assuming the other players' strategies remain unchanged. The Prisoner's Dilemma has a single Nash Equilibrium where both players confess.

## Applications of Game Theory

Game theory has revolutionized our understanding of strategic interactions in diverse fields:

*   **Economics:** Modeling market competition, auctions, and bargaining.
*   **Political Science:** Analyzing voting behavior, international relations, and coalition formation.
*   **Biology:** Understanding evolutionary stable strategies and animal behavior.
*   **Computer Science:** Designing algorithms for artificial intelligence, network routing, and security protocols.
*   **Social Sciences:** Studying social dilemmas and cooperation.

# the condensed idea

# Strategic thinking

```python
# Python demo: The Prisoner's Dilemma

def play_prisoner_dilemma(player1_choice, player2_choice):
    # Choices: 'Confess' or 'Stay Silent'
    # Payoffs are represented as (Player1_Years, Player2_Years)

    payoffs = {
        ('Confess', 'Confess'): (5, 5),       # Both confess, moderate sentence
        ('Confess', 'Stay Silent'): (0, 10),  # P1 confesses, P2 silent: P1 free, P2 harsh
        ('Stay Silent', 'Confess'): (10, 0),  # P1 silent, P2 confesses: P1 harsh, P2 free
        ('Stay Silent', 'Stay Silent'): (1, 1) # Both silent, light sentence
    }
    return payoffs[(player1_choice, player2_choice)]

print("Prisoner's Dilemma Simulation:")

# Scenario 1: Both confess (Nash Equilibrium)
p1_choice1 = 'Confess'
p2_choice1 = 'Confess'
payoff1 = play_prisoner_dilemma(p1_choice1, p2_choice1)
print(f"\nPlayer 1: {p1_choice1}, Player 2: {p2_choice1}")
print(f"  Player 1 gets {payoff1[0]} years, Player 2 gets {payoff1[1]} years.")

# Scenario 2: Player 1 confesses, Player 2 stays silent
p1_choice2 = 'Confess'
p2_choice2 = 'Stay Silent'
payoff2 = play_prisoner_dilemma(p1_choice2, p2_choice2)
print(f"\nPlayer 1: {p1_choice2}, Player 2: {p2_choice2}")
print(f"  Player 1 gets {payoff2[0]} years, Player 2 gets {payoff2[1]} years.")

# Scenario 3: Both stay silent (Mutually beneficial, but not Nash Equilibrium)
p1_choice3 = 'Stay Silent'
p2_choice3 = 'Stay Silent'
payoff3 = play_prisoner_dilemma(p1_choice3, p2_choice3)
print(f"\nPlayer 1: {p1_choice3}, Player 2: {p2_choice3}")
print(f"  Player 1 gets {payoff3[0]} years, Player 2 gets {payoff3[1]} years.")

# This demonstrates that even when cooperation leads to a better collective outcome,
# individual rationality can lead to a suboptimal result for both parties.
```
```