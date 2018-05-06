|PyPI|

prologterms - a python library for constructing prolog terms
============================================================

Example::
   
    from prologterm import TermGenerator, PrologRenderer, Var
    
    X = Var('X')
    P = TermGenerator()
    term = P.member(X, [1, 2, 3])
    r = PrologRenderer()
    print(r.render(term))

writes::

   member(X, [1, 2, 3])

Usage
=====

This module is of little use by itself. It is intended to be used to
generate prolog programs that can be fed into a prolog execution
engine.

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
    
    
