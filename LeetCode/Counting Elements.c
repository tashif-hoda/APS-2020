int countElements(int* arr, int arrSize){
    char hashset[1005] = {0};
    int i, count=0;
    for(i=0; i<arrSize; i++)
        hashset[arr[i]]=1;
    for(i=0; i<arrSize; i++)
    {
        if(hashset[arr[i]+1])
            count++;
    }
    return count;

}
