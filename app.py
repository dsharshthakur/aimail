import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain




st.markdown("<h1 style = 'text-align:center; font-size:58px;'><span style = 'color:orange'>AI</span>mail</h1>" , unsafe_allow_html = True)
st.markdown("<p style = ' text-align:center;font-size:15px ; margin-top:-25px;'> It's <b>AImail</b> not <b>Email !!</b> </p>" , unsafe_allow_html = True)
st.markdown("<br>" , unsafe_allow_html = True)



st.markdown('''
<h4 style = 'text-decoration:underline;'>Welcome to the <span style = 'color:orange'>AI</span>mail</h4>

<p>Are you looking for a personalized touch to your mails? Look no further! Our advanced text generation model is here to assist you in crafting unique and thoughtful letters. Whether you're expressing gratitude, sharing exciting news,
 or simply penning a heartfelt note, our model is ready to help.</p>

<h6>How it Works:</h6>
<ol>
<li>Enter a few key details or prompts to guide the content generation process.</li>
<li>Watch as our model weaves words together to create a one-of-a-kind mail just for you.</li>
<li>Tweak and customize the generated text until it perfectly captures your sentiments.</li>
</ol>
<h6>Why Choose Us:</h6>

State-of-the-art language model for natural and coherent text generation.
Easy-to-use interface for a seamless experience.
Personalize each letter according to your preferences.
Start creating beautiful, expressive letters today! Simply input your details, and let our model do the rest.

''' , unsafe_allow_html = True)

def generatemail(occupation, mail_subject, total_words):
    key = st.secrets["PROJECT_KEY"]

    model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=str(key))

    system_template = "write an email for a {mtype} on the topic {topic} in {words} words."

    prompt = PromptTemplate(input_variables=["mtype", "topic", "total_words"], template=system_template)
    chain = LLMChain(llm=model, prompt=prompt)
    ai_response = chain.run(mtype=occupation, topic=mail_subject, words=total_words)
    return ai_response

col1, col2, col3 = st.columns([0.4,0.4,0.2])

with col1:
    occupation = st.selectbox("Who you are :", options = [" ","Student" , "Professional" , "Other"])
    if occupation == "Student":
        mail_subject = [" ","Take Leave","Special Accommodations Request","Event","Facility/Service Issue","Exam Issue" , "Custom"]
    elif occupation == "Professional":
        mail_subject = [" ","Leave Request Email" , "Job Application Email", "Resignation Email" , "Meeting Request Email" ,"Thank You Email" , "Client Proposal Email" , "Feedback Request Email", "Custom" ]
    else:
        mail_subject =" "

if occupation != "Other" :
    with col2:
        selected_subject = st.selectbox(label = "Choose mail type." , options = mail_subject)
    with col3:
        total_words = st.number_input(label="Total Words", value=100 ,  min_value = 50)
    if selected_subject == 'Custom':
        col1,col2,col3 = st.columns([0.40,0.40,0.20])
        with col2:
            selected_subject = st.text_input(label = "Write the subject here." , value = " " )

else :
    with col2:
        selected_subject = st.text_input(label = "Write the subject here." , value = " ")
    with col3:
        total_words = st.number_input(label="Total Words", value=100)



col1,col2,col3 = st.columns([0.40, 0.20 , 0.30])
with col2:
    st.markdown("<br>", unsafe_allow_html = True)
    generate_btn = st.button("Generate", use_container_width = True)
   st.markdown("<br>", unsafe_allow_html = True)

if generate_btn == True:
    if occupation != " " and selected_subject != " " :
        ai_response = generatemail(occupation=occupation , mail_subject = selected_subject, total_words = total_words)

        with st.container(border = True ) as response_container:
            
            st.markdown("<h5>Response:</h5>", unsafe_allow_html=True)
          
            st.info(ai_response)
            st.write("You can generate the response again iff not satisfied.")
            
    else:
        st.warning("Please fill all the information first.")

