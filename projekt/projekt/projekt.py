# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import __builtin__
__builtin__.army_list={}
__builtin__.prov_list={}
__builtin__.ind_prov_list={}
__builtin__.pl_list={}
import random
random.seed()
from map_of_world import *
from army import *
from player import player
from actions import *
from nilfgaard import nilfgaard

class game(object):
    turn_number=0
    turn_order=[]
    pl_sitting_order=[]
    def __init__(self,data={}):
        if len(data) == 0:
            player1=player('kuba','p1','nan')
            player2=player('marks','p2','nan')
            a=prov_creator('A','A','p1',5,3,3,['B'])
            b=prov_creator('B','B','p2',5,3,3,['A'])
            ind_prov_creator('X','X',3)
            ind_prov_creator('Y','Y',3)
            ind_prov_creator('Z','Z',3)
            self.nilfgaard=nilfgaard(5,8)
            for i in pl_list:
                self.pl_sitting_order.append(i)
            random.shuffle(self.pl_sitting_order)
            self.turn_order=self.pl_sitting_order
    def get_next_sitting_player(self,ID):
        tmp=None
        for i in range(len(self.pl_sitting_order)):
            if self.pl_sitting_order[i] == ID:
                tmp=i
        if tmp == None:return 'error'
        try:
            return self.pl_sitting_order[tmp+1]
        except IndexError:
            return self.pl_sitting_order[0]
    def post_bid_phase(self,bid_list): #rezerwacja na ewentualne odszkodowania
        pass 
    def bid_phase(self):
        lic={}
        pas={}
        for i in self.pl_sitting_order:
            lic[i]=0
            pas[i]=False
        tmp=True
        def licytacja(pl_id):
                tmp=input('licytuje '+pl_id)
                tmp=int(tmp)
                if pl_list[pl_id].amount_of_gold < tmp:
                    print('nie mozesz dac tyle!')
                    print('maks '+str(pl_list[pl_id].gebid('aog')))
                    return licytacja(pl_id)
                pl_list[pl_id].amount_of_gold-=tmp
                return tmp
        while   tmp:
            tmp=False
            for i in pas:
                if not pas[i]:
                    tmp=True
                    break
            for i in self.turn_order:
                if not pas[i]:
                    l=licytacja(i)
                    if l == 0:
                        pas[i]= True
                        continue
                    lic[i]+=l
            for i in lic:
                print(i+' dal '+str(lic[i]))
            h=next(lic.__iter__())
            for i in lic:
                if lic[h] < lic[i]:
                    h=i
            remis=[]
            remis.append(h)
            for i in lic:
                if lic[i] == lic[h] and i != h:
                    remis.append(i)
            if len(remis) == 1:
                winner=remis[0]
                print('licytacje wygral '+winner)
                while len(self.turn_order) != len(pl_list):
                    self.turn_order.append(self.get_next_sitting_player(winner))
                    winner=self.get_next_sitting_player(winner)
                self.post_bid_phase(lic)
                return
        h=next(lic.__iter__())
        for i in lic:
            if lic[h] < lic[i]:
                h=i
        remis=[]
        remis.append(h)
        for i in lic:
            if lic[i] == lic[h] and i != h:
                remis.append(i)
        intek = random.randint(0,len(remis)-1)
        winner=remis[intek]
        print('licytacje wygral '+winner)
        self.turn_order=[]
        self.turn_order.append(winner)
        while len(self.turn_order) != len(pl_list):
            self.turn_order.append(self.get_next_sitting_player(winner))
            winner=self.get_next_sitting_player(winner)
        self.post_bid_phase(lic)
        return
    def taxes_phase(self):
        for i in prov_list:
            pl_list[i.gebid('pl_id')]=i.gebid('pr_in')
        for i in pl_list:
            if i.longterm_fund:
                i.amount_of_gold+=4
                i.longterm_fund=False
    def nilfgaard_phase(self):
        for i in pl_list: #do zaimplementowania - wybor szpiega
            self.nilfgaard.roll_event(i)
        
    def players_action(self):
        pass #wybor akcji
    def send_troops(self):
        pass # wysylanie wojsk, #przeslanie ich do innych prowincji
    def late_recrutation(self):
        pass # 
if __name__ == "__main__":
    gam=game()
    gam.bid_phase()
    gam.playerts_action()
    gam.nilfgaard_phase()
    #n=nilfgaard(5,8)
    #n.set_invasion_plan()
    #b.add_fort_effect()
    #diplomatic_action(3,player1)
    #economic_action(3,player1)
    #economic_action(4,player1)
    #support('A',n.invasion_plan[0],'p1',3)
    #support('B',n.invasion_plan[1],'p2',1)
    #n.resolve_invasion()
    #for i in ind_prov_list:
    #    print(ind_prov_list[i].players_influence)