import __builtin__ as bt

def check_builtin():
    tmp_lis=['army_list','prov_list','ind_prov_list','pl_list']
    try:
        for i in tmp_lis:
             if not hasattr(bt,i):
                 raise NameError
    except NameError:
        raise NameError
check_builtin()

class player(object):
    name=''
    player_id=''
    fraction=''
    amount_of_gold=3
    victory_points=0
    lowborn_happiness=5
    noble_happiness=5
    amount_of_spies=0
    soldiers_total=0
    longterm_fund=False
    skip_turn=False
    actions_left=2
    def __init__(self,name,player_id,fraction):
        for i in bt.pl_list:
            if i == player_id:
                raise KeyError('multiple key in players : '+player_id)
        self.player_id=player_id
        self.name=name
        self.fraction=fraction
        bt.pl_list[player_id]=self
    def _create_quick_access(self):
        qa={}
        qa['name']=self.name
        qa['frac']=self.fraction
        qa['pl_id']=self.player_id
        qa['stot']=self.soldiers_total
        qa['aos']=self.amount_of_spies
        qa['aog']=self.amount_of_gold
        qa['lh']=self.lowborn_happiness
        qa['nh']=self.noble_happiness
        qa['vp']=self.victory_points
        tmp=[]
        for i in bt.army_list:
            if bt.army_list[i].gebid('pl_id') == self.player_id:
                tmp.append(bt.army_list[i])
        qa['army']=tmp
        tmp=[]
        for i in bt.prov_list:
            if bt.prov_list[i].gebid('pl_id') == self.player_id:
                tmp.append(bt.prov_list[i])
        qa['prov']=tmp
        return qa
    def gebid(self,id):
        qa=self._create_quick_access()
        try:
            return qa[id]
        except:
            return 'error'
    def add_longterm_fund_effect(self):
        self.longterm_funds=True
                    