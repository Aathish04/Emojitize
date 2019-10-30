import emojidict

def emojitize(usertext): #make a function emojitize, that accepts the raw usertext in string form.
  #Split user's input into words
  userwords = re.findall(r"[\w']+|[.,!?;]", usertext, re.UNICODE) # I found this online and have no idea how it works. I only know that it works.
  
  # Loop that checks for each word in userwords whether it matches with a dictionary key, and replaces it with the value for that key.
  
  for the_word in range(0, len(userwords)): #for each word in the length of userwords.
    word = userwords[the_word] # the variable "word" is equal to a corresponding value in userwords.
    
    if word in emojidict.emojidict: #if a word is found to match with a dictionary entry in emojidict.
      userwords[the_word] = emojidict.emojidict[word] #replace that word with the corresponding entry in the dictionary.

  sentence = (" ".join(userwords)) # Make a sentence that joins all the words in userwords, separated by spaces.

  emojified_sentence = emoji.emojize(sentence) #Emojitize the joined sentence.
  return emojified_sentence #Return the emojified_sentence