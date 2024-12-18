import cohere

# Initialize Cohere client with your API key
cohere_api_key = '7DNoxjgNM7h9ffV8WGcQYPnsggQUUhq2UYywfk3Z'
co = cohere.Client(cohere_api_key)

# Make an API call to generate text
response = co.generate(
    model='command-r-plus',  # You can choose a different model size
    prompt='''
    Only give the answer in a single word, negative or positive!!
    Is it a negative review or postive?
    This movie made it into one of my top 10 most awful movies. Horrible. <br /><br />There wasn't a continuous minute where there wasn't a fight with one monster or another. There was no chance for any character development, they were too busy running from one sword fight to another. I had no emotional attachment (except to the big bad machine that wanted to destroy them) <br /><br />Scenes were blatantly stolen from other movies, LOTR, Star Wars and Matrix. <br /><br />Examples<br /><br />>The ghost scene at the end was stolen from the final scene of the old Star Wars with Yoda, Obee One and Vader. <br /><br />>The spider machine in the beginning was exactly like Frodo being attacked by the spider in Return of the Kings. (Elijah Wood is the victim in both films) and wait......it hypnotizes (stings) its victim and wraps them up.....uh hello????<br /><br />>And the whole machine vs. humans theme WAS the Matrix..or Terminator.....<br /><br />There are more examples but why waste the time? And will someone tell me what was with the Nazi's?!?! Nazi's???? <br /><br />There was a juvenile story line rushed to a juvenile conclusion. The movie could not decide if it was a children's movie or an adult movie and wasn't much of either. <br /><br />Just awful. A real disappointment to say the least. Save your money.

    ''',
    max_tokens=1,
    temperature=0.7
)

# Output the generated text
print(response.generations[0].text)
