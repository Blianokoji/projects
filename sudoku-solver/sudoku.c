#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include <ctype.h>
#define size 9
struct sudoku{
    int num;
};

struct sudoku a[size][size]={0};

void display(){
    printf("+-----+-----+-----+-----+-----+-----+-----+-----+-----+\n");
    for(int i=0;i<size;i++){
        printf("|");
        for(int j=0;j<size;j++){
            if(a[i][j].num==0){
                printf("     |");
            }else
                printf("  %d  |",a[i][j].num);

        }
        printf("\n");
        printf("+-----+-----+-----+-----+-----+-----+-----+-----+-----+");
        printf("\n");
    }
}


bool inputcheck(int row,int col,int num){
    //printf("hi");
    a[row][col].num=num;
    int set[9]={0};
    int hori=0;
    int vert=0;
    int thxth=0;
    //horizontal check
    for(int i=0;i<size;i++){
        if(a[row][i].num>0){
            set[a[row][i].num-1]+=1;
        }
    }
    for(int i=0;i<size;i++){
        if(set[i]>1){
           hori=1; 
        }
    }
    //reset
    for(int i=0;i<size;i++){
        set[i]=0;
    }
    //vertical check
    for(int i=0;i<size;i++){
        if(a[i][col].num>0){
            set[a[i][col].num-1]+=1;
        }
    }
    for(int i=0;i<size;i++){
        if(set[i]>1){
           vert=1; 
        }
    }
    //reset
    for(int i=0;i<size;i++){
        set[i]=0;
    }
    //three by three check
    int startRow = row - row % 3;
    int startCol = col - col % 3;
    for(int i=startRow; i<startRow+3; i++){
        for(int j=startCol; j<startCol+3; j++){
            if(a[i][j].num>0){
                set[a[i][j].num-1]+=1;
            }
        }
    }
    for(int i=0;i<size;i++){
        if(set[i]>1){
           thxth=1; 
        }
    }
    //printf("%d",hori);
    if(hori==1 || vert==1 || thxth==1){
        a[row][col].num=0;
        return false;
    }else{
        return true;
    }
}


void input(){
    int row ,col,n;
    int ch=0;
    while(ch!=2){
        display();
        printf("\n1.entry\n2.exit\n");
        scanf("%d",&ch);
        if(ch==1){
            printf("Enter the row and col index(starting index (1 1)): ");
            scanf("%d%d",&row,&col);
            if(row < 1 || row > 9 || col < 1 || col > 9){
                printf("Invalid row or column index. Please enter again.\n");
                continue;
            }
            if(a[row-1][col-1].num!=0){
                printf("The column is already entered.\n");
            }else{
                printf("Enter the value (1-9): ");
                scanf("%d",&n);
                if(n < 1 || n > 9){
                    printf("Invalid input. Please enter a number between 1 and 9.\n");
                    continue;
                }
                if(!inputcheck(row-1,col-1,n)){
                    a[row-1][col-1].num=0;
                    printf("Not a valid entry.\n");
                }
            }
        }else{
            break;
        }
    }
}

bool solveSudoku(int row, int col) {
    
    // Find the first empty cell in the grid
   for (; row < size; row++) {
        for (; col < size; col++) {
            if (a[row][col].num == 0) {
                break;
            }
        }
        if (col < size && a[row][col].num == 0) {
            break;
        }
        col = 0;
    }
    if (row == size ) {
        return true; // If no empty cell is found, puzzle is solved
    }
    // Try different numbers for the empty cell
    for (int num = 1; num <= size; num++) {
        if (inputcheck(row,col,num)==true) {
            a[row][col].num = num; // Assign the number if it is safe
            if (solveSudoku(row,col+1)) {
                return true; // If puzzle is solved, return true
            }else
                a[row][col].num = 0; // If not, backtrack and try a different number
        }
    }
    return false; // If no number can be placed, trigger backtracking
}

int main(){
    //display();
    input();
    display();
    printf("\nSOLVED PUZZLE: \n"); 
    if(solveSudoku(0, 0)){
        display();
    }else{
        printf("No solution exists for the given Sudoku puzzle.\n");
        display();
    }
    return 0;
}