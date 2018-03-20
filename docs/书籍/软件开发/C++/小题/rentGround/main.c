#include <stdio.h>
#include <stdlib.h>
#define rentCash 10
#define MaxGroundNum 100;  //共有100个场地
typedef struct groundbook{
    int groundID;          //每个场地的编号
    int rentTime;         //该场地的租赁期，单位：小时
    int usedTime;          //已被使用时间
    bool door;              //场地的使用状态；on /off
    int rentCash;           //场地的租金，单位：元
   }groundbook;

typedef struct groundUser{
 string userName;
int userID;
int playTime;             //已消耗时间，单位：小时；应和场地已被使用的时间相同
int rentNum;                 //租赁的场地数目；
int rentFirstGoundID;        //租赁的第一个场地的编号
bool playStation;          //用户使用状态，on / off

}groundUser;


int main()
{
    printf("Hello world!\n");
    return 0;
}
