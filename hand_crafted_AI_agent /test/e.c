#include <stdio.h>

int main() {
    // 示例1: 遍历整型数组
    int numbers[] = {10, 20, 30, 40, 50};
    int length = sizeof(numbers) / sizeof(numbers[0]); // 计算数组长度

    printf("遍历整型数组:\n");
    for (int i = 0; i < length; i++) {
        printf("元素 %d: %d\n", i, numbers[i]);
    }

    // 示例2: 遍历字符数组（字符串）
    char text[] = "Hello";
    printf("\n遍历字符数组:\n");
    for (int i = 0; text[i] != '\0'; i++) { // 遇到结束符\0停止
        printf("字符 %d: %c\n", i, text[i]);
    }

    return 0;
}