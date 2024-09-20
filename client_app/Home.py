import streamlit as st
# Local imports
from common.cognito_helper import CognitoHelper
from common.streamlit_utils import hide_deploy_button
from streamlit_option_menu import option_menu

from st_pages import show_pages,Section, Page, hide_pages,add_indentation


#========================================================================================
# [View] Render UI components  
#========================================================================================
# Streamlit page configuration
st.set_page_config(page_title="Generative AI CDK Constructs Samples", page_icon="🤖")
add_indentation() 

show_pages(
    [
        Section("Document Explorer", icon="📁"),
        Page("pages/1_doc_explorer_home.py", "Home", "🏠",in_section=True),
        Page("pages/2_Select_Document.py", "Select Document", "📃",in_section=True),
        Page("pages/3_Q&A.py", "Q&A", "💬",in_section=True),
        Page("pages/4_Summary.py", "Summary", "🏷️",in_section=True),
        Page("pages/5_Visual_Q&A.py", "Visual Q&A", "👁️‍🗨️",in_section=True),
        
    ]
)

#with st.sidebar:
# Check if user is authenticated and display login/logout buttons
auth = CognitoHelper() 
auth.set_session_state()
auth.print_login_logout_buttons()

if auth.is_authenticated():
   
        hide_deploy_button()

        # Guest user UI 
        st.write("# Welcome to Document Explorer!")
        st.markdown('''
        The Sample Generative AI Application demonstrates how to build end-to-end solutions leveraging AWS services and the [Generative AI Constructs library](https://github.com/awslabs/generative-ai-cdk-constructs).

        It includes examples of key components needed in generative AI applications:

        - [Data Ingestion Pipeline](https://github.com/awslabs/generative-ai-cdk-constructs/tree/main/src/patterns/gen-ai/aws-rag-appsync-stepfn-opensearch): Ingests documents, converts them to text, and stores them in a knowledge base for retrieval. This enables long context window approaches.

        - [Document Summarization](https://github.com/awslabs/generative-ai-cdk-constructs/tree/main/src/patterns/gen-ai/aws-summarization-appsync-stepfn): Summarizes PDF documents leveraging Large Language Models like Anthropic Claude V2 via Amazon Bedrock. 

        - [Question Answering](https://github.com/awslabs/generative-ai-cdk-constructs/tree/main/src/patterns/gen-ai/aws-qa-appsync-opensearch): Answers natural language questions by retrieving relevant documents from the knowledge base and leveraging Large Language Models.

        By providing reusable constructs following AWS best practices, this app enables quickly building custom generative AI apps on AWS. The constructs abstract complexity of orchestrating AWS services like Lambda, OpenSearch, Step Functions, Bedrock, etc.

        Here is the architecture diagram of the sample application:
        ''')
        st.image('assets/doc_explorer_diagram.png', width=700)
        st.markdown('<style>div[class="stApp"] > div[class="css-1es6loc e1tzin5j2"]{text-align:center;}</style>', unsafe_allow_html=True)


      
else:
    hide_pages(["Q&A","Select Document","Summary","Visual Q&A"])
    st.write("Please login!")
    st.stop()