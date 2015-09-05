Title: Axelrod Python Strategies
Date: 2015-08-05
Slug: axelrod
Author: Thomas Campbell
Status: Draft

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
payoff" style="width: 700px;"/>
