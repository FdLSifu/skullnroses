import base64
import random
class Player:
    def __init__(self,name):
        self.name = name
        self.deck = ['R','R','R','S']   # Starting deck
        self.score = 0                  # Starting score is zero

    def __str__(self):
        return self.name + " has " + str(len(self.deck)) +" cards and " + str(self.score) + " points"

    def setid(self,i):
        self.id = i                     # players id to order the round

    def getroses(self):
        return self.deck.count('R')
    def getskulls(self):
        return self.deck.count('S')
    def playskull(self):
        i = self.deck.index('S')
        assert(i>=0)
        self.deck.pop(i)
    def playrose(self):
        i = self.deck.index('R')
        assert(i>=0)
        self.deck.pop(i)


class Game:
    states = ["Not Started", "On Going", "Done"]
    def __init__(self,nbplayer):
        self.nbplayer = nbplayer    # Max players
        self.players = []           # Actual players
        self.status = Game.states[0]     # Check status of the game
        self.turn = 0
        self.msg = ''
        self.id = base64.b64encode(str(random.randint(0,2**128)).encode()).decode()

    def add_player(self,name):
        if (len(self.players) >= self.nbplayer):
            return False

        # Create player
        player = Player(name)
        # Attribute player id
        player.setid(len(self.players))
        # Add player to the game
        self.players.append(player)
        return True

    def get_playerid(self,name):
        for p in self.players:
            if p.name == name:
                return p.id
        return -1
    def list_player(self):
        s = []
        for p in self.players:
            s.append(p.name)
        return s

    def is_done(self):
        # Game is done when one player has score 2
        for p in self.players:
            if (p.score > 1):
                return p
        # Return player who won
        return None
    
    def launch(self):
        if len(self.players) != self.nbplayer:
            self.msg = 'Missing %s players' % str(self.nbplayer - len(self.players))
            return
        self.msg = 'Game Started'

        self.status = Game.states[1]

