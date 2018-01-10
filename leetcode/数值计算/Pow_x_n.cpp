#include <cstdint>

class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0)
            return 1;
        double cur;
        double result = 1.0;
        uint32_t m;
        if (n < 0)
        {
            m = -n;
            cur = 1 / x;
        }            
        else
        {
            m = n;
            cur = x;
        }            
        while (m)
        {
            if (m & 1)
                result *= cur;
            cur *= cur;
            m >>= 1;
        }
        return result;
    }
};