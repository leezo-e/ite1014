#include <stdio.h>
#include <stdlib.h>

typedef struct {

char title[400];
char author [30];
int page;
} Book;

int main() {

  int n;
  scanf("%d", &n);

  Book* p = (Book*)malloc(n*sizeof(Book));

  for (int i = 0; i < 3; i++){

    printf("Title : ");
    scanf("%s",p[i] -> title); 

    printf("Author : ");
    scanf("%s",p[i] -> authour);

    printf("Page : ");
    scanf("%d",&(p[i] -> page);
  }
  


  for (int i =0; i<3; i++) {
    printf("\n");
    printf("BOOK %d\n", i+1);
    printf("\n");
    printf("Title : %s\n",p[i] -> title); 
    printf("Author : %s\n", p[i] -> author);
    printf("Page : %d\n", p[i] ->page);
    printf("\n");
    
  }

  for (int i = 0; i < 3 ; i ++){

    free(p[i]);
    
  }
  
  return 0;

}