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

def prov_creator(name,pr_id,pl_id,nos,pr_in,pr_val,lon):
    dic={}
    dic['name']=name
    if pr_id in bt.prov_list:
        raise KeyError('multi prov ids : '+pr_id)
    dic['pr_id']=pr_id
    
    for i in bt.pl_list:
        if i == pl_id:
            dic['pl_id']=pl_id
            break
    if not 'pl_id' in dic:
        raise KeyError('no such player! : '+pl_id)
    
    dic['nos']=nos
    dic['pr_in']=pr_in
    dic['pr_val']=pr_val
    for ID in lon:
        for i in bt.prov_list:
            if ID == i:
                error=True
                for i_ID in bt.prov_list[i].gebid('lon'):
                    if i_ID == pr_id:
                        error=False
                        break
                if error:
                    raise KeyError('prov '+ID+' has no neighbour called '+pr_id)
                break #czy cos to zepsuje?
    for i in bt.prov_list:
        for i_ID in bt.prov_list[i].gebid('lon'):
            if i_ID != pr_id:
                continue
            else:
                for k in lon:
                    error=True
                    if i == k:
                        error=False
                        break
                if error:
                    raise KeyError('prov '+pr_id+' has no neighbour called '+i)
                break #czy cos to zepsuje?
    dic['lon']=lon
    return province(dic)

def ind_prov_creator(name,pr_id,pr_val):
    dic={}
    dic['name']=name
    dic['pr_id']=pr_id
    dic['pr_val']=pr_val
    return ind_province(dic)
class province(object):
    name=''
    province_id=''
    player_id=''
    number_of_soldiers=0
    has_fort=False
    has_spy=False
    province_income=0
    province_value=0
    list_of_neigh=[]
    def __init__(self,data_dict):
        dt=data_dict 
        self.name=dt['name']
        self.province_id=dt['pr_id']
        self.player_id=dt['pl_id']
        self.number_of_soldiers=dt['nos']
        self.province_income=dt['pr_in']
        self.province_value=dt['pr_val']
        self.list_of_neigh=dt['lon']
        bt.prov_list[self.province_id]=self
    def _create_quick_access(self):
        qa={}
        qa['name']=self.name
        qa['pr_id']=self.province_id
        qa['pl_id']=self.player_id
        qa['nos']=self.number_of_soldiers
        qa['hf']=self.has_fort
        qa['hs']=self.has_spy
        qa['pr_in']=self.province_income
        qa['pr_val']=self.province_value
        qa['lon']=self.list_of_neigh
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
    def add_fort_effect(self):
        self.has_fort=True
    def remove_fort_effect(self):
        self.has_fort=False
        
        
class ind_province(object):
    name=""
    province_id=""
    province_value=0
    was_conquested=False
    def __init__(self,data_dict):
        dt=data_dict
        self.name=dt['name']
        self.province_id=dt['pr_id']
        self.province_value=dt['pr_val']
        self.players_influence={}
        for i in bt.pl_list:
            self.players_influence[i]=0
        self.support_army=[]
        bt.ind_prov_list[self.province_id]=self
    def _create_quick_access(self):
        qa={}
        qa['ar']=self.support_army
        qa['pl_inf']=self.players_influence
        qa['wq']=self.was_conquested
        qa['pr_val']=self.province_value
        qa['pr_id']=self.province_id
        qa['name']=self.name
        return qa
    def gebid(self,id):
        qa=self._create_quick_access()
        try:
            return qa[id]
        except:
            return 'error'
    def grant_influence(self):
        def get_highest(lista):
            if len(lista) == 0:
                return None
            h=lista[0]
            for i in lista:
                if bt.army_list[i].gebid('nos') > bt.army_list[h].gebid('nos'):
                    h=i
            return h
        a=get_highest(self.support_army)
        if a !=None:
            self.support_army.remove(a)
            iD=bt.army_list[a].gebid('pl_id')
            self.players_influence[iD]+=2
        b=get_highest(self.support_army)
        if b !=None:
            self.support_army.remove(b)
            iD=bt.army_list[b].gebid('pl_id')
            self.players_influence[iD]+=1
        