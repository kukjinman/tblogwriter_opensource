from openai import OpenAI

def requestGptAPI(text):
    print("requestGptAPI is called")
    mygptkey = "add your gpt key"

    client = OpenAI(
        api_key=mygptkey,
    )

    my_msg = [
        {
            "role":"user",
            "content":"techCrunch사이트의 글을 제공할거야. 해당 글에 대한 블로그 리뷰글을 한글로 써줘",
        },
        {
            "role": "user",
            "content": "본문의 글을 단순히 번역하지 말고, 사람의 견해가 들어 간 것 처럼 리뷰 글을 써줘",
        },
        {
            "role": "user",
            "content": "리뷰글 답변의 가장 첫 문장은 리뷰글의 제목을 줘. 그리고 제목은 항상 마침표로 끝맺음 되게 해줘",
        },
    ]

    for t in text:
        # print(t)
        my_msg.append(
            {
                "role":"user",
                "content":t
            }
        )

    print(my_msg)
    # model="gpt-3.5-turbo"
    # model="gpt-4"
    # model="gpt-4o"

    chat_completion = client.chat.completions.create(
        messages=my_msg,
        model="gpt-4o"

    )

    prompt_token = chat_completion.usage.prompt_tokens
    completion_token = chat_completion.usage.completion_tokens


    # print(chat_completion.choices[0].message.content)

    print("prompt token : ", prompt_token)
    print("completion token : ", completion_token)

    # gpt3_input_price = 0.5
    # gpt3_output_price = 1.5

    gpt4o_input_price = 5
    gpt4o_output_price = 15

    input_cost = (prompt_token/1000000) * gpt4o_input_price
    output_cost = (completion_token/1000000) * gpt4o_output_price
    total_cost = input_cost + output_cost

    print(f"GPT 4o 사용비용 : ${total_cost:.6f}")

    return chat_completion.choices[0].message.content
