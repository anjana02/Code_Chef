def ispalindrome(string):
    string.strip()
    if(string == string[::-1]):
        return "True"
    else:
        return "False"
    
if __name__ == "__main__":
    s = input()
    print(ispalindrome(s))
