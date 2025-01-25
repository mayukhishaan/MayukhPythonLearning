sentence = '/*Jon is @developer & musician!!'
print(sentence)
new_sentence = ((sentence.replace('!','#').replace('/','#')).replace('*','#').replace('@','#'))
print(new_sentence)
