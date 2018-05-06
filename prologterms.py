"""
Prolog Terms

All Prolog data structures are called terms. A term is either:

 - A constant, which can be either an atom or a number.
 - A variable.
 - A compound term.

"""

import re


class Program(object):
    def __init__(self, *terms):
        self.terms = list(terms)

class Term(object):
    def __init__(self, pred, *args):
        self.pred = pred
        self.args = list(args)
        self.comments = []

    def add_comment(self, c):
        self.comments.append(c)
        
    # override <= to mean same as prolog :-
    def __le__(self, body):
        return Rule(self, body)
    
    # override % for comments
    def __mod__(self, comment):
        self.comments = [comment]
        return self

class Rule(Term):
    def __init__(self, head, body):
        """
        Arguments
        ---------
        head: Term
        body: tuple of Terms
        """
        self.pred = ':-'
        self.args = [head, body]
        self.comments = []

class Var(object):
    def __init__(self, name):
        self.name = name

class TermGenerator(object):
    def __getattr__(self, pred):
        def method(*args):
            return Term(pred, *args)
        return method

class PrologRenderer(object):
    def render(self, t):
        s=""
        if isinstance(t, Program):
            s = "{}".format("".join([self.render(x) + ".\n" for x in t.terms]))
        elif isinstance(t, Rule):
            head = self.render(t.args[0])
            bodyt = t.args[1]
            body = ""
            if isinstance(bodyt, tuple):
                body = "{}".format(", ".join([self.render(e) for e in bodyt]))
            else:
                body = self.render(bodyt)
            s = "{} :-\n    {}".format(head, body)
        elif isinstance(t, Var):
            s = "{}".format(t.name)
        elif isinstance(t, Term):
            s = "{}({})".format(t.pred, ", ".join([self.render(a) for a in t.args]))
        elif isinstance(t, list):
            s = "[{}]".format(", ".join([self.render(e) for e in t]))
        elif isinstance(t, tuple):
            s = "({})".format(", ".join([self.render(e) for e in t]))
        elif isinstance(t, str):
            s = "{}".format(t)
            if not re.match(r"^[a-z]\w*$", s):
                s = s.replace("'","\\'").replace("\n","\\n")
                s = "'{}'".format(s)
        else:
            s = "{}".format(t)
        # add comments
        if isinstance(t, Term) and len(t.comments) > 0:
            cmt = "".join(['% {}\n'.format(c) for c in t.comments])
            s = cmt + s
        return s

    
