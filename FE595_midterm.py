from flask import Flask, request, render_template, jsonify, Response
import re
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)

def remove_stop_words():

	input_text = request.form['text1']

	stop_words = set(stopwords.words('english'))  
  
	word_tokens = word_tokenize(input_text)  
  
	filtered_sentence = [w for w in word_tokens if not w in stop_words]

	remove_punctuation = []

	for i in filtered_sentence:

		if i not in string.punctuation:

			remove_punctuation.append(i)
		else:

			continue
	result = " ".join(remove_punctuation)
  	
	return result

def uppercase_all_words():

	input_text = request.form['text1']

	return 	input_text.upper()

def word_appearance_count():

	input_text = request.form['text1']
	    
	counts = dict()
	
	words = input_text.split()

	for word in words:
		if word in counts:
			counts[word] += 1
		else:
			counts[word] = 1

	return str(counts)


def POS_tag():

	input_text = request.form['text1']

	pre_processing = word_tokenize(input_text)

	tagged = nltk.pos_tag(pre_processing)

	return str(tagged)
		


def func_5():
	combine_5 = "New year is Saturday in 2022."
	return combine_5

def func_6():
	combine_6 = "New year is Sunday in 2023."
	return combine_6

def func_7():
        combine_7 = "The Spring Festival in 2029 is the day before Valentine's Day."
        return combine_7

def func_8():
        combine_8 = "Study hard and make progress everyday!"
        return combine_8

def func_9():
	combine_9 = "Stevens Institue of Technology is located near New York."
	return combine_9

def func_10():
	combine_10 = "Staying up late is bad for your health but you need to complete your homework"
	return combine_10

def count_w_numb():
    # calculate the total words you input
    str = request.form['text1']
    #split all the words with space and punctuation mark
    pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
    str1 = re.split(pattern, str)
    lenth = len(str1)
    strr = ["The number of words you have spoken is ",lenth]
    return(strr)

def count_a_numb():
	# calculate the length of the inputs
	str = request.form['text1']
	lenth = len(str)
	strr = ["The lenth of the inputs is ", lenth]
	return(strr)


@app.route('/')
def home():
	return render_template('request.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
	text1 = request.form['text1']
	if text1[0] == '1':
		combine = remove_stop_words()
		result = {"output": combine,
				  # "Total words": count_w_numb(),
				  # "Length": count_a_numb()
				  }
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

	elif text1[0] == '2':
		combine_2 = uppercase_all_words()
		result = {"output": combine_2,
				  # "Total words": count_w_numb(),
				  # "Length": count_a_numb()
				  }
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

	elif text1[0] == '3':
		combine_3 = word_appearance_count()
		result = {"output": combine_3,
				  # "Total words": count_w_numb(),
				  # "Length": count_a_numb()
				  }
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

	elif text1[0] == '4':
		combine_4 = POS_tag()
		result = {"output": combine_4,
				  # "Total words": count_w_numb(),
				  # "Length": count_a_numb()
				  }
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

	elif text1 == '2022':
		combine_5 = func_5()
		result = {"output": combine_5,
				  "Total words": count_w_numb(),
				  "Length": count_a_numb()
				  }
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

	elif text1 == '2023':
		combine_6 = func_6()
		result = {"output": combine_6,
				  "Total words": count_w_numb(),
				  "Length": count_a_numb()
				  }
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

	elif text1 == '2029':
		combine_7 = func_7()
		result = {"output": combine_7,
				  "Total words": count_w_numb(),
				  "Length": count_a_numb()
				  }
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

	elif text1 == 'FE595':
		combine_8 = func_8()
		result = {"output": combine_8,
				  "Total words": count_w_numb(),
				  "Length": count_a_numb()
				  }
		result = {"output": combine_8}
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

	elif text1 == 'Stevens':
		combine_9 = func_9()
		result = {"output": combine_9,
				  "Total words": count_w_numb(),
				  "Length": count_a_numb()
				  }
		result = {"output": combine_9}
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

	elif text1 == 'Health':
		combine_10 = func_10()
		result = {"output": combine_10,
				  "Total words": count_w_numb(),
				  "Length": count_a_numb()
				  }
		result = {"output": combine_10}
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

	elif text1 == 'ALL':
		text = remove_stop_words() + '\n '+uppercase_all_words() + '\n ' + word_appearance_count() + '\n '+ POS_tag()+ '\n ' + func_5()+ '\n '+ func_6()+ '\n ' +func_7()+ '\n ' + func_8()
		result = {"output1": remove_stop_words(),
				  "output2": uppercase_all_words(),
				  "output3": word_appearance_count(),
				  "output4": POS_tag(),
				  "output5": func_5(),
				  "output6": func_6(),
				  "output7": func_7(),
				  "output8": func_8(),
				  "output9": func_9(),
				  "output10": func_10(),
				  "Total words": count_w_numb(),
				  "Length": count_a_numb()
				  }
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)
	else:
		print("400 Bad request")
		return jsonify(result = "Not Found"),400

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8000)
