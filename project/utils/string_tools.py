
def word_count_in(str1):
    arr=str1.split() # convert the string into each word of list
    return f'Count of string {len(list(arr))}'

def find_most_common_word(str1):
    dict1={} # create a empty list
    arr=list(str1.split())

    for word in arr:
        if word in dict1:
            dict1[word]+=1
        else:
            dict1[word]=1
    max_value=max(dict1.values())
    min_value=min(dict1.values())
    if(max_value==min_value):
        return "Nothn is common"
    for key,value in dict1.items():
        if value==max_value:
            return f'Most Common word in string {key}'


def reverse_word(text):
    arr=text.split()
    reverse_word=arr.pop()
    while arr:
        reverse_word+=f" {arr.pop()}"
    return f'Reverse of string :{reverse_word}'


def check_pallindrome(text):
    arr=text.split()
    for i in range(len(arr)//2):
        if arr[i]!=arr[len(arr)-1-i]:
            return False
    return True
