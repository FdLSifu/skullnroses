class Player:
    def __init__(self,name):
        self.name = name
        self.deck = ['R','R','R','S']   # Starting deck
        self.side = 'S'                 # Starting side is Skull

    def setid(self,i):
        self.id = i                     # players id to order the round

class Game:
    states = ["None", "Playing", "Done"]
    def __init__(self,nbplayer):
        self.nbplayer = nbplayer    # Max players
        self.players = []           # Actual players
        self.status = Game.states[0]     # Check status of the game

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

    def list_player(self):
        s = []
        for p in self.players:
            s.append(p.name)
        return s
