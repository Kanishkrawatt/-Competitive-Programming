#include <stdio.h>
#include <stdlib.h>

struct treeNode{
    int info;
    struct treeNode * leftTreeNode;
    struct treeNode * rightTreeNode;
};
int depth=0;
int * height;
struct treeNode * start,*p,*mover,*pl,*pr;




int main(){
    root = (struct treeNode *) malloc(sizeof(struct treeNode));
    insert(NULL,root,NULL);
    printf("\n\n");
    display(root,1);

}