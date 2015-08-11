Title: Axelrod Python Strategies
Date: 2015-08-05
Slug: axelrod
Author: Thomas Campbell

## Axelrod-Python

I recently started contributing to a project called Axelrod-Python and have
found it very interesting.

Axelrod-Python is a repository on Github dedicated to recreating Robert
Axelrod’s original iterated prisoner's dilemma tournaments in python in the
1980's. The repository can be viewed
[here](https://github.com/Axelrod-Python/Axelrod).

Axelrod's original tournament was used to simulate evolution and investigate how cooperation can evolve over time. This project aims to reproduce that work.

You can read about Axelrod's original tournaments and learn more about the
prisoner's dilemma
[here](http://axelrod.readthedocs.org/en/latest/background.html).

Axelrod-Python is an open source project and so anyone can contribute. If you want to contribute, there are instructions on how to on the repository [Readme](https://github.com/Axelrod-Python/Axelrod).

## Nice and Mean Strategies

One way of grouping strategies is be splitting them into “nice” and “mean”
strategies. Nice strategies will never defect before their opponent has defected
and so will never defect first. Hence if two nice strategies play each other,
the outcome will always be cooperation on every turn. This is called a
“cooperation cycle”.

A mean strategy is a strategy that may defect before the opponent. Any
randomised strategy is by definition mean.

The advantage of a nice strategy is that when both players cooperate they
maximise their points as a pair. They receive 6 points overall, which is more
than any other situation.

Mean strategies will anger other strategies by defecting. If two strategies end
up defecting against each other on every turn it is called a “defection cycle”.
This is the worst possible outcome as the pair only receives 2 points overall.

Therefore it is easy to see that a cooperation cycle is desirable.

## Meta Hunter and Fool me Once

Once the tournament on Axelrod-Python is run, a boxplot is generated and
displayed on the Readme of the repository so that everyone can see the winning
strategies. As of June 2015 there were 66 strategies submitted to
Axelrod-Python. The boxplot looked like this:

<img src="/images/strategies_boxplot_june_2015.png" alt="Strategies boxplot from
June 2015" style="width: 500px;"/>

As you can see, in June 2015 "Meta Hunter” was the current winning strategy on
Axelrod-Python. This strategy was one of the more complicated strategies of the
tournament. It worked by combining various “hunters” that hunted specific mean
strategies and defected against them. Individually these hunters did not perform
particularly well. However when combined as “Meta Hunter” it proved to be
extremely effective and was the winning strategy for quite a while.

The only other strategy that even came close to “Meta Hunter” was “Fool me
Once”. This strategy was one of the most simple strategies in the tournament. It
cooperated unless the opponent had defected more than once. If the opponent had
defected more than once then it would defect forever. It was extremely simple
and yet very effective. Both of these strategies were “nice”.

At first glance it may be easy to say that “Meta Hunter” and “Fool me Once”  are
very different strategies. However on closer inspection they appear to be more
similar than you might think. “Meta Hunter” hunts individual mean strategies and
when it finds them it will defect forever. “Fool me Once” bypasses individual
strategies and will just generically defect against anything that defects
unprovoked. The end outcome is the same. So even though “Fool me Once” is only a
few lines of code, it does almost the same thing as “Meta Hunter”.

## BackStabber

During the summer holidays I found that I had a bit of spare time. So, naturally
I decided to submit some strategies to Axelrod-Python. I saw that “Fool me Once”
was so simple and so effective and decided to base my new strategy on it. The
first thing I noticed was that every strategy should defect on the last 2 turns
unconditionally. This is because defecting is better than cooperating whether
the opponent cooperates or defects. The reason that cooperating can be
beneficial is to prevent a defection cycle. On the last 2 turns there is no
danger of a defection cycle because by the time your opponent retaliates there
will only be 1 turn left. Therefore defecting on the last 2 turns is better in
every situation.

Due to my strategies nature of cruelty at the end of the round, I named it
“BackStabber”. And sure enough it won the tournament by a very slim margin.

However I then improved the strategy even more. Instead of defecting forever
after my opponent's second defection, I increased it to their fourth. At first I
did not understand why this improved the strategy. Surely it made it more
inefficient? It did. But it greatly improved its performance against strategies
that cooperated most of the time but randomly defected every now and then. It
meant that Backstabber could be in a cooperation cycle with these strategies for
much longer, rather than defecting and being in a defection cycle. Its
performance was improved against these strategies so much that it greatly
outweighed the slight inefficiencies it caused against all of the other
strategies. This improvement propelled Backstabber to the top of the tournament
by a much bigger margin.

## Aggravater

Of course the biggest factor in how well a strategy performs is how well it is
suited to it's environment. Because of this I decided to "tweak" the
environment. I did this by creating a strategy that was deliberately designed so
that Backstabber would perform well against it while the other strategies did
not. I decided to take advantage of the fact that Backstabber would forgive the
first 3 defections from any strategy.

The strategy I created was not designed to win the tournament. It was a pawn. It
was designed to "sacrifice" itself to help Backstabber.

The strategy worked by defecting on the first 3 turns to "aggravate" the
opponent. It then would cooperate until the opponent defected. If they defected
it would then defect forever. I named the strategy "Aggravater".

The reason the strategy worked was because Backstabber would not defect because
Aggravater would not reach the limit of 4 defections. After the first 3 turns
they would begin an endless cooperation cycle and maximise their score.

However, other strategies (like Fool Me Once and Meta Hunter) would defect early
because of the 3 defections at the beginning. This would cause a defection cycle
and minimize their scores.

The end result was that Backstabber's average score became even higher than any
other strategy's.

## Double-Crosser

<img src="/images/strategies_payoff_no_doublecrosser.png" alt="Strategies
payoff" style="width: 1000px;"/>
