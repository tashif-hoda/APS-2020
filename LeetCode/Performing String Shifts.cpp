class Solution {
public:
    string stringShift(string s, vector<vector<int>>& shift) {
        
        int total_shift=0;
        for(int i=0; i<shift.size(); i++)
        {
            if (shift[i][0]==0)
                total_shift-=shift[i][1];
            else
                total_shift+=shift[i][1];
        }
        string out="";
        if(total_shift<0)
        {
            int n = (-total_shift)%s.size();
            out += s.substr(n, s.size()-n);
            out += s.substr(0, n);
        }
        else if(total_shift>0)
        {
            int n = total_shift%s.size();
            out += s.substr(s.size()-n, s.size());
            out += s.substr(0, s.size()-n);
        }
        else
            out = s;
        
        return out;
    }
};
