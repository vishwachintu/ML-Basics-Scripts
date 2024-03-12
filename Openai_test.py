import openai

# Replace with your own OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Prompt to send to the API
prompt = "Write a poem about a cat."

# Optional arguments for completion
temperature = 0.7  # How creative the response should be (0-2)
max_tokens = 100  # Maximum number of words to generate

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens
)

# Print the generated text
print(response.choices[0].text.strip())
