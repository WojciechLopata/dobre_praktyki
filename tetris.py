from ast import Return
import random
class tetris():
    def __init__(self):
        self.size=10
        self.board=[["." for i in range(self.size)] for j in range(self.size)]
        f = open("pieces.txt", "r")
        self.pieces=(f.read())
        
        helper=""
        for line in self.pieces:
            line=line.rstrip("\n")
            line=line.replace(" ","")
            helper+=line
        self.pieces=helper
        self.pieces=self.pieces.split("=")
        self.pieces=list(self.pieces)
        for i  in range(len(self.pieces)-1):
            self.piece=self.pieces[i] 
            self.piece=self.piece.replace("[","")
            self.piece=self.piece.split("]")
           
            self.piece.pop()
            for element in self.piece:
                pre_change_element=element
                element=element.replace("\'","")
                
                help=element.split(',')
                
                for row in help:
                    if row=="":
                        del help[help.index(row)]
                

                self.piece[self.piece.index(pre_change_element)]=help
               
            
                
            self.pieces[i]=self.piece
        del self.pieces[0]
        
      
        
            

        self.piece=self.pieces[random.randint(0,len(self.pieces)-1)][0]

        self.next_piece=self.pieces[random.randint(0,len(self.pieces)-1)][0]
        
        
        
        #print(self.pieces)
       
        print(self.piece)
        
        #print(self.piece[0])
        self.col=0
        self.row=0
        self.dynamic_board=self.board            
        self.lines_left=10
        self.result="W trakcie"
        self.height=0
        
    def line_check(self):
            for line in self.board:
                for sign in line:
                    if(sign!="0"):return False
                        
            empty_line=["." for i in range(self.size)]
            self.board[self.board.index(line)]=empty_line
            self.new_piece()
    def render(self):
            for x in self.board:
                print("|",end="",sep="")
                for i in x:
                    print(i,end="",sep="")
                
                print("|")
            print("-------------------------")

            
    def rotate(self,direction):
            self.piece=self.pieces[self.pieces.index(self.piece)+direction]
    def place(self,direction):
        x=0
        dynamic_board=self.board
        for row in self.piece:
            #print(row)
            for i in range(len(row)-1):
                if(self.row+x-1)>=10:
                    break
              
                
                dynamic_board[x-1+self.row][i+self.col]=row[i]
               
            x+=1
        self.board=dynamic_board
        
        self.render()
        self.line_check()
        
    def move(self,direction):
        if(self.col!=10 or self.col!=0):self.col+=direction
        self.row+=1
        if not self.floor():
            self.place(direction)
        else:
            self.render
        
    def floor(self):
        self.piece_height()
        print(self.height)
        if(self.row+self.height==10):
            self.new_piece()
            return True
        
        
            
            
        for row in self.board:
            for sign in row:
                i=row.index(sign)
                #print(i)
                i=int(i)
                if(sign=="0" and self.board[i+1]=="0"):
                    self.new_piece()

                    return True
    def new_piece(self):
        self.piece=self.next_piece
        self.next_piece=self.pieces[random.randint(0,len(self.pieces)-1)][0]
        self.col=0
        self.row=0
        print(self.piece)
    def piece_height(self):
        for i in range(len(self.piece)-1):
            print(self.piece[len(self.piece)-i-1])
            if(self.piece[len(self.piece)-i-1]=="....."):
                self.height=5-i

            
            
a=tetris()
a.move(0)
a.move(0)
a.move(1)
a.move(1)
a.move(1)
a.move(0)
a.move(0)
a.move(0)
a.move(0)
a.move(0)
a.move(0)





            
