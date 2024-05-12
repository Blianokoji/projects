#include<iostream>
#include<cstdlib>
#include<conio.h>
#include<windows.h>
#include<ctime>
#include<unistd.h> 

using namespace std;

bool gameOver;
const int height=20;
const int width=30;

int x,y,fruitx,fruity,score;

int tailx[100],taily[100],ntail;

enum eDirection{STOP=0,UP,DOWN,LEFT,RIGHT};
eDirection dir;

void setup(){
    gameOver=false;
    x=height/2;
    y=width/2;
    fruitx = rand()%width;
    fruity = rand()%height;
}

void Draw(){
    system("CLS"); // Clear the screen

    for(int i=0;i<width+2;i++){
        cout<<"#";
    }
    cout<<endl;

    for(int i=0;i<height;i++){
        for(int j=0;j<width;j++){
            if(j==0){
                cout<<"#";
            }
            if(i==x && j==y){
                cout<<"O";
            }
            else if(i==fruity&&j==fruitx){
                cout<<"F";
            }
            else{
                bool print=false;
                for(int k=0;k<ntail;k++){
                    if(i==tailx[k] && j==taily[k]){
                        cout<<"o";
                        print=true;
                    }
                }
                if(!print){
                    cout<<" ";
                }
            }
            if(j==width-1){
                cout<<"#";
            }
        }
        cout<<endl;
    }

    for(int i=0;i<width+2;i++){
        cout<<"#";
    }
    cout<<endl;
    cout<<"SCORE: "<<score<<endl;
}

void input(){
    // Check for keyboard input
    // Assuming 'w' for UP, 'a' for LEFT, 's' for DOWN, 'd' for RIGHT
    
    if(_kbhit()){
        switch(_getch()){
            case 'w':
                dir=UP;
                break;
            case 'a':
                dir=LEFT;
                break;
            case 's':
                dir=DOWN;
                break;
            case 'd':
                dir=RIGHT;
                break;
            default:
                break;
        }
    }
}

void logic(){
    int prevx=tailx[0];
    int prevy=taily[0];
    int prev2x,prev2y;
    tailx[0] = x;
    taily[0] = y;

    for(int i=1;i<ntail;i++){
         prev2x=tailx[i];
         prev2y=taily[i];
         tailx[i]=prevx;
         taily[i]=prevy;
         prevx=prev2x;
         prevy=prev2y;
    }

    switch(dir){
        case UP:
            x--;
            break;
        case DOWN:
            x++;
            break;
        case LEFT:
            y--;
            break;
        case RIGHT:
            y++;
            break;
        default:
            break;
    }

    // Boundary checking
    if(x<0 || x>=height || y<0 || y>=width){
        gameOver=true;
    }

    // Check for collision with tail
    for(int i=0;i<ntail;i++){
        if(y==taily[i] && x==tailx[i]){
            gameOver=true;
        }
    }

    // Check for collision with fruit
    if(y==fruitx&&x==fruity){
        score+=10;
        fruitx = rand()%width;
        fruity = rand()%height;
        // Ensure fruit doesn't spawn on the snake's tail
        for(int i=0;i<ntail;i++){
            if(fruitx==taily[i] && fruity==tailx[i]){
                fruitx = rand()%width;
                fruity = rand()%height;
            }
        }
        ntail++;
    }
}

int main(){
    setup();

    while(!gameOver){
        Draw();
        input();
        logic();
        Sleep(50); // Uncomment this line for Windows
        //usleep(50000); 
    }
    cout << "Game Over!" << endl;
    cout << "Final Score: " << score << endl;
    return 0;
}
