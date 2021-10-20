int rangeBitwiseAnd(int left, int right){
    int significanceOfLetter{0};
    while (left < right)
    {
        significanceOfLetter ++;
        left /= 2;
        right /= 2;
    }

    return left << significanceOfLetter;
}