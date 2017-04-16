
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'C5F8FE0096C8F33DAD6033EE53283DC9'
    
_lr_action_items = {'CREATEPACKAGE':([0,],[13,]),'DESTINATIONS':([0,],[14,]),'FLIGHTS':([0,],[15,]),'FLY':([0,],[16,]),'HOTELS':([0,],[17,]),'RESERVE':([0,],[18,]),'STAY':([0,],[19,]),'CARS':([0,],[20,]),'TOURS':([0,],[21,]),'VISIT':([0,],[22,]),'BOOK':([0,],[23,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,14,23,27,29,30,31,33,35,36,37,38,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-13,-22,-16,-18,-19,-20,-12,-15,-17,-21,-14,]),'NAME':([13,24,],[24,33,]),'XX':([15,16,17,20,21,22,26,],[25,26,27,30,31,32,35,]),'RENTAL':([18,],[28,]),'HOTEL':([19,],[29,]),'DATE':([25,34,],[34,38,]),'DAYS':([28,],[36,]),'TOUR':([32,],[37,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'statement_createpackage':([0,],[2,]),'statement_destinations':([0,],[3,]),'statement_flights':([0,],[4,]),'statement_fly':([0,],[5,]),'statement_hotels':([0,],[6,]),'statement_reserve':([0,],[7,]),'statement_stay':([0,],[8,]),'statement_cars':([0,],[9,]),'statement_tours':([0,],[10,]),'statement_visit':([0,],[11,]),'statement_book':([0,],[12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> statement_createpackage','statement',1,'p_statement','VoyageYacc.py',15),
  ('statement -> statement_destinations','statement',1,'p_statement','VoyageYacc.py',16),
  ('statement -> statement_flights','statement',1,'p_statement','VoyageYacc.py',17),
  ('statement -> statement_fly','statement',1,'p_statement','VoyageYacc.py',18),
  ('statement -> statement_hotels','statement',1,'p_statement','VoyageYacc.py',19),
  ('statement -> statement_reserve','statement',1,'p_statement','VoyageYacc.py',20),
  ('statement -> statement_stay','statement',1,'p_statement','VoyageYacc.py',21),
  ('statement -> statement_cars','statement',1,'p_statement','VoyageYacc.py',22),
  ('statement -> statement_tours','statement',1,'p_statement','VoyageYacc.py',23),
  ('statement -> statement_visit','statement',1,'p_statement','VoyageYacc.py',24),
  ('statement -> statement_book','statement',1,'p_statement','VoyageYacc.py',25),
  ('statement_createpackage -> CREATEPACKAGE NAME NAME','statement_createpackage',3,'p_statement_createpackage','VoyageYacc.py',31),
  ('statement_destinations -> DESTINATIONS','statement_destinations',1,'p_statement_destinations','VoyageYacc.py',37),
  ('statement_flights -> FLIGHTS XX DATE DATE','statement_flights',4,'p_statement_flights','VoyageYacc.py',42),
  ('statement_fly -> FLY XX XX','statement_fly',3,'p_statement_fly','VoyageYacc.py',48),
  ('statement_hotels -> HOTELS XX','statement_hotels',2,'p_statement_hotels','VoyageYacc.py',54),
  ('statement_reserve -> RESERVE RENTAL DAYS','statement_reserve',3,'p_statement_reserve','VoyageYacc.py',60),
  ('statement_stay -> STAY HOTEL','statement_stay',2,'p_statement_stay','VoyageYacc.py',66),
  ('statement_cars -> CARS XX','statement_cars',2,'p_statement_cars','VoyageYacc.py',72),
  ('statement_tours -> TOURS XX','statement_tours',2,'p_statement_tours','VoyageYacc.py',78),
  ('statement_visit -> VISIT XX TOUR','statement_visit',3,'p_statement_visit','VoyageYacc.py',84),
  ('statement_book -> BOOK','statement_book',1,'p_statement_book','VoyageYacc.py',90),
]
