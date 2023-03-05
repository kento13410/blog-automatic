import openai


def getOpenAIResponse(prompt):
    openai.api_key = ''  # 発行したAPIキーを入力

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,  # 入力する文章
        max_tokens=1000,  # 文章の最大単語数
        echo=False  # promptの文章を出力
    )

    return response['choices'][0]['text'].replace('¥n', '')


class WordPressFormat:
    def __init__(self, item, request, response, htmlformat):
        self.item = item
        self.request = request
        self.response = response
        self.htmlformat = htmlformat

    def getFormatContent(self):
        if self.item != 'タイトル':
            return '<' + self.htmlformat + '>' + self.response + '</' + self.htmlformat + '>'
        else:
            return self.response


title = ''
blog_element_list = [
    WordPressFormat('タイトル', 'ChatGPTとプログラミングを用いた副業のタイトルを考えてください', '', ''),
    WordPressFormat('リード文', 'のリード文を考えてください', '', 'p'),
    WordPressFormat('本文', 'の本文をこれまでの流れを踏まえ、考えてください', '', 'p'),
    WordPressFormat('まとめ', 'のまとめをこれまでの流れを踏まえ、考えてください', '', 'p'),
]
for blog_element in blog_element_list:
    blog_element.response = getOpenAIResponse(title + blog_element.request)
    if title == '':
        title = blog_element.response.replace('/n', '')
    print(blog_element.getFormatContent())
