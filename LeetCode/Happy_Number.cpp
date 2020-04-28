class Solution {
public:
    bool isHappy(int n) {
        set <int> s;
        int sum;
        int x;
        while(true)
        {
            sum=0;
            while(n)
            {
                x=n%10;
                n/=10;
                sum+=pow(x,2);
                // cout<<sum<<endl;
            }
            if (sum==1)
                return true;
            else if(s.find(sum)!=s.end())
                return false;
            s.insert(sum);
            n=sum;
        }
        return false;
    }
};
