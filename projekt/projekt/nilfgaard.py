import __builtin__ as bt
import random
def check_builtin():
    tmp_lis=['army_list','prov_list','ind_prov_list','pl_list']
    try:
        for i in tmp_lis:
             if not hasattr(bt,i):
                 raise NameError
    except NameError:
        raise NameError
check_builtin()

class nilfgaard(object):
    power=0
    mages_power=0
    invasion_plan=[]
    bribed_prov=[]
    event_list=[]
    def __init__(self,power,mages_power):
        self.power=power
        self.mages_power=mages_power
        self.mages_aid = True
        self.event_list.append(self.event_0)
        self.event_list.append(self.event_1)
        self.event_list.append(self.event_2)
        self.event_list.append(self.event_3)
        self.event_list.append(self.event_4)
        self.event_list.append(self.event_5)
    def set_invasion_plan(self):
        ind_prov=[]
        for i in bt.ind_prov_list:
            ind_prov.append(bt.ind_prov_list[i])
        while True:
            if len(self.invasion_plan) == 2:
                break
            t=random.randint(0,len(ind_prov)-1)
            if not ind_prov[t].gebid('wq') and not ind_prov[t].gebid('pr_id') in self.invasion_plan:
                self.invasion_plan.append(ind_prov[t].gebid('pr_id'))
    def resolve_invasion(self):
        ind_prov=[]
        for i in self.invasion_plan:
            ind_prov.append(bt.ind_prov_list[i])
        for i in ind_prov:
            p_power=0
            print(i)
            print(i.support_army)
            for j in i.support_army:
                p_power+=bt.army_list[j].gebid('nos')
            print(p_power)
            if p_power < self.power:
                r=self.power-p_power
                p_power+=self._get_mage_power(r)
                if p_power == self.power:
                    print('prowincja '+i.name+" sie obronila!")
                    i.grant_influence()
                    for j in i.support_army:
                        del bt.army_list[j]
                    i.support_army=[]
                    bt.ind_prov_list[i.gebid('pr_id')]=i
                else:
                    print('prowincja '+i.name+ ' zostala podbita!')
                    i.was_conquested=True
                    for j in i.support_army:
                        del bt.army_list[j]
                    i.support_army=[]
                    bt.ind_prov_list[i.gebid('pr_id')]=i
                    return
    def _get_mage_power(self,amount):
        if self.mages_power < 1:
            return 0
        if self.mages_power-amount >= 0:
            self.mages_power-=amount
            return amount
        else:
            r_v=self.mages_power
            self.mages_power=0
            self.mages_aid=False
            print('uwaga, doszlo do buntu wsrod magow!')
            return r_v
    def roll_event(self,pl_id):
        intek=random.randint(0,5)
        return self.event_list[intek](pl_id)
    def event_0(self,pl_id):
        pl_list[pl_id].noble_happiness-=1
        if pl_list[pl_id].noble_happiness < 1:
            pl_list[pl_id].victory_points-=1
            pl_list[pl_id].noble_happiness=1
    def event_1(self,pl_id):
        pl_list[pl_id].lowborn_happiness-=1
        if pl_list[pl_id].lowborn_happiness < 1:
            pl_list[pl_id].skip_turn=True
            pl_list[pl_id].lowborn_happiness=1
        
    def event_2(self,pl_id):
        pl_list[pl_id].amount_of_gold-=1
        if pl_list[pl_id].amount_of_gold < 0:
            #decyzja czy podatki zbierane sa od szlachty (+2) czy plebsu (+1)
            pl_list[pl_id].amount_of_gold=1
    def event_3(self,pl_id):
        self.power+=1
    def event_4(self,pl_id):
        if self.mages_power > 0:
            self.mages_power-=1
        else:
            return self.roll_event(pl_id)
        if self.mages_power == 0:
            self.mages_aid=False
            print('uwaga, doszlo do buntu wsrod magow!')
    def event_5(self,pl_id):
        pass
    