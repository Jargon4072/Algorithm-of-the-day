/**
 * @Author: Dwivedi Chandan
 * @Date:   2019-09-08T01:00:55+05:30
 * @Email:  chandandwivedi795@gmail.com
 * @Last modified by:   Dwivedi Chandan
 * @Last modified time: 2019-09-08T11:31:00+05:30
 */

#include<bits/stdc++.h>
using namespace std;
bool search(vector<vector<char>>& board,string word,int i,int j,int n,int m,int ** visited,int idx){
  if(board[i][j]!=word[idx])
    return false;
  if(idx==word.length()-1)
    return true;
  visited[i][j]=1;
  //left
  if(j-1>=0 && visited[i][j-1]==0){
      if(search(board,word,i,j-1,n,m,visited,idx+1))
          return true;
  }
  //right
  if(j<m-1 && visited[i][j+1]==0){
      if(search(board,word,i,j+1,n,m,visited,idx+1))
          return true;
  }
  //top
  if(i-1>=0 && visited[i-1][j]==0){
      if(search(board,word,i-1,j,n,m,visited,idx+1))
          return true;
  }
  //down
  if(i<n-1 && visited[i+1][j]==0){
      if(search(board,word,i+1,j,n,m,visited,idx+1))
          return true;
  }
  visited[i][j]=0;
  return false;

}
bool exits(vector<vector<char>>& boards,string words){
  int n=boards.size();
  int m=boards[0].size();
  int ** visited=new int*[n];   //2D array 
  for(int i=0;i<n;i++){
    visited[i]=new int[m]();
  }
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      if(boards[i][j]==words[0]){
        if(search(boards,words,i,j,n,m,visited,0)){
          return true;
        }
      }
    }
  }
  return false;
}
int main(){
  vector<vector<char>> boards;
  string words;
  int n,m;
  cin>>n>>m;
  for(int i=0;i<n;i++){
    vector<char> vec;
    for(int j=0;j<m;j++){
      char ch;
      cin>>ch;
      vec.push_back(ch);
    }
    boards.push_back(vec);
  }
  cin>>words;
  if(exits(boards,words)){
    cout<<"Word Found in Grid!"<<endl;
  }
  else
    cout<<"Word not found in Grid!"<<endl;
    return 0;
}

