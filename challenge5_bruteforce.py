#from tabnanny import check

class expression:
    def __init__(self,exp):
        self.exp=exp
    def fix_broken_exp(self):
        self.stack=0
        self.balance=0
        for  _ in self.exp:
            if "("<= str(20) or ")"<=str(20) :
                return self.exp
            elif self.exp[_]==self.exp[_+1]=="(":
                self.exp.remove(1*"(")
                return self.exp
            elif self.exp[_]==self.exp[_+1]==")":
                self.exp.remove(1*")")
                return self.exp
            elif "(" is not None:
                self.exp.remove("(")
                return self.exp
            elif ")" is not None:
                self.exp.remove(")")
                return self.exp
            else:
                return self.exp
e=expression("((a))")
print(e.fix_broken_exp())