# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
import __builtin__
__builtin__.army_list={}
__builtin__.prov_list={}
__builtin__.ind_prov_list={}
__builtin__.pl_list={}
from player import *
from map_of_world import *
from army import *

class Test_Basic(unittest.TestCase):
    def test_player(self):
        __builtin__.pl_list={}
        player('kuba','p1','nan')
        for i in __builtin__.pl_list:
            self.assertEqual(i,'p1')
        lis=__builtin__.pl_list
        self.assertEqual(lis[i].gebid('name'),'kuba')
        self.assertEqual(lis[i].gebid('pl_id'),'p1')
        self.assertEqual(lis[i].fraction,'nan')
        with self.assertRaises(KeyError) as context:
            player('kuba','p1','nan')
        self.assertTrue('multiple key in players : p1' in context.exception)
        player('marks','p2','nan')
        self.assertEqual(2,len(__builtin__.pl_list))
    def test_map_of_world(self):
        __builtin__.pl_list={}
        player('kuba','p1','nan')
        prov_creator('A','A','p1',5,4,3,['A','B'])
        for i in __builtin__.prov_list:
            self.assertEqual(i,'A')
        lis=__builtin__.prov_list
        self.assertEqual(lis[i].gebid('name'),'A')
        self.assertEqual(lis[i].gebid('pr_id'),'A')
        self.assertEqual(lis[i].gebid('pl_id'),'p1')
        self.assertEqual(lis[i].gebid('nos'),5)
        self.assertEqual(lis[i].gebid('pr_in'),4)
        self.assertEqual(lis[i].gebid('pr_val'),3)
        with self.assertRaises(KeyError) as context:
            prov_creator('A','A','p1',5,4,3,['A','B'])
        
        with self.assertRaises(KeyError) as context:
            prov_creator('B','B','p2',5,4,3,['A','B'])
       
        __builtin__.prov_list={}
        prov_creator('A','A','p1',5,4,3,['C','B'])
        prov_creator('B','B','p1',5,4,3,['A','C','E','D'])
        prov_creator('C','C','p1',5,4,3,['A','B','D'])
        with self.assertRaises(KeyError) as context:
            prov_creator('D','D','p1',5,4,3,['C','E'])
        prov_creator('D','D','p1',5,4,3,['C','B','E'])
        with self.assertRaises(KeyError) as context:
            prov_creator('E','E','p1',5,4,3,['B'])
        prov_creator('E','E','p1',5,4,3,['B','D'])
if __name__ == '__main__':
    unittest.main()

