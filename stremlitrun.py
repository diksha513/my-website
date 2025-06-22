import streamlit as st

# Page config
st.set_page_config(page_title="Diksha Gadataranavar", page_icon="🌐", layout="wide")

# Header
st.title("Hi, I'm Diksha 👋")
st.subheader("Cloud Data Engineer | GenAI Developer | Explorer")

# About Me
st.markdown("""
I'm a passionate GenAI developer and cloud data engineer with experience in:
- Python, LangChain, Azure OpenAI, Vertexai
- Data automation, Data engineering.  
- Exploring cultures & food across India 🇮🇳""")

with st.sidebar:
    st.header("💼 Tech Stack")
    st.markdown("""
    - Python, SQL , Streamlit
    - AL ,ML
    - Cloud - Azure,AWS
    - NLP  tools - nltk,Gensim
    - Azure OpenAI , Google Vertex AI, 
    - LLMOps, JWT, Dashboards,LangChain ,LLMs,Rag
       
    """)            
st.text("Reach me at --  diksh2018@gmail.com")


# Projects
st.header("🚀 Projects")
st.markdown("""
            
### 🤖 Multi-Agent GenAI App:
Built a multi-agent GenAI app using Google ADK, MCP Toolbox, and AlloyDB, featuring Renovation Proposal, Permit
Compliance, and Order Status agents with agent-to-agent communication and real-time user interaction.

### 🔍 GenAI Resume Parser
Developed a resume parser using Python, LangChain, Azure OpenAI, and Streamlit to extract candidate details, skills, and
experience into structured format with interactive UI.
            
### 🧠 Early Stage Alzheimer’s Detection 
Built an end-to-end Early-Stage Alzheimer’s Detection model using Deep Learning approach. Used Transfer learning models
like VGG16 and ResNet50 and scratch CNN model.
            
### 💲 Crypto currency price predictor 
Built a real time Machine Learning project to predict Crypto-Currency Price using Python, Flask machine learning algorithm
and hosted on PythonAnywhere.
Project link: https://github.com/diksha513/CryptocurrencyPredictor          

""")

# Contact
st.header("📬 Contact")
st.write("LinkedIn: [MY LinkedIn](https://www.linkedin.com/in/diksha-gadataranavar/)")
st.write("GitHub: [MY GitHub](https://github.com/diksha513)")


st.markdown("---")
st.markdown("🛠️ *This portfolio is a work in progress. Thank you for visiting!*")