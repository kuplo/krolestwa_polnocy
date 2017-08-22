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

def military_action(typ,player):
    if typ == 1:
        u_type=raw_input('typ: ')
        am=input('ile: ')
        p_id=raw_input('id: ')
        try:
            am=int(am)
            prov=None
            for i in bt.prov_list:
                if i == p_id:
                    if bt.prov_list[i].gebid('pl_id') == player.gebid('pl_id'):
                        prov=bt.prov_list[i]
                        break
            print(prov)
            print(u_type)
            if prov==None:
                raise NameError
            if u_type != 'mercenary' and u_type != 'lowborn' and u_type != 'noble':
                raise NameError
        except NameError:
            military_action(typ,player)
            return
        r=0
        if u_type == 'mercenary':
            gold=player.amount_of_gold
            while r != am:
                if gold-2 < 0:
                    break
                gold-=2
                r+=1
            prov.number_of_soldiers+=r
            player.amount_of_gold=gold
        if u_type == 'lowborn':
            gold=player.amount_of_gold
            lh=player.lowborn_happiness
            while r != am:
                if gold == 0 or lh == 1 :
                    break
                gold-=1
                lh-=1
                r+=1
            prov.number_of_soldiers+=r
            player.amount_of_gold=gold
            player.lowborn_happiness=lh
        if u_type == 'noble':
            nh=player.noble_happiness
            while r != am:
                if nh == 1:
                    break
                nh-=1
                r+=1
            prov.number_of_soldiers+=r
            player.noble_happiness=nh

    if typ == 2:
        p_id=raw_input('id: ')
        try:
            prov=None
            for i in player.provinces:
                if i.gebid('pr_id') == p_id:
                    prov=i
                    break
            if prov==None:
                raise NameError
        except Exception:
            military_action(typ,player)
            return
        if prov.gebid('hs'):
            return
        if player.amount_of_gold > 0:
            player.amount_of_gold -=1
            prov.add_fort_effect()

def diplomatic_action(typ,player):
    if typ == 1:
        pass
    if typ == 2:
        pass
    if typ == 3:
        player.amount_of_spies+=1

def economic_action(typ,player):
    if typ == 1:
        if player.gebid('nh') < 5:
            player.noble_happiness+=1
    if typ == 2:
        if player.gebid('lh') < 5:
            player.lowborn_happiness+=1
    if typ == 3:
        player.amount_of_gold+=2
    if typ == 4:
        player.add_longterm_fund_effect()
    if typ == 5:
        pass
        