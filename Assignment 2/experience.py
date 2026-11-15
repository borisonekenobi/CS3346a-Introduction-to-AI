"""Recorded experience, not the full true transition model."""
EPISODES=[
 [('A','try',-1,'B',False),('B','send',6,'T',True)],
 [('A','try',-1,'A',False),('A','try',-1,'B',False),
  ('B','send',-2,'C',False),('C','reset',-1,'A',False),
  ('A','try',-1,'B',False),('B','send',6,'T',True)],
 [('A','try',-1,'B',False),('B','send',-2,'C',False),
  ('C','reset',-1,'A',False),('A','try',-1,'B',False),('B','send',6,'T',True)]
]
AVAILABLE={'A':('try','wait'),'B':('send','retry'),'C':('reset','send'),'T':()}
INITIAL_Q={('A','try'):1.,('A','wait'):.5,('B','send'):2.,('B','retry'):0.,
           ('C','reset'):-.5,('C','send'):0.}
Q_TRACE=[('B','send',-2.,'C',False),('A','try',-1.,'B',False),('B','send',6.,'T',True)]
