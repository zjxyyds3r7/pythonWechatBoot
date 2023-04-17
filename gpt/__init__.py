import openai

# openai.api_key = "openai的apikey"

# 设定参数

model = "text-davinci-003"
temperature = 0.5
max_tokens = 1000


def questionToGpt(q):
    try:
        prompt = q
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].text
    except Exception as e:
        print(e)
        return 'GPT出问题了哦:' + str(e)
