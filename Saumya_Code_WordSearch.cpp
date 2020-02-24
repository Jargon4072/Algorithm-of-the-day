class Solution {
public:
    bool safe(vector<vector<char>>& board, int i, int j, int idx, string word) {
        return (i >= 0 && i < board.size() && j >= 0 && j < board[0].size() && board[i][j] != '.' && word[idx] == board[i][j]);
    }
    
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int idx, vector< vector<int> > &dirs) {
        if(idx == word.size()) return true;
        if(safe(board, i, j, idx, word)) {
            board[i][j] = '.';
            for(auto &x: dirs) {
                if(dfs(board, word, i + x[0], j + x[1], idx + 1, dirs)) return true;
            }
            board[i][j] = word[idx];
        }
        return false;
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        vector< vector<int> > dirs{{1,0}, {-1, 0}, {0, 1}, {0, -1}};
        for(int i = 0; i < board.size(); ++i) {
            for(int j = 0; j < board[0].size(); ++j) {
                if(dfs(board, word, i, j, 0, dirs)) return true;//firstfunction
            }
        }
        return false;
    }
};
                                
                                
                                     
