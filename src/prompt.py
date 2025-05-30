prompt_template = """
You are an expert at creating questions based on deep learning, generative ai, nlp, ml materials and documentation.
Your goal is to prepare a coder or programmer or interviewer for their exam and coding tests.
You do this by asking questions about the text below:
--------------
{text}
--------------

Create questions that will prepare the coder or programmer or interviewer for their tests.
Make sure not to lose any important information.

QUESTIONS:
"""


refine_template = ("""
You are an expert at creating practice questions based on on deep learning, generative ai, nlp, ml materials and documentation.
Your goal is to help prepare a coder or programmer or interviewer for their exam, interviews and coding tests.
We have received some practice questions to a certain extent: {existing_answer}.
We have the option to refine the existing questions or add new ones.
(only if necessary) with some more context below.
------------------
{text}
------------------

Given the new context, refine the original questions in English.
If the context is not helpful, please provide the original quesitons.

QUESTIONS:
""")