import random
import string
random.seed()
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

def generate_army_id():
    while True:
        u_id=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        for i in bt.army_list:
            if i == u_id:
                continue
        break
    return u_id

def army_creator(or_id,pr_id,pl_id,nos,ar_id):
    dic={}
    dic['pr_id']=pr_id
    dic['pl_id']=pl_id
    dic['ar_id']=ar_id
    dic['or_id']=or_id
    dic['nos']=nos
    bt.prov_list[or_id].number_of_soldiers-=nos
    return army(dic)

class army(object):
    province_id=''
    player_id=''
    army_id=''
    origin_id=''
    number_of_soldiers=0
    has_spy=False
    def __init__(self,data={}):
        self.province_id=data['pr_id']
        self.origin_id=data['or_id']
        self.player_id=data['pl_id']
        self.army_id=data['ar_id']
        self.number_of_soldiers=data['nos']
        bt.army_list[self.army_id]=self
    def _create_quick_access(self):
        qa={}
        qa['pr_id']=self.province_id
        qa['pl_id']=self.player_id
        qa['ar_id']=self.army_id
        qa['nos']=self.number_of_soldiers 
        qa['hs']=self.has_spy
        qa['or_id']=self.origin_id
        return qa
    def gebid(self,id):
        qa=self._create_quick_access()
        try:
            return qa[id]
        except:
            return 'error' 
    def add_spy_effect(self):
        self.has_spy=True
    def remove_spy_effect(self):
        self.has_spy=False
        
def dice_pow(dice):
        if dice < 3:return -1
        if dice > 4:return 1
        return 0

def battle_in_province(prov,army):
    arA=army.gebid('nos')
    arP=prov.gebid('nos')
    
    if army.has_spy:
        arA+=1
        army.has_spy=False
    else:
        arA+=dice_pow(random.randint(1,6))
    if prov.has_spy:
        arP+=1
        prov.has_spy=False
    else:
        arP+=dice_pow(random.randint(1,6))
        
    if prov.has_fort:
        arP+=1
        prov.number_of_soldiers+=1
    prov.has_fort=False
    while army.number_of_soldiers and prov.number_of_soldiers > 0:
        army.number_of_soldiers-=1
        prov.number_of_soldiers-=1
    print(arA,arP)
    if arA >= arP :
        prov.number_of_soldiers =army.number_of_soldiers
        prov.player_id=army.player_id
        print('prowincja zostala podbita!')
    else:
        print('prowincja sie obronila!')    
    return prov


def attack(prov_id,target_id,player_id,amount):
    am=amount
    prov=None
    if prov_id in bt.prov_list:
        prov=bt.prov_list[prov_id]
    if prov == None:
        print('province not found!')
        return
    if prov.player_id != player_id:
        print('that province doesnt belong to you!')
        return
    if prov.number_of_soldiers < am:
        print('not enough soldiers in the province!')
        return
    for i in prov.gebid('lon'):
        if i == target_id:
            bt.prov_list[prov_id].number_of_soldiers-=am
            army_creator(prov_id,target_id,player_id,am)
            return

def support(prov_id,target_id,player_id,amount):
    am=amount
    prov=None
    if prov_id in bt.prov_list:
        prov=bt.prov_list[prov_id]
    if prov == None:
        print('province not found!')
        return
    if prov.player_id != player_id:
        print('that province doesnt belong to you!')
        return
    
    ind_prov=None
    if target_id in bt.ind_prov_list:
        ind_prov= bt.ind_prov_list[target_id]
        
    if ind_prov == None:
        print('ta prowincja nie istnieje! : ')
        return
    if ind_prov.gebid('wq'):
        print('prowincja zostala juz podbita')
        return
    if amount > prov.gebid('nos'):
        print('w prowincji nie ma tylu zolnierzy!')
        return
    ar_id=generate_army_id()
    bt.ind_prov_list[target_id].support_army.append(ar_id)
    army_creator(prov_id,target_id,player_id,amount,ar_id)
def spy_decision(pl1,pl2):
    try:
        dec1=input('czy gracz '+pl1.player_id +' uzywa szpiega? ')
        dec1=bool(int(dec1))
        dec2=input('czy gracz '+pl2.player_id +' uzywa szpiega? ')
        dec2=bool(int(dec2))
        
    except Exception:
        spy_decision(pl1,pl2)
        return
    if dec1:
        pl1.has_spy=True
    if dec2:
        pl2.has_spy=True
    
def battle_search():
    for i in bt.prov_list:
        for j in bt.army_list:
            if prov_list[i].gebid('pr_id') == army_list[j].gebid('pr_id'):
                pr=prov_list[i]
                ar=army_list[j]
                print('bitwa w prowincji '+pr.gebid('pr_id')+' miedzy '+pr.gebid('pl_id')
                +' a '+ar.gebid('pl_id'))
                spy_decision(pr,ar)
                pr=battle_in_province(pr,ar)
                bt.prov_list[i]=pr
                del bt.army_list[j]
                return battle_search()