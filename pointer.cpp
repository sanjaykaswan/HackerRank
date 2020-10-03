#include <iostream>
#include <stdio.h>

void update(int *pa,int *pb) {
       
    if (*pa - *pb >=0) {
        *pb = *pa - *pb;
        *pa = *pa + *pa - *pb;
    }
    else {
        *pb = *pb - *pa;
        *pa = *pa + *pa + *pb;
    }
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}