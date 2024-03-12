from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer

# Define the text for summarization
text = """
This is a sample text for summarization. It contains multiple sentences 
that convey different information. An ideal summary would capture the key points 
of the text concisely. Let's see how well the summarizer performs. 
"""

# Create a parser object
parser = PlaintextParser.from_string(text)

# Create a summarizer object with desired number of sentences
lsa_summarizer = LsaSummarizer(2)  # Summarize into 2 sentences

# Summarize the parsed text
summary = lsa_summarizer(parser.document, sentences=2)

# Print the summarized text
print("Summary:\n")
for sentence in summary:
  print(sentence)
