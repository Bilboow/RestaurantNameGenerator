import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

load_dotenv()

llm = ChatGroq (
    model="openai/gpt-oss-20b",
    api_key = os.getenv("GROQ_API_KEY_2") ,
    temperature=0.9
)

def generate_restaurant_name_and_items(cuisine):
    
#  chain1 restaurant name

    prompt_template_name = PromptTemplate(
        input_variables = ['cuisine'],
        template = """
You are a creative branding expert. 
Suggest a **unique single English restaurant name** for a {cuisine} food restaurant.  

Requirements:
- The name must be **one phrase only** (no explanations).
- It must sound elegant and catchy.  
- Each time, give a **different** name (avoid repeating past names).
"""
    )

    name_chain = LLMChain(llm = llm, prompt = prompt_template_name, output_key = "restaurant_name")

# chain2 items

    prompt_template_item = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = """Suggest some menu items for {restaurant_name} . Return it as a comma separated string """
    )

    food_items_chain = LLMChain(llm = llm, prompt = prompt_template_item, output_key = "menu_items")

    chain = SequentialChain(
        chains = [name_chain,food_items_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name' , 'menu_items'],
        verbose=True
    )

    response = chain({'cuisine':cuisine})

    return response


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))