from transformers import pipeline

# 文本生成
generator = pipeline("text-generation", model="gpt2")
result = generator("Once upon a time, in a land far away,", max_length=50)
print(result[0]["generated_text"])


# 情感分析
classifier = pipeline("sentiment-analysis")
result = classifier("这家餐厅的菜太好吃了，服务也很棒！")
print(result)
