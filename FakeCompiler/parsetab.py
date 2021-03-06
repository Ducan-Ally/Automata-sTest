
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA EQUAL INT LEFTPARENTHESIS METODO NAME NEWLINE PRINT RIGHTPARENTHESISFakeProgram : names EQUAL METODO LEFTPARENTHESIS INT RIGHTPARENTHESIS continuationFakeProgram : PRINT NAME continuationnames : NAME COMMA namesnames : NAMEcontinuation : NEWLINE FakeProgramcontinuation : emptyempty : '
    
_lr_action_items = {'PRINT':([0,10,],[3,3,]),'NAME':([0,3,7,10,],[4,6,4,4,]),'$end':([1,6,9,11,14,16,17,],[0,-7,-2,-6,-5,-7,-1,]),'EQUAL':([2,4,12,],[5,-4,-3,]),'COMMA':([4,],[7,]),'METODO':([5,],[8,]),'NEWLINE':([6,16,],[10,10,]),'LEFTPARENTHESIS':([8,],[13,]),'INT':([13,],[15,]),'RIGHTPARENTHESIS':([15,],[16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'FakeProgram':([0,10,],[1,14,]),'names':([0,7,10,],[2,12,2,]),'continuation':([6,16,],[9,17,]),'empty':([6,16,],[11,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> FakeProgram","S'",1,None,None,None),
  ('FakeProgram -> names EQUAL METODO LEFTPARENTHESIS INT RIGHTPARENTHESIS continuation','FakeProgram',7,'p_Start1','parser.py',15),
  ('FakeProgram -> PRINT NAME continuation','FakeProgram',3,'p_Start2','parser.py',19),
  ('names -> NAME COMMA names','names',3,'p_names1','parser.py',23),
  ('names -> NAME','names',1,'p_names2','parser.py',26),
  ('continuation -> NEWLINE FakeProgram','continuation',2,'p_continuation1','parser.py',29),
  ('continuation -> empty','continuation',1,'p_continuation2','parser.py',32),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',41),
]
