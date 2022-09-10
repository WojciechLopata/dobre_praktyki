class state_check():
    #Klasa służąca sprawdzaniu  czy ostatni ruch nie spełnia  warunku wygranej bądź nie uniemożliwa dalszej rozgrywki
    @staticmethod
    def check_draw(turn,size):
        if(turn==size):
            return True
            
    @staticmethod
    def check(board,win_con):
        
        return (state_check.check_vertical(board,win_con) or state_check.check_horizontal(board,win_con) or state_check.check_diagonal(board,win_con))
    @staticmethod
    def check_horizontal(board,win_con):
        for row in board:
            streak_counter=0
            symbol=row[0]
            for area in row:
                if(area==symbol and symbol!=" "):
                    streak_counter+=1
                    if(streak_counter>=win_con):return True
                else:
                    symbol=area
                    streak_counter=1
            if(streak_counter>=win_con):return True
        return False
    @staticmethod       
    def check_vertical(board,win_con):
         for column in range(0,len(board)):
             streak_counter=0
             symbol=board[0][column]
             for row in range(0,len(board)):
                if(board[row][column]==symbol and symbol!=" "):
                     streak_counter+=1
                     if(streak_counter>=win_con):return True
                else:

                    symbol=board[row][column]
                    streak_counter=1
         return False
                




    @staticmethod     
    def check_diagonal(board,win_con):
        for row in range(0,len(board)-win_con+1):
            for column in range(0,len(board)-win_con+1):
                streak_counter=0
                symbol=board[row][column]
                for i in range(0,win_con):
                    if(board[row+i][column+i]==symbol and symbol!=" "):
                        streak_counter+=1
                        if(streak_counter>=win_con):return True
                    else:
                        symbol=board[row+i][column+i]
                        streak_counter=1
        for row in range(win_con-1,len(board)):
            streak_counter=0
            symbol=board[row][0]
            for column in range(0,len(board)-win_con+1):
                streak_counter=0
                symbol=board[row][column]
                for i in range(0,win_con):
                    if(board[row-i][column+i]==symbol and symbol!=" "):
                        streak_counter+=1
                        if(streak_counter>=win_con):return True
                    else:
                        symbol=board[row-i][column+i]
                        streak_counter=1
    # tu będzie dużo błędów pamiętaj
#i=input("START")
