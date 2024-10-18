import os
import tiktoken
import textwrap
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback
import pandas as pd

# Function to load context data (your context.txt, and other data)
def load_context():
    with open("report_data/context.txt", "r") as f:
        context = f.read()
    return context

# Wrap text to a specified width
def wrap_text(text: str, width: int = 120) -> str:
    return "\n".join(textwrap.wrap(text, width=width))

# Count tokens using tiktoken for tracking
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    return len(encoding.encode(string))

# Extract filename without extensions from a path string
def extract_filename(path: str) -> str:
    base_name = os.path.basename(path)
    return os.path.splitext(base_name)[0]

# Prepare context and prompt templates for OpenAI model
def prepare_prompt_templates(context):
    # System message: Provide system instructions to the AI
    context_template = (
        "You are a master data analyst specializing in generating detailed reports "
        "based on comparative insights between basic, deep, and Google Trends analysis."
    )
    system_message_prompt = SystemMessagePromptTemplate.from_template(context_template)
    
    # Human message: Describe the task
    human_template = (
        "Using the provided context about the basic analysis, deeper analysis, and Google Trends data, "
        "generate a detailed report covering all key insights, trends, and comparisons. "
        "Include sections comparing basic vs deeper, basic vs Google Trends, and deeper vs Google Trends. "
        "Here is the context:\n\n{context}\n\n"
    )
    human_message_prompt = HumanMessagePromptTemplate(
        prompt=PromptTemplate(template=human_template, input_variables=["context"])
    )
    
    # Combine into a chat prompt template
    chat_prompt_template = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )
    
    return chat_prompt_template

# Generate report with LangChain LLMChain
def generate_report(context):
    # Set up the chat LLM (OpenAI GPT model)
    chat_llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    # Prepare the prompt template
    chat_prompt_template = prepare_prompt_templates(context)

    # Set up the chain
    report_chain = LLMChain(llm=chat_llm, prompt=chat_prompt_template)

    # Monitor tokens and costs
    with get_openai_callback() as cb:
        output = report_chain.run({"context": context})
        print(f"Total Tokens: {cb.total_tokens}")
        print(f"Prompt Tokens: {cb.prompt_tokens}")
        print(f"Completion Tokens: {cb.completion_tokens}")
        print(f"Total Cost (USD): ${cb.total_cost:.4f}")

    return output

# Main function
def main():
    # Load analysis context
    context = load_context()

    # Generate report
    print("Generating report...")
    report = generate_report(context)

    # Save the generated report to a file
    report_file_path = 'report_data/final_report.txt'
    with open(report_file_path, 'w') as report_file:
        report_file.write(report)

    print(f"Report generated and saved to {report_file_path}")

# Execute the main function
if __name__ == "__main__":
    main()
