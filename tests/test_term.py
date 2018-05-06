from prologterms import TermGenerator, PrologRenderer, Program, Var

P = TermGenerator()
X = Var('X')
Y = Var('Y')
Z = Var('Z')
R = PrologRenderer()

def test_term():
    t = P.member(X, [1, 2, 3])
    print("TERM: {}\n".format(R.render(t)))
    assert R.render(t) == "member(X, [1, 2, 3])"

def test_quote():
    t = P.member(X, ['a', 'B', '$c', '.d', '', ' ', "'x'", "foo\n\n'bar'"])
    print("TERM: {}\n".format(R.render(t)))
    assert R.render(t) == "member(X, [a, 'B', '$c', '.d', '', ' ', '\\'x\\'', 'foo\\n\\n\\'bar\\''])"

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
    
    
