import os
from langchain.llms import OpenAI
# from langchain.document_loaders import S3FileLoader
# import unstructured
from langchain.document_loaders import UnstructuredPDFLoader

os.environ["OPENAI_API_KEY"] = "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"

# #Load pdf file from AWS S3 bucket and extract plain text
# loader = S3FileLoader("Your Bucket", "filename.pdf")
# pdf_content = loader.load()
# plain_text = unstructured.extract_text(pdf_content)

llm = OpenAI(temperature=0.9)

loader = UnstructuredPDFLoader("questions.pdf", mode="elements")
data = loader.load()

queries = data[0].page_content.split('?')

for query in queries:
    if query != '':
        print(llm.predict(query))