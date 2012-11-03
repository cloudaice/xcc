#include<stdio.h>
int main(){
    int score[7] = {76, 82, 90, 86, 79, 62,12};
    int acredit[7] = {2, 2, 1, 2, 2, 3, 3};
    int stu_number;
    float mean, sum;
    int temp;
    int i;
 
    printf("please input your student number:");
    scanf("%d",&stu_number);
 
    sum = 0;
    temp = 0;
    for( i = 0; i < 7; i++)
    {
         sum = sum + score[i] * acredit[i];
         temp = temp + acredit[i];
    }
    mean = sum / temp;
 
    if(mean < 60){
         mean = mean - 60;
         printf("the score of student number %d is %f higher than 60.\n", stu_number, mean);
    }
    else{
         mean = 20;
         printf("the score of student number %d is %f lower than 60.\n",stu_number, mean);
    }
    return 0;
}
