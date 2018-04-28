import os
word = input("Make up a word and enter it here: ")
response = str(os.system('''th sample.lua cv/lm_lstm_epoch9.31_1.3900.t7 -primetext "%s:" -temperature 0.5'''%(word)))
print(response[:response.find("\n")])