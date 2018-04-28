import os
word = input("Make up a word and enter it here: ")
response = str(os.system('''th sample.lua cv/lm_lstm_epoch21.60_1.3933.t7 -primetext "%s:" -temperature 0.5'''%(word)))
print(response[:response.find("\n")])