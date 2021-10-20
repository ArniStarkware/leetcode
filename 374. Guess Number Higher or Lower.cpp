/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int left{1}, right{n};
        int mid;
        int guessResult;
        while (left < right)
        {
            mid = (left+right)/2;
            guessResult = guess(mid);
            if (guessResult == 0){
                return mid;
            }
            else if (guessResult == -1){
                right = mid - 1;
            }
            else{
                left = mid +1;
            }
        }
        return left;
    }
};