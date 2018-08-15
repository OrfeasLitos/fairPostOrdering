# Creates a list of two posts and two players. Each player votes for
# each post in the order that they appear in the list and the list is
# reordered after each player completes its vote. We assume that both
# players have 1 SP. We have selected player preferences that show
# that the final order of posts does not correspond to the ideal
# order.

class Constants:
  def __init__(self, fullRegen = 144000, minCost = 0.01, divisor = 2):
    self.fullRegen = fullRegen
    self.minCost = minCost
    self.divisor = divisor

class Post:
  def __init__(self, name, score = 0):
    assert isinstance(name, str)

    self.name = name
    self.score = score
    self.voters = []

  def __repr__(self):
    return "Post(%r, %r)" % (self.name, self.score)

  def __str__(self):
    return self.name

  def incScore(self, score):
    self.score += score

  def setScore(self, score):
    self.score = score

  def getScore(self):
    return self.score

  def setVotedBy(self, player):
    self.voters.append(player)

  def isVotedBy(self, player):
    if player in self.voters:
      return True
    else:
      return False

class Player(Constants):
  def __init__(self, name, likes, vp = 1, vpLimit = 0):
    assert isinstance(likes, dict)
    assert isinstance(name, str)
    assert all(0 <= likes[post] <= 1 for post in likes)

    Constants.__init__(self)
    self.name = name
    self.likes = likes
    self.vpLimit = vpLimit
    self.vp = vp

  def __repr__(self):
    return "Player(%r, %r, %r, %r)" % \
      (self.name, self.likes, self.vp, self.vpLimit)

  def __str__(self):
    return self.name

  def vote(self, post, weight = 1):
    assert isinstance(post, Post)
    assert 0 <= post.getScore()
    assert post in self.likes

    # one vote every 3 secs
    self.vp = min(1, self.vp + 1/self.fullRegen)
    if self.vp > self.vpLimit:
      vote = self.likes[post] * self.vp / self.divisor + self.minCost
      self.vp -= vote
      return vote
    else:
      return False

def reset(posts):
  assert isinstance(posts, list)
  assert all(isinstance(post, Post) for post in posts)
  assert all(0 <= post.getScore() for post in posts)

  for post in posts:
    post.setScore(0)

def idealOrder(posts, players):
  assert isinstance(posts, list)
  assert all(isinstance(post, Post) for post in posts)
  assert all(0 <= post.getScore() for post in posts)

  assert isinstance(players, list)
  for player in players:
    assert isinstance(player, Player)
    assert isinstance(player.likes, dict)
    assert all(0 <= player.likes[post] <= 1 for post in player.likes)

  for post in posts:
    for player in players:
      post.setScore(post.getScore() + player.likes[post])

  posts.sort(key=lambda x: x.getScore(), reverse = True)

def simulate(posts, players):
  votecount = 0
  while votecount < len(posts)*len(players):
    for player in players:
      toVote = 0
      while toVote < len(posts) and posts[toVote].isVotedBy(player):
        toVote += 1
      if toVote >= len(posts):
        break
      vote = player.vote(posts[toVote])
      posts[toVote].incScore(vote)
      posts[toVote].setVotedBy(player)
      votecount += 1
    posts.sort(key=lambda x: x.getScore(), reverse = True)

posts = [Post('a'), Post('b')]

players = [Player('A', {posts[0]: 0.5, posts[1]: 0.35}),
           Player('B', {posts[0]: 0.5, posts[1]: 1})]

simulate(posts, players)
print('real order:', posts)
reset(posts)
idealOrder(posts, players)
print('ideal order:', posts)
