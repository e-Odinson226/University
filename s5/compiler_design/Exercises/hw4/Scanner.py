# Scanner---------------------
class Scanner:
    num_stack = ''
    ch = 0
    pointer = 0
    grammar = {
        '^id':'^id',
        'byte':'byte',
        'integer':'integer',
        'num':'num',
        '..':'dotdot',
        'array':'array',
        'obracket':'obracket',
        'cbracket':'cbracket',
        'of':'of',
        '$':'EOF',
        'lexicalError':'lexicalError'
        }
    num_sign = ['-', '+']
    whites = ['\n', '\t', ' ']
    
    def buffer_set(self, string):
        self.string = string+"$"
    
    def buffer_get(self):
        #print(f"Char  :[{self.ch}]")
        dash = ''
        for d in range (self.pointer-1):
            dash += ' '
            
        print(f"String  :{self.string}")
        print(f"Pointer :{dash}^")
        print(f"Pointer :{self.pointer}\n")

    def lexicalError(self):
        return(self.grammar['lexicalError'])
        
    def by_pass(self):
        while not(self.ch == ' ' or self.ch == '\n' or self.ch == '\t'):
            self.nextchar()
        self.revert()
        
    def nextchar(self):
        self.ch = self.string[self.pointer]
        self.pointer += 1
        #self.string = self.string[self.pointer+1:]
        return self.ch
    
    def revert(self):
        self.pointer -= 1

    def is_whitespace(self):
        self.look_ahead = self.string[self.pointer]
        if (self.look_ahead in self.whites) or (self.look_ahead == '$'):
            return True
        else:
            return False
        
    def get_token(self):
        state = 0
        if self.pointer < len(self.string):
            while True:
                match state:
                    case 0:
                        self.nextchar()
                        #self.buffer_get()
                        
                        if self.ch == '^':
                            state = 1
                        elif self.ch == 'b':
                            state = 2
                        elif self.ch == 'i':
                            state = 3
                        elif (self.ch in self.num_sign) or (self.ch.isdigit()):
                            state = 4
                        elif self.ch == 'a':
                            state = 5
                        elif (self.ch==' ') or (self.ch=="\t") or (self.ch=='\n'):
                            state = 6
                        elif self.ch == '.':
                            state = 7
                        elif (self.ch=='['):
                            state = 8
                        elif (self.ch ==']'):
                            state = 9
                        elif (self.ch =='o'):
                            state = 10
                        elif self.ch=='$':
                            state = 11
                        else:
                            return(self.lexicalError())
                            break
                    case 1:
                        #print("------------\t\tCASE 1\t\t------------")
                        self.nextchar()
                        try:
                            if self.ch == 'i':
                                self.nextchar()
                                if self.ch == 'd' and self.is_whitespace():
                                    return self.grammar['^id']
                        except:
                            self.by_pass()
                            return(self.lexicalError())
                            break
                    case 2:
                        #print("------------\t\tCASE 2\t\t------------")
                        self.nextchar()
                        #self.buffer_get()
                        if self.ch == 'y':
                            self.nextchar()
                            if self.ch == 't':
                                self.nextchar()
                                if self.ch == 'e' and self.is_whitespace():
                                    return self.grammar['byte']
                        self.by_pass()
                        return(self.lexicalError())
                        break
                    case 3:
                        #print("------------\t\tCASE 3\t\t------------")
                        self.nextchar()
                        #self.buffer_get()
                        if self.ch == 'n':
                            self.nextchar()
                            if self.ch == 't':
                                self.nextchar()
                                if self.ch == 'e':
                                    self.nextchar()
                                    if self.ch == 'g':
                                        self.nextchar()
                                        if self.ch == 'e':
                                            self.nextchar()
                                            if self.ch == 'r' and self.is_whitespace():
                                                return self.grammar['integer']
                        self.by_pass()
                        return(self.lexicalError())                    
                        break
                    case 4:
                        #print("------------\t\tCASE 4\t\t------------")
                        self.num_stack = ''
                        self.num_stack += self.ch
                        #print(f"B1 W -- checking {self.string[self.pointer]} is whitespace:{self.is_whitespace()}")
                        #print(f"B1 W -- checking {self.ch} is {self.string[self.pointer]}")
                        self.nextchar()
                        while self.ch.isdigit():
                            #print(f"ch:{self.ch}, pointer: {self.string[self.pointer]}\nIs whitespace:{self.is_whitespace()}")
                            self.num_stack += self.ch
                            if self.is_whitespace():
                                state = 0
                                #return self.num_stack
                                return self.grammar['num']
                            else:
                                self.nextchar()
                        self.revert()
                        #if self.is_whitespace():
                        #return self.grammar['num']
                    case 5:
                        #print("------------\t\tCASE 5\t\t------------")
                        
                        self.nextchar()
                        if self.ch == 'r':
                            self.nextchar()
                            if self.ch == 'r':
                                self.nextchar()
                                if self.ch == 'a':
                                    self.nextchar()
                                    if self.ch == 'y' and self.is_whitespace():
                                        return self.grammar['array']
                        self.by_pass()
                        return self.lexicalError()
                        break
                    case 6:
                        #print("------------\t\tCASE 6\t\t------------")
                        self.nextchar()
                        while (self.ch==' ') or (self.ch=="\t") or (self.ch=='\n'):
                            self.nextchar()
                        state = 0
                        self.revert()
                        #return(self.lexicalError())
                    case 7:
                        #print("------------\t\tCASE 7\t\t------------")
                        
                        self.nextchar()
                        if self.ch == '.' and self.is_whitespace():
                            return self.grammar['..']
                        self.by_pass()
                        return self.lexicalError()
                        break
                    case 8:
                        #print("------------\t\tCASE 8\t\t------------")
                        
                        if self.is_whitespace():
                            return self.grammar['obracket']
                        self.by_pass()
                        return self.lexicalError()
                        break
                    case 9:
                        #print("------------\t\tCASE 9\t\t------------")
                        
                        if self.is_whitespace():
                            return self.grammar['cbracket']
                        self.by_pass()
                        return self.lexicalError()
                        break
                    case 10:
                        #print("------------\t\tCASE 10\t\t------------")
                        
                        self.nextchar()
                        if self.ch == 'f' and self.is_whitespace():
                            return self.grammar['of']
                        self.by_pass()
                        return self.lexicalError()
                        break
                    case 11:
                        return self.grammar["$"]
    
def typee():
    if look_ahead in ['byte', 'integer', 'num']:
        #print(f"look ahead:'{look_ahead}'")
        simple()
        
    elif look_ahead in ['^id']:
        #print(f"look ahead:'{look_ahead}'")
        match(scanner, '^id')
    
    elif look_ahead in ['array']:
        #print(f"look ahead:'{look_ahead}'")
        match(scanner, 'array')
        match(scanner, 'obracket')
        simple()
        match(scanner, 'cbracket')
        match(scanner, 'of')
        typee()
        
    else:
        print(f"parse failed!")
        exit()

        
def simple():
    if look_ahead in ['byte']:
        #print(f"look ahead:'{look_ahead}'")
        match(scanner, 'byte')
    elif look_ahead in ['integer']:
        #print(f"look ahead:'{look_ahead}'")
        match(scanner, 'integer')
    elif look_ahead in ['num']:
        #print(f"look ahead:'{look_ahead}'")
        match(scanner, 'num')
        match(scanner, 'dotdot')
        match(scanner, 'num')
    else:
        print(f"parse failed!")
        exit()
    
def match(scanner, t):
        global look_ahead
        #print(f"match({look_ahead}, {t})")
        if str(t) == str(look_ahead):
            look_ahead = scanner.get_token()
            if look_ahead == "EOF":
                print("parse succesful!")
                exit()
        else:
            print(f"parse failed!")
            exit()

#-----------------MAIN-----------------        
global look_ahead
scanner = Scanner()
# hard coded strings for debugging and testing porpuses.
#scanner.buffer_set(str("array [ 10 .. 20 ] of array [ 10 .. 20  of byte"))
#scanner.buffer_set(str("array [ -20 .. 20 ] of array [ -20 .. 20 ] of integer"))
#scanner.buffer_set(str("[  20 . 30 ]"))
scanner.buffer_set(str(input("Enter input:")))
look_ahead = scanner.get_token()
typee()
simple()