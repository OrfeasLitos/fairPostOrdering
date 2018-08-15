### Alternative Models

Note: Simultaneous votes are tallied at once, thus the order of posts changes atomically
between simultaneous votes.
`#define MIN_VOTE 3sec`
`#define PLAYERS`
1. Every round lasts `MIN_VOTE` time units. Every player votes as many posts as they
   can/want in their turn of each round simultaneously. (This is closest to our current
   formulation.)
1. Every round lasts `MIN_VOTE*PLAYERS` time units. Every turn lasts `MIN_VOTE` time
   units. Every player can vote 0 or 1 post every turn. All votes are sequential.
1. Every round lasts `MIN_VOTE` time units. Players vote simultaneously 0 or 1 posts every
   round. (This is the actual model Steem uses.)

Note: In all the aforementioned models, each player can vote only once for each post and
voting power is regenerated as time passes. We get alternative models otherwise.

### Which models have attacks

1. The first model is attacked in
   [scripts/simpleVoter.py](https://git.gtklocker.com/orfeas/fairPostOrdering/src/branch/master/scripts/simpleVoter.py).
1. The same attack works for the second model as well, since players cannot cast a second
   vote for the same post and the regeneration every `MIN_VOTE` time units is negligible.
1. [scripts/allPlayersOneVote.py](https://git.gtklocker.com/orfeas/fairPostOrdering/src/branch/master/scripts/allPlayersOneVote.py)
   attacks the third model. Unfortunately here we have to give the posts in an initial order
   that is not optimal, but still the difference in average likeability between the two posts
   is substantial.
