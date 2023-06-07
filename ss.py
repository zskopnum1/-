#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>

// 定义游戏区域的大小
#define WIDTH 20
#define HEIGHT 20

// 定义蛇和食物的标记
#define SNAKE_HEAD 'H'
#define SNAKE_BODY 'X'
#define FOOD '@'

// 定义蛇的移动方向
#define UP 0
#define DOWN 1
#define LEFT 2
#define RIGHT 3

int score = 0; // 分数
int gameover = 0; // 游戏结束标志

int snakeX[100], snakeY[100]; // 蛇身的坐标
int snakeLength = 1; // 蛇的长度
int foodX, foodY; // 食物的坐标
int direction = RIGHT; // 蛇的初始移动方向

// 初始化游戏
void initGame() {
    score = 0;
    gameover = 0;
    snakeLength = 1;
    snakeX[0] = WIDTH / 2;
    snakeY[0] = HEIGHT / 2;
    foodX = rand() % WIDTH;
    foodY = rand() % HEIGHT;
}

// 绘制游戏界面
void drawGame() {
    system("cls"); // 清空屏幕

    int i, j;
    for (i = 0; i < HEIGHT; i++) {
        for (j = 0; j < WIDTH; j++) {
            if (i == snakeY[0] && j == snakeX[0]) { // 绘制蛇头
                printf("%c", SNAKE_HEAD);
            } else if (i == foodY && j == foodX) { // 绘制食物
                printf("%c", FOOD);
            } else {
                int k;
                int isBody = 0;
                for (k = 1; k < snakeLength; k++) {
                    if (i == snakeY[k] && j == snakeX[k]) { // 绘制蛇身
                        printf("%c", SNAKE_BODY);
                        isBody = 1;
                        break;
                    }
                }
                if (!isBody) {
                    printf(" ");
                }
            }
        }
        printf("\n");
    }
    printf("Score: %d\n", score);
    printf("Use arrow keys to control the snake.\n");
    printf("Press 'q' to quit.\n");
}

// 处理键盘输入
void handleInput() {
    if (_kbhit()) {
        char ch = _getch();
        switch (ch) {
            case 'q':
                gameover = 1; // 按下 'q' 退出游戏
                break;
            case 72:
                if (direction != DOWN) {
                    direction = UP; // 按下上箭头键，蛇向上移动
                }
                break;
            case 80:
                if (direction != UP) {
                    direction = DOWN; // 按下下箭头键，蛇向下移动
                }
                break;
            case 75:
                if (direction != RIGHT) {
                    direction = LEFT; // 按下左箭头键，蛇向左移动
                }
                break;
            case 77:
                if (direction != LEFT) {
                    direction = RIGHT; // 按下右箭头键，蛇向右移动
                }
                break;
        }
    }
}

// 更新游戏状态
void updateGame() {
    int i;
    int prevX = snakeX[0];
    int prevY = snakeY[0];
    int prev2X, prev2Y;
    snakeX[0] += (direction == RIGHT) ? 1 : (direction == LEFT) ? -1 : 0;
    snakeY[0] += (direction == DOWN) ? 1 : (direction == UP) ? -1 : 0;

    if (snakeX[0] == foodX && snakeY[0] == foodY) { // 吃到食物
        score += 10;
        snakeLength++;
        foodX = rand() % WIDTH;
        foodY = rand() % HEIGHT;
    }

    for (i = 1; i < snakeLength; i++) { // 更新蛇身的坐标
        prev2X = snakeX[i];
        prev2Y = snakeY[i];
        snakeX[i] = prevX;
        snakeY[i] = prevY;
        prevX = prev2X;
        prevY = prev2Y;
    }

    // 判断游戏结束条件
    if (snakeX[0] < 0 || snakeX[0] >= WIDTH || snakeY[0] < 0 || snakeY[0] >= HEIGHT) {
        gameover = 1; // 蛇碰到边界，游戏结束
    }

    for (i = 1; i < snakeLength; i++) {
        if (snakeX[0] == snakeX[i] && snakeY[0] == snakeY[i]) {
            gameover = 1; // 蛇碰到自己的身体，游戏结束
        }
    }
}

int main() {
    initGame();

    while (!gameover) {
        drawGame();
        handleInput();
        updateGame();
        Sleep(100); // 控制游戏速度
    }

    printf("Game Over! Your score is: %d\n", score);
    return 0;
}
