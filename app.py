import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Identity Echo Interface",
    page_icon="📨",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>

/* Main Container */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    border-right:1px solid #d1d5db;
}

/* Button */
.stButton > button{

    width:100%;

    height:52px;

    border-radius:12px;

    font-size:17px;

    font-weight:700;

    border:none;

    transition:.25s;

}

.stButton > button:hover{

    transform:translateY(-2px);

}

div[data-testid="stVerticalBlockBorderWrapper"]{

    border-radius:20px !important;
border-top:4px solid #2563EB !important;
    border:1px solid rgba(120,120,120,.15) !important;

    padding:20px !important;

    box-shadow:0 12px 30px rgba(0,0,0,.12);

    background:rgba(255,255,255,.02);

}

/* Mobile */

@media (max-width:768px){

.block-container{
    padding-left:1rem;
    padding-right:1rem;
    padding-top:1rem;
}

div[data-testid="stVerticalBlockBorderWrapper"]{
    padding:16px !important;
}

}
}
</style>
""", unsafe_allow_html=True)



with st.sidebar:

    st.title("Identity Echo Interface")

    st.caption("Secure Communication Portal")

    st.divider()

    st.subheader("Assignment")

    st.write("Virtual Summer Internship 2026")

    st.write("AI Builder Track")

    st.write("Framework: Streamlit")

    st.divider()

    st.subheader("Core Features")

    st.write("• User Input")

    st.write("• Input Validation")

    st.write("• Message Transmission")

    st.write("• Token Estimation")

    st.write("• Message Analysis")

    st.divider()

    st.subheader("System")

    st.success("Ready")

    st.metric(
        "Context Window",
        "4096",
        "Tokens"
    )

    st.divider()

    st.caption("Version 1.0")


left, center, right = st.columns([1,8,1])

with center:

    with st.container(border=True):

        st.title("Identity Echo Interface")

        st.caption("Secure Communication Portal")

        st.write(
            "Enter your identity and message below, then click **Transmit** to securely process your transmission."
        )
    st.markdown("<div style='margin-top:10px'></div>", unsafe_allow_html=True)


left, center, right = st.columns([1,6,1])

with center:

    with st.container(border=True):

        st.subheader("Transmission Details")

        user_name = st.text_input(
            "Name",
            placeholder="Enter your full name"
        )

        user_message = st.text_input(
            "Message",
            placeholder="Type your message"
        )

        st.write("")

        transmit = st.button(
            "Transmit",
            use_container_width=True
        )

if transmit:

    if user_name.strip() == "":

        st.error("Please provide your name.")

    elif user_message.strip() == "":

        st.warning("Please type a message to transmit.")

    else:

     

        character_count = len(user_message)

        word_count = len(user_message.split())

        token_count = round(character_count / 4, 2)

        context_window = 4096

        context_usage = round(
            (token_count / context_window) * 100,
            2
        )

        if context_usage < 25:
            context_status = "Safe"

        elif context_usage < 50:
            context_status = "Moderate"

        elif context_usage < 75:
            context_status = "High"

        else:
            context_status = "Critical"

        transmission_time = datetime.now().strftime(
            "%d %B %Y | %I:%M %p"
        )

     
        st.success(
            f"Transmission successful! Greetings, {user_name}. "
            f"We received your message: {user_message}"
        )

        st.info(
            f"System Check: Your message will consume approximately "
            f"{token_count} tokens from our context window."
        )

        st.divider()

      

        st.subheader("Message Analysis")

        metric1, metric2, metric3, metric4 = st.columns(4)

        with metric1:
            st.metric(
                "Characters",
                character_count
            )

        with metric2:
            st.metric(
                "Words",
                word_count
            )

        with metric3:
            st.metric(
                "Estimated Tokens",
                token_count
            )

        with metric4:
            st.metric(
                "Context Status",
                context_status
            )

        st.write("Context Window Usage")

        st.progress(
            min(context_usage / 100, 1.0)
        )

        st.caption(
            f"{context_usage}% of 4096-token context window used."
        )
        st.divider()
    

        detail_col1, detail_col2 = st.columns(2)

        with detail_col1:

            st.subheader("Transmission Details")

            st.write(f"**Operator:** {user_name}")

            st.write(f"**Submission Time:**")

            st.write(transmission_time)

            st.write(f"**Context Status:** {context_status}")

        with detail_col2:

            st.subheader("Message Preview")

            st.code(
                user_message,
                language=None
            )

        st.divider()


        with st.expander("View Transmission Log"):

            st.write("Transmission completed successfully.")

            st.write("---")

            st.write(f"Operator : {user_name}")

            st.write(f"Message : {user_message}")

            st.write(f"Characters : {character_count}")

            st.write(f"Words : {word_count}")

            st.write(f"Estimated Tokens : {token_count}")

            st.write(f"Context Usage : {context_usage}%")

            st.write(f"Context Status : {context_status}")

            st.write(f"Submitted : {transmission_time}")

        st.divider()


        st.download_button(
            label="Download Message",
            data=user_message,
            file_name="Message.txt",
            mime="text/plain",
            use_container_width=True
        )

        st.divider()

        st.subheader("System Information")

        info1, info2, info3 = st.columns(3)

        with info1:
            st.metric("Framework", "Streamlit")

        with info2:
            st.metric("Language", "Python")

        with info3:
            st.metric("Context Window", "4096")

       


st.divider()

st.caption(
    "Developed for MirAI School of Technology • Virtual Summer Internship 2026 • AI Builder Track"
)