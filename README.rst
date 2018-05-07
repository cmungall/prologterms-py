prologterms - a python library for constructing prolog terms
============================================================

Example::
   
    from prologterms import TermGenerator, PrologRenderer, Var
    
    X = Var('X')
    P = TermGenerator()
    term = P.member(X, [1, 2, 3])
    r = PrologRenderer()
    print(r.render(term))

writes::

   member(X, [1, 2, 3])

All prolog escaping conventions are handled automatically.

See the `Jupyter notebook <http://nbviewer.jupyter.org/github/cmungall/prologterms-py/tree/masterPrologTermsExamples.ipynb>`_
   
Rules
=====

The "<=" operator in python is overloaded to mean the same as prolog
":-". This means a rule object can be created as follows:

::
   
   P.ancestor(X,Y) <= (P.parent(X,Z), P.ancestor(Z,Y))

This can be done more explicitly using a Rule constructor:

::

   from prologterms import TermGenerator, PrologRenderer, Var, Rule

   X = Var('X')
   Y = Var('Y')
   Z = Var('Z')
   P = TermGenerator()
   rule = Rule(P.ancestor(X,Y), (P.parent(X,Z), P.ancestor(Z,Y))
   
Usage
=====

This module is of little use by itself. It is intended to be used to
generate prolog programs that can be fed into a prolog execution
engine.

- write prolog programs and queries to a file, and load these using an engine like swi-prolog
- through web services, e.g. via pengines
  
Pengines
========

[Note: requires latest pengines which may not be on pypi]

One of the intended applications is pengines

::
    
    from pengines.Builder import PengineBuilder
    from pengines.Pengine import Pengine
    from prologterms import TermGenerator, PrologRenderer, Program, Var
    
    P = TermGenerator()
    X = Var('X')
    Y = Var('Y')
    Z = Var('Z')
    R = PrologRenderer()
    
    p = Program(
        P.ancestor(X,Y) <= (P.parent(X,Z), P.ancestor(Z,Y)),
        P.ancestor(X,Y) <= P.parent(X,Y),
        P.parent('a','b'),
        P.parent('b','c'),
        P.parent('c','d')
    )
    
    q = P.ancestor(X,Y)
    
    factory = PengineBuilder(urlserver="http://localhost:4242",
                             srctext=R.render(p),
                             ask=R.render(q))
    pengine = Pengine(builder=factory, debug=True)
    while pengine.currentQuery.hasMore:
        pengine.doNext(pengine.currentQuery)
    for p in pengine.currentQuery.availProofs:
        print('{} <- {}'.format(p[X.name], p[Y.name]))
    
    
