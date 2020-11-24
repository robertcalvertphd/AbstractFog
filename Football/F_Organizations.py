from Football.C_F_Player import C_Player
from Football.F_Events import *
from Football.F_Interactions import *
from Football.F_ENUMS import E
import _CORE

class F_O_Run_play(_CORE.AF_Organization):
        #something bigger would create players and feed them in... I am doing so here for convenience
    def __init__(self):
        super().__init__(self.middle_run_func, E.RUN_PLAY)
        self.offensive_line = F_O_Run_play.create_players(6)
        self.defensive_line = F_O_Run_play.create_players(4)
        self.line_backers = F_O_Run_play.create_players(4)
        self.safeties = F_O_Run_play.create_players(1)
        self.runner = C_Player()

    def middle_run_func(self, **kwargs):
        # setup line competitions
        line_events = []

        for i in range(len(self.defensive_line)):
            line_events.append(E_Block(self.offensive_line[i], self.defensive_line[i]))
        line_remaining_for_lb = len(self.offensive_line) - len(self.defensive_line)
        for i in range(line_remaining_for_lb):
            o_line_index = len(self.defensive_line) + i
            line_events.append(E_Block(self.offensive_line[o_line_index], self.line_backers[i]))

        # gather players available to make the tackle at time 0
        # line events that whiff + unblocked players
        run_successes = 0
        unblocked_players = []
        for p in self.safeties:
            unblocked_players.append(p)
        unblocked_lbs = len(self.line_backers)-line_remaining_for_lb
        if unblocked_lbs > 0:
            for lb_i in range(unblocked_lbs):
                unblocked_players.append(self.line_backers[line_remaining_for_lb+lb_i])

        over = False
        time = -1

        while over is False:
            time+=1
            for e in line_events:
                if len(e.interactions)>time:
                    current_interaction_at_time = e.interactions[time]
                    if current_interaction_at_time.result == I_Execute_block.WHIFF:
                        unblocked_players.append(current_interaction_at_time.ActorB)
            for p in unblocked_players:
                e = E_Tackle(p, self.runner)
                e.evaluate()
                # only interested in the end though later we may add complexity here

                resolution = e.interactions[len(e.interactions)-1]
                # complexity should be added here based on the quality of the tackle...
                if resolution is True:
                    over = True
            print("Time to tacke = ", time)

    @ staticmethod
    def create_players(n):
        ret = []
        for p in range(n):
            ret.append(C_Player())
        return ret

o = F_O_Run_play()
result = o.run()
print(result)