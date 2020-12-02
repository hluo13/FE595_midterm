# FE595_midterm

The website url: http://3.131.90.103:8000/
This website is supposed to give NLP result for your input text.
Use the key words in optional functions to call the functions.
key words:
"stop words" : remove_stop_words()
To remove all the stopwords.
"uppercase": uppercase_all_words()
To turn all the text into uppercase.
"appearance count": word_appearance_count()
To count the number of times each word appears.
"pos_tag": POS_tag()
To check the part of speech of each word.
"sentence tokenize" : sent_token()
To tokenize sentences in the text by using nltk logic for future analysis.
"stem" : sent_stem()
To tokenize words in the text and to remove affix and get the stems of each words. In this way, we can save storage and avoid the situation of dealing with derivative words from a same original word.
"lemma" : sent_lemma()
To link words with similar meaning to one word. It does morphological analysis of the words.
"translate": translate_input()
To translate the English input into Chinese.
"longest word definition" : long_word_def()
To give the definition of the longest word in the input.
"sentiment analysis" : sentiment_analysis()
To return sentiment analysis scores.
"tree" : gram_tree()
To make a Tree and show the tag of each words.
"all" : call all the above functions.
If the function name inputed is not in the optional list, "400 Bad request" will be returned.
