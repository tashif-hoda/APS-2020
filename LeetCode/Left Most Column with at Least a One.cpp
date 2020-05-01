/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * class BinaryMatrix {
 *   public:
 *     int get(int x, int y);
 *     vector<int> dimensions();
 * };
 */

class Solution {
public:
    int leftMostColumnWithOne(BinaryMatrix &binaryMatrix) {
        int n =binaryMatrix.dimensions()[0] - 1;
        int m =binaryMatrix.dimensions()[1] - 1;
        
        int p=0, q=m;
        
        while(p<=n and q>=0)
        {
            if(binaryMatrix.get(p,q)==0)
                p++;
            
            else
                q--;
        }
        if(p>n and q==m)
            return -1;
        
        return q+1;
    }
};
