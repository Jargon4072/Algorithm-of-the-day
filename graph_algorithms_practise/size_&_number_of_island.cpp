/*
*
* Given a image represented as 2d array of 0 and 1, find the size of the biggest
* cluster in the image.
* Cluster: one or more adjunct cell with 1 is cluster. Even in a single cell which
* surrounded by all 0 will be clustered.
* Adjacent cell : cell on left, right, top and bottom. Diagonal cells are not
* considered for cluster.
* Size-of-Cluster: number of 1 in the cluster
* input:
* 4
* 5
* 10001
* 00110
* 10000
* 11110
*
* output:
* 5
*
*/


#include <iostream>
#include<bits/stdc++.h>
using namespace std;

#define COL 5
#define ROW 4

bool is_safe(int M[][COL],int row, int col, bool is_visited[][COL]){
	return ((row>=0) && (col>=0) && (row<ROW) && (col<COL) && (M[row][col] && !is_visited[row][col]));
}

void dfs(int arr[][COL], int row, int col, bool is_visited[][COL],int *max1){
	int row_num[8]={  -1, 0, 0, 1, };
	int col_num[8]={  0, -1, 1, 0, };
	is_visited[row][col]=true;
	for(int i=0;i<4;i++){
		if(is_safe(arr,row+row_num[i],col+col_num[i],is_visited)){
			*max1+=1;
			dfs(arr,row+row_num[i],col+col_num[i],is_visited,max1);

		}
	}
}

int count_islandsz(int M[][COL]){
	bool visited[ROW][COL];
	memset(visited, 0, sizeof(visited));
	int res=0;
	// int num_island=0;
	int max1=0;
	for(int i=0;i<ROW;i++){
		for(int j=0;j<COL;j++){
			if(M[i][j] && !visited[i][j]){
				dfs(M,i,j,visited,&max1);
				// num_island++;
				if(max1>res){
					res=max1;
				}
			}
		}
	}
	return res;
	// return num_island;
}
int main() {
	int M[ROW][COL]={{1,0,0,0,1},
	                 {0,0,1,1,0},
	                 {1,0,0,0,0},
	                 {1,1,1,1,0}};
	 int res=count_islandsz(M);
	 cout<<res<<endl;

	return 0;
}
