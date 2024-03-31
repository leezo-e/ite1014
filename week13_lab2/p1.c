#include <stdio.h>

struct Book {

char title[400];
char author [30];
int page;
};

int main() {

  struct Book book[3];

  for (int i = 0; i < 3; i++){

    printf("Title : ");
    scanf("%s", book[i].title);

    printf("Author : ");
    scanf("%s", book[i].author);

    printf("Page : ");
    scanf("%d", &book[i].page);
  }
  


  for (int i =0; i<3; i++) {
    printf("\n");
    printf("BOOK %d\n", i+1);
    printf("\n");
    printf("Title : %s\n", book[i].title);
    printf("Author : %s\n", book[i].author);
    printf("Page : %d\n", book[i].page);
    printf("\n");
    
  }
  
  return 0;

}