
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'SLR'

_lr_signature = 'rightIDCALLBEGINIFWHILErightPROCEDURErightVARrightASSIGNrightUPDATEleftNEleftLTLTEGTGTEleftPLUSMINUSleftTIMESDIVIDErightODDleftLPARENTRPARENTASSIGN BEGIN CALL COMMA CONST DIVIDE DO DOT ELSE END GT GTE ID IF IN LPARENT LT LTE MINUS NE NUMBER ODD OUT PLUS PROCEDURE RPARENT SEMMICOLOM THEN TIMES UPDATE VAR WHILEprogram : blockblock : constDecl varDecl procDecl statementconstDecl : CONST constAssignmentList SEMMICOLOMconstDecl : emptyconstAssignmentList : ID ASSIGN NUMBERconstAssignmentList : constAssignmentList COMMA ID ASSIGN NUMBERvarDecl : VAR identList SEMMICOLOMvarDecl : emptyidentList : IDidentList : identList COMMA IDprocDecl : procDecl PROCEDURE ID SEMMICOLOM block SEMMICOLOMprocDecl : emptystatement : ID UPDATE expressionstatement : CALL IDstatement : BEGIN statementList ENDstatement : IF condition THEN statementstatement : WHILE condition DO statementstatement : emptystatementList : statementstatementList : statementList SEMMICOLOM statementcondition : ODD expressioncondition : expression relation expressionrelation : ASSIGNrelation : NErelation : LTrelation : GTrelation : LTErelation : GTEexpression : termexpression : addingOperator termexpression : expression addingOperator termterm : factorterm : term multiplyingOperator factoraddingOperator : PLUSaddingOperator : MINUSmultiplyingOperator : TIMESmultiplyingOperator : DIVIDEfactor : IDfactor : NUMBERfactor : LPARENT expression RPARENTempty :'
    
_lr_action_items = {'CONST':([0,49,],[4,4,]),'VAR':([0,3,5,6,11,15,22,49,52,53,68,],[-41,7,-4,-41,-41,-3,-41,-41,-41,-41,-41,]),'PROCEDURE':([0,3,5,6,8,11,12,15,22,26,49,52,53,68,78,],[-41,-41,-4,-41,-8,19,-12,-3,-41,-7,-41,-41,-41,-41,-11,]),'ID':([0,3,4,5,6,7,8,11,12,15,16,19,21,22,23,24,26,27,31,36,39,41,42,45,49,52,53,55,56,57,58,59,60,61,62,63,64,65,68,78,],[-41,-41,10,-4,-41,14,-8,20,-12,-3,28,30,32,20,43,43,-7,47,43,43,43,-34,-35,43,-41,20,20,43,43,-23,-24,-25,-26,-27,-28,43,-36,-37,20,-11,]),'CALL':([0,3,5,6,8,11,12,15,22,26,49,52,53,68,78,],[-41,-41,-4,-41,-8,21,-12,-3,21,-7,-41,21,21,21,-11,]),'BEGIN':([0,3,5,6,8,11,12,15,22,26,49,52,53,68,78,],[-41,-41,-4,-41,-8,22,-12,-3,22,-7,-41,22,22,22,-11,]),'IF':([0,3,5,6,8,11,12,15,22,26,49,52,53,68,78,],[-41,-41,-4,-41,-8,23,-12,-3,23,-7,-41,23,23,23,-11,]),'WHILE':([0,3,5,6,8,11,12,15,22,26,49,52,53,68,78,],[-41,-41,-4,-41,-8,24,-12,-3,24,-7,-41,24,24,24,-11,]),'$end':([0,1,2,3,5,6,8,11,12,15,18,22,25,26,32,38,40,43,44,49,50,51,52,53,66,68,72,74,75,76,77,78,],[-41,0,-1,-41,-4,-41,-8,-41,-12,-3,-2,-41,-18,-7,-14,-29,-32,-38,-39,-41,-13,-15,-41,-41,-30,-41,-16,-31,-33,-40,-17,-11,]),'SEMMICOLOM':([0,3,5,6,8,9,11,12,13,14,15,18,22,25,26,29,30,32,33,34,38,40,43,44,47,49,50,51,52,53,66,68,69,70,71,72,74,75,76,77,78,],[-41,-41,-4,-41,-8,15,-41,-12,26,-9,-3,-2,-41,-18,-7,-5,49,-14,52,-19,-29,-32,-38,-39,-10,-41,-13,-15,-41,-41,-30,-41,-6,78,-20,-16,-31,-33,-40,-17,-11,]),'END':([0,3,6,11,22,25,32,33,34,38,40,43,44,49,50,51,52,53,66,68,71,72,74,75,76,77,],[-41,-41,-41,-41,-41,-18,-14,51,-19,-29,-32,-38,-39,-41,-13,-15,-41,-41,-30,-41,-20,-16,-31,-33,-40,-17,]),'COMMA':([9,13,14,29,47,69,],[16,27,-9,-5,-10,-6,]),'ASSIGN':([10,28,37,38,40,43,44,66,74,75,76,],[17,48,57,-29,-32,-38,-39,-30,-31,-33,-40,]),'NUMBER':([17,23,24,31,36,39,41,42,45,48,55,56,57,58,59,60,61,62,63,64,65,],[29,44,44,44,44,44,-34,-35,44,69,44,44,-23,-24,-25,-26,-27,-28,44,-36,-37,]),'UPDATE':([20,],[31,]),'ODD':([23,24,],[36,36,]),'PLUS':([23,24,31,36,37,38,40,43,44,45,50,54,55,57,58,59,60,61,62,66,67,73,74,75,76,],[41,41,41,41,41,-29,-32,-38,-39,41,41,41,41,-23,-24,-25,-26,-27,-28,-30,41,41,-31,-33,-40,]),'MINUS':([23,24,31,36,37,38,40,43,44,45,50,54,55,57,58,59,60,61,62,66,67,73,74,75,76,],[42,42,42,42,42,-29,-32,-38,-39,42,42,42,42,-23,-24,-25,-26,-27,-28,-30,42,42,-31,-33,-40,]),'LPARENT':([23,24,31,36,39,41,42,45,55,56,57,58,59,60,61,62,63,64,65,],[45,45,45,45,45,-34,-35,45,45,45,-23,-24,-25,-26,-27,-28,45,-36,-37,]),'THEN':([35,38,40,43,44,54,66,73,74,75,76,],[53,-29,-32,-38,-39,-21,-30,-22,-31,-33,-40,]),'NE':([37,38,40,43,44,66,74,75,76,],[58,-29,-32,-38,-39,-30,-31,-33,-40,]),'LT':([37,38,40,43,44,66,74,75,76,],[59,-29,-32,-38,-39,-30,-31,-33,-40,]),'GT':([37,38,40,43,44,66,74,75,76,],[60,-29,-32,-38,-39,-30,-31,-33,-40,]),'LTE':([37,38,40,43,44,66,74,75,76,],[61,-29,-32,-38,-39,-30,-31,-33,-40,]),'GTE':([37,38,40,43,44,66,74,75,76,],[62,-29,-32,-38,-39,-30,-31,-33,-40,]),'DO':([38,40,43,44,46,54,66,73,74,75,76,],[-29,-32,-38,-39,68,-21,-30,-22,-31,-33,-40,]),'RPARENT':([38,40,43,44,66,67,74,75,76,],[-29,-32,-38,-39,-30,76,-31,-33,-40,]),'TIMES':([38,40,43,44,66,74,75,76,],[64,-32,-38,-39,64,64,-33,-40,]),'DIVIDE':([38,40,43,44,66,74,75,76,],[65,-32,-38,-39,65,65,-33,-40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block':([0,49,],[2,70,]),'constDecl':([0,49,],[3,3,]),'empty':([0,3,6,11,22,49,52,53,68,],[5,8,12,25,25,5,25,25,25,]),'varDecl':([3,],[6,]),'constAssignmentList':([4,],[9,]),'procDecl':([6,],[11,]),'identList':([7,],[13,]),'statement':([11,22,52,53,68,],[18,34,71,72,77,]),'statementList':([22,],[33,]),'condition':([23,24,],[35,46,]),'expression':([23,24,31,36,45,55,],[37,37,50,54,67,73,]),'term':([23,24,31,36,39,45,55,56,],[38,38,38,38,66,38,38,74,]),'addingOperator':([23,24,31,36,37,45,50,54,55,67,73,],[39,39,39,39,56,39,56,56,39,56,56,]),'factor':([23,24,31,36,39,45,55,56,63,],[40,40,40,40,40,40,40,40,75,]),'relation':([37,],[55,]),'multiplyingOperator':([38,66,74,],[63,63,63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> block','program',1,'p_program','Analisis_Sintactico.py',23),
  ('block -> constDecl varDecl procDecl statement','block',4,'p_block','Analisis_Sintactico.py',28),
  ('constDecl -> CONST constAssignmentList SEMMICOLOM','constDecl',3,'p_constDecl','Analisis_Sintactico.py',32),
  ('constDecl -> empty','constDecl',1,'p_constDeclEmpty','Analisis_Sintactico.py',37),
  ('constAssignmentList -> ID ASSIGN NUMBER','constAssignmentList',3,'p_constAssignmentList1','Analisis_Sintactico.py',42),
  ('constAssignmentList -> constAssignmentList COMMA ID ASSIGN NUMBER','constAssignmentList',5,'p_constAssignmentList2','Analisis_Sintactico.py',46),
  ('varDecl -> VAR identList SEMMICOLOM','varDecl',3,'p_varDecl1','Analisis_Sintactico.py',50),
  ('varDecl -> empty','varDecl',1,'p_varDeclEmpty','Analisis_Sintactico.py',54),
  ('identList -> ID','identList',1,'p_identList1','Analisis_Sintactico.py',58),
  ('identList -> identList COMMA ID','identList',3,'p_identList2','Analisis_Sintactico.py',62),
  ('procDecl -> procDecl PROCEDURE ID SEMMICOLOM block SEMMICOLOM','procDecl',6,'p_procDecl1','Analisis_Sintactico.py',66),
  ('procDecl -> empty','procDecl',1,'p_procDeclEmpty','Analisis_Sintactico.py',70),
  ('statement -> ID UPDATE expression','statement',3,'p_statement1','Analisis_Sintactico.py',74),
  ('statement -> CALL ID','statement',2,'p_statement2','Analisis_Sintactico.py',78),
  ('statement -> BEGIN statementList END','statement',3,'p_statement3','Analisis_Sintactico.py',82),
  ('statement -> IF condition THEN statement','statement',4,'p_statement4','Analisis_Sintactico.py',86),
  ('statement -> WHILE condition DO statement','statement',4,'p_statement5','Analisis_Sintactico.py',90),
  ('statement -> empty','statement',1,'p_statementEmpty','Analisis_Sintactico.py',94),
  ('statementList -> statement','statementList',1,'p_statementList1','Analisis_Sintactico.py',98),
  ('statementList -> statementList SEMMICOLOM statement','statementList',3,'p_statementList2','Analisis_Sintactico.py',102),
  ('condition -> ODD expression','condition',2,'p_condition1','Analisis_Sintactico.py',106),
  ('condition -> expression relation expression','condition',3,'p_condition2','Analisis_Sintactico.py',110),
  ('relation -> ASSIGN','relation',1,'p_relation1','Analisis_Sintactico.py',114),
  ('relation -> NE','relation',1,'p_relation2','Analisis_Sintactico.py',118),
  ('relation -> LT','relation',1,'p_relation3','Analisis_Sintactico.py',122),
  ('relation -> GT','relation',1,'p_relation4','Analisis_Sintactico.py',126),
  ('relation -> LTE','relation',1,'p_relation5','Analisis_Sintactico.py',130),
  ('relation -> GTE','relation',1,'p_relation6','Analisis_Sintactico.py',134),
  ('expression -> term','expression',1,'p_expression1','Analisis_Sintactico.py',138),
  ('expression -> addingOperator term','expression',2,'p_expression2','Analisis_Sintactico.py',142),
  ('expression -> expression addingOperator term','expression',3,'p_expression3','Analisis_Sintactico.py',146),
  ('term -> factor','term',1,'p_term1','Analisis_Sintactico.py',150),
  ('term -> term multiplyingOperator factor','term',3,'p_term2','Analisis_Sintactico.py',154),
  ('addingOperator -> PLUS','addingOperator',1,'p_addingOperator1','Analisis_Sintactico.py',158),
  ('addingOperator -> MINUS','addingOperator',1,'p_addingOperator2','Analisis_Sintactico.py',162),
  ('multiplyingOperator -> TIMES','multiplyingOperator',1,'p_multiplyingOperator1','Analisis_Sintactico.py',166),
  ('multiplyingOperator -> DIVIDE','multiplyingOperator',1,'p_multiplyingOperator2','Analisis_Sintactico.py',170),
  ('factor -> ID','factor',1,'p_factor1','Analisis_Sintactico.py',174),
  ('factor -> NUMBER','factor',1,'p_factor2','Analisis_Sintactico.py',178),
  ('factor -> LPARENT expression RPARENT','factor',3,'p_factor3','Analisis_Sintactico.py',182),
  ('empty -> <empty>','empty',0,'p_empty','Analisis_Sintactico.py',186),
]
