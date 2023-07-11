
from otree.api import *
c = cu

doc = 'Norm Following Task: Kimbrough, E. O., & Vostroknutov, A. (2018).'
class C(BaseConstants):
    NAME_IN_URL = 'NormFollowingTask'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    BLUE_BONUS = 0.1
    YELLOW_BONUS = 0.15
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    RFT_balls_in_blue = models.IntegerField(max=50)
    RFT_balls_in_yellow = models.IntegerField(max=50)
def set_payoffs(player: Player):
    participant = player.participant
    participant.RFT_payoff = (player.RFT_balls_in_blue * C.BLUE_BONUS) + (player.RFT_balls_in_yellow * C.YELLOW_BONUS)
class Task(Page):
    form_model = 'player'
    form_fields = ['RFT_balls_in_blue', 'RFT_balls_in_yellow']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        set_payoffs(player)
class Results(Page):
    form_model = 'player'
page_sequence = [Task, Results]