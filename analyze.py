from openai import OpenAI
client = OpenAI(api_key=(open("key.txt", "r").read()))
input_data = open("result.txt", "r").read()
def get_response(input_data, resume):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You will compare the job listing and the resume provided and provide specific improvements to the resume tailored to the job listing in the format: Improvements for [Full Name]'s Resume <br>, [Improvements]"
        },
        {
            "role": "user", 
            "content": ("Job Listing: " + input_data + "Resume" + resume)
        }
    ],
    max_tokens=500,
    )
    return response.choices[0].message.content