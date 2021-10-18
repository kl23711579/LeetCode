#include "stdlib.h"
#include "stdio.h"
#include "string.h"

int romanToInt(char *);

int main() {
    char str[256];
    char *delim = "";
    char *pch;

    scanf("%s", str);
    printf("%d\n", romanToInt(str));
    system("pause");
    return 0;
}

int romanToInt(char* str) {
    
    int result = 0;
    for(int i = 0; str[i] != '\0'; i++) {
        switch(str[i]) {
            case 'I':
                if(str[i+1] == 'V') {
                    result += 4;
                    i++;
                } else if(str[i+1] == 'X') {
                    result += 9;
                    i++;
                } else {
                    result++;
                }
                break;
            case 'V':
                result += 5;
                break;
            case 'X':
                if(str[i+1] == 'L') {
                    result += 40;
                    i++;
                } else if( str[i+1] == 'C') {
                    result += 90;
                    i++;
                } else {
                    result += 10;
                }
                break;
            case 'L':
                result += 50;
                break;
            case 'C':
                if(str[i+1] == 'D') {
                    result += 400;
                    i++;
                } else if(str[i+1] == 'M') {
                    result += 900;
                    i++;
                } else {
                    result += 100;
                }
                break;
            case 'D':
                result += 500;
                break;
            case 'M':
                result += 1000;
                break;
            default:
                result = -1;
        }
    }

    return result;
}