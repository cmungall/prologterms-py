from prologterms import TermGenerator, PrologRenderer, Program, Var, SExpressionRenderer

P = TermGenerator()
X = Var('X')
Y = Var('Y')
Z = Var('Z')
R = PrologRenderer()
S = SExpressionRenderer()

def test_term():
    t = P.member(X, [1, 2, 3])
    print("TERM: {}\n".format(R.render(t)))
    assert R.render(t) == "member(X, [1, 2, 3])"
    assert S.render(t) == "(member ?X (list 1 2 3))"

def test_atom():
    t = P.foo()
    print("TERM: {}\n".format(R.render(t)))
    assert R.render(t) == "foo"
    assert S.render(t) == "(foo )"

def test_unary_neg():
    t = (-X)
    print("TERM: {}\n".format(R.render(t)))
    assert R.render(t) == "-(X)"
    assert S.render(t) == "(- ?X)"
    
def test_not():
    t = (~ P.true())
    print("TERM: {}\n".format(R.render(t)))
    assert R.render(t) == "\+(true)"
    assert S.render(t) == "(\+ (true ))"
    
def test_eq():
    t = (X == Y)
    print("TERM: {}\n".format(R.render(t)))
    assert R.render(t) == "=(X, Y)"
    assert S.render(t) == "(= ?X ?Y)"

def test_ne():
    t = (X != Y)
    print("TERM: {}\n".format(R.render(t)))
    assert R.render(t) == "\=(X, Y)"
    assert S.render(t) == "(\= ?X ?Y)"

def test_quote():
    t = P.member(X, ['a', 'B', '$c', '.d', '', ' ', "'x'", "foo\n\n'bar'"])
    print("TERM: {}\n".format(R.render(t)))
    assert R.render(t) == "member(X, [a, 'B', '$c', '.d', '', ' ', '\\'x\\'', 'foo\\n\\n\\'bar\\''])"
    assert S.render(t) == "(member ?X (list a 'B' '$c' '.d' '' ' ' '\\'x\\'' 'foo\\n\\n\\'bar\\''))"

def test_comments():
    t = P.member(X, [1, 2, 3])
    t.add_comment('foo')
    print('Term with comments:')
    print("TERM: {}\n".format(R.render(t)))
    assert R.render(t) == "% foo\nmember(X, [1, 2, 3])"

def test_comments_infix():
    t = P.member(X, [1, 2, 3]) % 'foo'
    print('Term with comments:')
    print("TERM: {}\n".format(R.render(t)))
    assert R.render(t) == "% foo\nmember(X, [1, 2, 3])"
    
def test_program():
    p = Program(
        P.ancestor(X,Y) <= (P.parent(X,Z), P.ancestor(Z,Y)),
        P.ancestor(X,Y) <= P.parent(X,Z),
        P.parent('a','b'),
        P.parent('b','c'),
        P.parent('c','d')
        )
    print('PROG:\n')
    print(R.render(p))

def test_program_infix_comments():
    p = Program(
        (P.ancestor(X,Y) <= (P.parent(X,Z), P.ancestor(Z,Y))) % 'recursive',
        (P.ancestor(X,Y) <= P.parent(X,Z)) % 'base case',
        P.parent('a','b') % 'a isa b',
        P.parent('b','c') % 'b isa c',
        P.parent('c','d') % 'c isa d'
        )
    print('PROG:\n')
    print(R.render(p))
    
    
