from flask import Flask, request, render_template, jsonify, Response
import re

app = Flask(__name__)

def func_1():
	combine = "New Year is Friday in 2021. "
	return combine

def func_2():
	combine_2 = "New year is Wednesday in 2020. "
	return combine_2

def func_3():
	combine_3 = "Our team have five members. "
	return combine_3


def func_4():
	F=[0,1]
	i = 1
	while F[i] < 100000:
		F.append(F[i]+F[i-1])
		i = i+1
	del F[-1]
	F = str(F)
	return(F)


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
	if text1 == '2021':
		combine = func_1()
		result = {"output": combine,
				  "Total words": count_w_numb(),
				  "Length": count_a_numb()
				  }
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

	elif text1 == '2020':
		combine_2 = func_2()
		result = {"output": combine_2,
				  "Total words": count_w_numb(),
				  "Length": count_a_numb()
				  }
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

	elif text1 == 'Members':
		combine_3 = func_3()
		result = {"output": combine_3,
				  "Total words": count_w_numb(),
				  "Length": count_a_numb()
				  }
		result = {str(key): value for key, value in result.items()}
		return jsonify(result=result)

	elif text1 == 'Fibonacci':
		combine_4 = func_4()
		result = {"output": combine_4,
				  "Total words": count_w_numb(),
				  "Length": count_a_numb()
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
		text = func_1() + '\n '+func_2() + '\n ' + func_3() + '\n '+ func_4()+ '\n ' + func_5()+ '\n '+ func_6()+ '\n ' +func_7()+ '\n ' + func_8()
		result = {"output1": func_1(),
				  "output2": func_2(),
				  "output3": func_3(),
				  "output4": func_4(),
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
	app.run(debug=True)
