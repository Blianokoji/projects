#global
a = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
i=1
c=0
flag=9

def check(flag,a):#check if all columns are filled 
    for j in range(0,len(a)):
        for k in range(0,3):
            if(a[j][k]!=' '):
                flag-=1
    if(flag==0):
        return 1
    else:
        return 0


def diagonal_check1(a):
	if a[0][0]==a[1][1]==a[2][2] and a[0][0]!=' ' :
		return True

def diagonal_check2(a):
     if a[0][2]==a[1][1]==a[2][0] and a[0][2]!=' ':
          return True

def row_check(a):
    for i in range(3):
        if a[i][0] == a[i][1] == a[i][2] and a[i][0] != ' ':
            return True
    return False

def col_check(a):
    for i in range(3):
        if a[0][i] == a[1][i] == a[2][i] and a[0][i] != ' ':
            return True
    return False

      
def wincheck(a):#final check for the win conditions

    if((row_check(a) or col_check(a) or diagonal_check1(a) or diagonal_check2(a)) is True):
        return True
    else:
        return False

def display(a):

    for i in range(3):
        print(f"  {a[i][0]} |  {a[i][1]} |  {a[i][2]} ")  # cells
        if i !=2:
            print("----+----+----")




def xin(a):#input x
    print("it is X's turn")
    while(True):
            c=input("enter the coordinate of the column ")
            if(a[int(c[0])][int(c[1])]!=' '):
                print("that column is already occupied ")
            else:
                break
        
    a[int(c[0])][int(c[1])]='X'



def oin(a):#input o
    print("it is O's turn")
    while(True):
        c=input("enter the coordinate of the column ")
        if(a[int(c[0])][int(c[1])]!=" "):
            print("that column is already occupied ")
        else:
            break
    a[int(c[0])][int(c[1])]='O'



if __name__=="__main__":
    while(True):
        display(a)
        f=check(flag,a)
        if(f==1):
            print("the game is a draw")
            break
        if(i%2==0):
        
            oin(a)
            if(wincheck(a)==True):
                display(a)
                print("o won the game")
                break
        else:
            xin(a)
            if(wincheck(a)==True):
                display(a)
                print("x won the game")
                break

        i+=1