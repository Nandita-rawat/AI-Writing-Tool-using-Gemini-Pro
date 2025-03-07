
import streamlit as st 
from api_key import google_gemini_api_key 
import google.generativeai as genai
  
genai.configure(api_key  = google_gemini_api_key)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


# setting up the model 
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)





st.set_page_config(layout = "wide")
# title
st.title("WriteWise ✍️🤖 – Smart writing, made simple")

# subheder 
st.subheader("Your AI-powered writing assistant for effortless and intelligent writing")

# sidebar for user input 
with st.sidebar:
    st.title("Input your Blog Details")
    st.subheader("Enter the details of the blog You want to generate")

    # blog title 
    blog_title = st.text_input("Blog Title")

    # blog keywords 
    blog_keywords = st.text_area("Keywords (comma seperated)")

    # number of words 
    num_words = st.slider("Number of Words" , min_value = 250 , max_value = 
                          1000 , step = 250 )
    
    
    prompt = [ f"Generate a comprehensive , engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{blog_keywords}\" Make sure all the keywords are used. The blog should be approximately {num_words} words in length , suitable for online audience . Ensure the content is original , informative , and maintains a consistent tone throughout "
            ]
    
    
    
    # submit button 
    submit_button = st.button("Generate Blog")

if submit_button:
    

    # Generate Blog Content
    response = model.generate_content(prompt)
    st.title("YOUR BLOG POST:")
    st.write(response.text)