import random
import sys
import os
sys.path.append(os.path.abspath(".."))
from module.utils import split_words

TAG = {1:"Coming_out",2:"Divined_inquested",3:"Guard",4:"Vote",5:"Estimate",6:"Agree",7:"Disagree",8:"Opinion",9:"Information",10:"Question",11:"Ans",12:"Request",13:"None"}
BODER = 0.7
def classification(data):,
  result = init_weight * np.random.randn(input_layer_size, hidden_layer_size)
  return result

def cl_basic(data):
  result = []
  i = 0
  classification_result = classification(data)
  sorted_result = sorted(classification_result.items(), key=lambda x:x[1],reverse=True)
  for key in sorted_result:
    if i == 0:
      if  key[1] < 0.5:
        result.append(None)
        break
      if key[0] in [6,7]:
        result.append(None)
        break
      if '？' in data or '?' in data:
        result.append("Question")
        i+=1
        continue
      result.append(TAG[key[0]])
      i+=1
    elif i ==1 and key[1] >= BODER and key[0] not in [6,7]:
      result.append(TAG[key[0]])
      break
  if classification_result[6] >= classification_result[7]:
    result.append("Agree")
  else:
    result.append("Disagree")
  return result

def main():
  text = input('text>')
  parsed_text = split_words(text)
  print(cl_basic(parsed_text))

if __name__ == "__main__":
  while True:
    main()