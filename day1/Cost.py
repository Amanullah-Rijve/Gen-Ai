'''
ধরো তুমি একটি AI চ্যাট অ্যাপে API ব্যবহারের খরচ হিসাব
করতে চাও। প্রতিদিন কতগুলো token ব্যবহার হয়েছে, তা থেকে 
মোট খরচ বের করতে হবে।
'''

modelName = 'demo-cost-model'
inputTokens = 12000
outputToken = 4000
price_per_million_input = 3.0
price_per_million_output = 15.0

inputCost = (inputTokens / 1000000)* price_per_million_input
outputCost = (outputToken / 1000000)* price_per_million_output
totalCost = inputCost+ outputCost

print(f"Model: {modelName}")
print(f"input cost: {inputCost:.4f}")
print(f"output cost: {outputCost:.4f}")
print(f" Total cost: {totalCost:.4f}")

isExpensive = totalCost > 0.10
print(f"is Expensive: {isExpensive}")