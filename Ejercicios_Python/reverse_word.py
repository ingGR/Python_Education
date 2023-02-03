def spin_words(sentence):
    # Your code goes here
    list_sentence=sentence.split()
    list_exit=[]
    for i in list_sentence:
        if len(i)>=5:
            list_exit.append("".join(reversed(i)))
        else:
            list_exit.append(i)            
    
    return " ".join(list_exit)

print(spin_words("this sentense is a test with experiences"))