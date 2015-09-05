Title: Meta Hunter and Fool Me Once
Date: 2015-08-18
Slug: axelrod-meta-hunter-fool-me-once
Author: Thomas Campbell

Once the tournament on Axelrod-Python is run, a boxplot is generated and
displayed on the Readme of the repository so that everyone can see the winning
strategies. As of June 2015 there were 66 strategies submitted to
Axelrod-Python. The boxplot looked like this:

<img src="/images/strategies_boxplot_june_2015.png" alt="Strategies boxplot from
June 2015" style="width: 800px;"/>

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

At first glance it may be easy to say that “Meta Hunter” and “Fool me Once” are
very different strategies. However on closer inspection they appear to be more
similar than you might think. “Meta Hunter” hunts individual mean strategies and
when it finds them it will defect forever. “Fool me Once” bypasses individual
strategies and will just generically defect against anything that defects
unprovoked.

This can be shown be how quickly the two strategies "detect" the mean
strategies. This table breaks down the individual strategies that "Meta Hunter"
hunts and shows the average number of turns it would take to detect them. It
also shows the average number of turns "Fool me Once" takes to detect them.

|Mean Strategy|Description|Meta Hunter Detection Rate (Turns)|Fool Me Once Detection Rate (Turns)|
|-|
|Defector|Always Defects|4|2|
|Alternator|Alternates between cooperating and defecting|6|4|
|Random|Randomly chooses between cooperating and defecting|10 |4 (on average)|
|Golden|Tries brings the ratio of cooperations to defections closer to the golden ratio|8||
|Pi|Tries brings the ratio of cooperations to defections closer to pi|8||
|e|Tries brings the ratio of cooperations to defections closer to e|8||
