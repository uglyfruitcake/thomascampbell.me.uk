Title: An Introduction to Axelrod-Python
Date: 2015-08-11
Slug: axelrod-intro
Author: Thomas Campbell

I recently started contributing to a project called Axelrod-Python and have
found it very interesting.

Axelrod-Python is a python project dedicated to recreating Robert Axelrod’s
original iterated prisoner's dilemma tournaments in the 1980's. The Github
repository can be viewed [here](https://github.com/Axelrod-Python/Axelrod).

Prisoner's dilemma is a two player game theory exercise where both players have the choice of defecting or cooperating. They do not know what the other player will do.

* If they both cooperate they will both receive 3 points.
* If they both defect they will both receive 1 point.
* If one cooperates and one defects then the defector will receive 5 points and the cooperator will receive 0 points.

It can also be defined by this payoff matrix:

$$
\begin{pmatrix}
(1,1) & (5,0)\\
(0,5) & (3,3)\\
\end{pmatrix}
$$

The aim of the game is to maximise your score over 200 rounds. The only information available to you is your opponent's history so far.

In Axelrod-Python strategies are submitted as python code. Each strategy will
play every other in a tournament and the strategy with the highest average score
wins.

Axelrod's original tournament was used to simulate evolution and investigate how
cooperation can evolve over time. This project aims to reproduce that work. You
can read about Axelrod's original tournaments and learn more about the
prisoner's dilemma
[here](http://axelrod.readthedocs.org/en/latest/background.html).

Axelrod-Python is an open source project and so anyone can contribute. If you
want to contribute, there are instructions on how to on the repository
[Readme](https://github.com/Axelrod-Python/Axelrod/blob/master/README.rst).
