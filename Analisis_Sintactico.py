import ply.yacc as yacc
import os
import codecs
import re
from Analisis_Lexico import tokens
from sys import stdin

precedence = (
    ('right', 'ASSIGN'),
    ('right','UPDATE'),
    ('left','NE'),
    ('left','LT','LTE','GT','GTE'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','ODD'),
    ('left','LPARENT','RPARENT'),
    )
