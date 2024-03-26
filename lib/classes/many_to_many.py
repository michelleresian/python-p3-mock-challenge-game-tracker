class Game:

    all = []

    def __init__(self, title):
        self._title = title
        Game.all.append(self)

    @property
    def title(self):
        if isinstance(self._title, str) and len(self._title) > 0:
            return self._title
    

    #     if hasattr(Game, 'title'):
    #         print('Cannot change title')

    @title.setter
    def title(self, title):
        raise Exception ("Cannot change title")

    def results(self):
        return [x for x in Result.all if x.game == self]

    def players(self):
        return list(dict.fromkeys([x.player for x in Result.all if x.game == self]))

    def average_score(self, player):
        return sum([x.score for x in Result.all if x.player == player and x.game == self]) / len([x.score for x in Result.all if x.player == player])

class Player:

    all = []

    def __init__(self, username):
        self._username = username
        Player.all.append(self)

    @property
    def username(self):
        if isinstance(self._username, str) and 2 <= len(self._username) <= 16:
            return self._username
        
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return [x for x in Result.all if x.player == self]

    def games_played(self):
        return list(dict.fromkeys([x.game for x in Result.all if x.player == self]))

    def played_game(self, game):
        return game in [x.game for x in Result.all if x.player == self]

    def num_times_played(self, game):
        return len([x for x in Result.all if x.player == self and x.game == game])

class Result:

    all = []

    def __init__(self, player, game, score):
        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)

    @property
    def score(self):
        if isinstance(self._score, int) and 1 <= self._score <= 5000:
            return self._score
        else:
            raise Exception ("Has to be an integer between 1 and 5000")

        
    @score.setter
    def score(self, score):
        self._score = self._score

    @property
    def player(self):
        if isinstance(self._player, Player):
            return self._player

    @property
    def game(self):
        if isinstance(self._game, Game):
            return self._game