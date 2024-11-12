def checkpalindrome(word):
    n=len(word)
    out=1
    for i in range(n):
        if(word[i]==word[n-i-1]):
            out=1
        else :
            out=0
            break
    
    if (out==1):
        print("True")
    else :
        print("False")

            


word=input("type a word : ")
checkpalindrome(word)