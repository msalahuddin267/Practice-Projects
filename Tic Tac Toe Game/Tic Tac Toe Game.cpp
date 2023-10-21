#include<bits/stdc++.h>
using namespace std;

int is_win(int ara[][4], int n)
{
    for(int i = 1; i <= n; i++)
    {
        if(ara[i][1] == ara[i][2] && ara[i][2] == ara[i][3] && ara[i][1] != -1)
            return ara[i][1];
    }

    for(int j = 1; j <= n; j++)
    {
        if(ara[1][j] == ara[2][j] && ara[2][j] == ara[3][j] && ara[1][j] != -1)
            return ara[1][j];
    }

    if(ara[1][1] == ara[2][2] && ara[2][2] == ara[3][3] && ara[1][1] != -1)
        return ara[1][1];

    if(ara[1][3] == ara[2][2] && ara[2][2] == ara[3][1] && ara[1][3] != -1)
        return ara[1][3];

    return -1;
}

void printGrid(int ara[][4], int n)
{
    cout << "\n";

    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= n; j++)
        {
            if(j == 1)
                cout << "\t";

            if(ara[i][j] == -1)
                cout << " ";

            if(ara[i][j] == 1)
                cout << "X";

            if(ara[i][j] == 2)
                cout << "O";

            if(j < n)
                cout << "\t|\t";
        }

        cout << "\n";

        if(i < n)
            cout << "___________________________________________________";

        cout << "\n\n";
    }
}

int main()
{
    int row, col, n = 3, cnt = 0;
    int grid[4][4];

    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= n; j++)
        {
            grid[i][j] = -1;
        }
    }

    bool player1 = true;
    bool player2 = false;

    while(1)
    {
        printGrid(grid, n);

        if(player1 == true)
        {
            cnt++;
flag1:
            cout << "Player 1 Turn (X), Enter the row and column : ";
            cin >> row >> col;

            if(grid[row][col] != -1)
            {
                cout << "Invalid Input, Try again.\n";
                goto flag1;
            }

            grid[row][col] = 1;
            player1 = false;
            player2 = true;
        }

        else
        {
            cnt++;
flag2:
            cout << "Player 2 Turn (O), Enter the row and column : ";
            cin >> row >> col;

            if(grid[row][col] != -1)
            {
                cout << ("Invalid Input, Try again.\n");
                goto flag2;
            }

            grid[row][col] = 2;
            player1 = true;
            player2 = false;
        }

        if(is_win(grid, n) == 1)
        {
            cout << "\nPlayer 1 Win the Game !!!\n\n";
            printGrid(grid, n);
            break;
        }

        else if(is_win(grid, n) == 2)
        {
            cout << "\nPlayer 2 Win the Game !!!\n\n";
            printGrid(grid, n);
            break;
        }

        if(cnt == 9)
        {
            printGrid(grid, n);
            cout << "\nGame is Draw.\n\n";
            break;
        }
    }

    return 0;
}
