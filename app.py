import streamlit as st
from datetime import datetime

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Identity Echo Interface",
    page_icon="📨",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------

st.markdown("""
<style>

/* Main Page */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:4rem;
    padding-right:4rem;
}

/* Cards */

.card{
    background:#ffffff;
    padding:25px;
    border-radius:18px;
    border:1px solid #E5E7EB;
    box-shadow:0 8px 24px rgba(0,0,0,.06);
}

/* Header */

.header {
    background: linear-gradient(
        135deg,
        #0f0f0f 0%,
        #2b2b2b 50%,
        #6b7280 100%
    );

    color: white;

    padding: 30px;

    border-radius: 20px;

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow: 0 10px 30px rgba(0,0,0,0.20);
}

.header h1{
    margin:0;
    font-size:40px;
}

.header p{
    margin-top:8px;
    font-size:17px;
    opacity:.95;
}

/* Status Badge */

.badge{
    background:rgba(255,255,255,.2);
    padding:8px 18px;
    border-radius:30px;
    float:right;
    font-size:14px;
}

/* Sidebar */

section[data-testid="stSidebar"]{
    border-right:1px solid #E5E7EB;
}

/* Metric Cards */

.metric-card{
    background:#F8FAFC;
    border:1px solid #E5E7EB;
    border-radius:14px;
    padding:18px;
    text-align:center;
}

/* Button */

.stButton button{

    width:100%;
    height:50px;
    border-radius:12px;
    font-weight:600;
    font-size:16px;
}

/* Remove top padding */

h1,h2,h3{
    padding-top:0px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# Sidebar
# ==================================================

with st.sidebar:

    st.title("Identity Echo Interface")
    st.caption("Secure Communication Portal")

    st.divider()

    # ----------------------------
    # Assignment
    # ----------------------------

    st.subheader("Assignment")

    st.markdown("""
**Virtual Summer Internship 2026**

**Track:** AI Builder

**Framework:** Streamlit
""")

    st.divider()

    # ----------------------------
    # Features
    # ----------------------------

    st.subheader("Features")

    st.markdown("""
✔ User Input Collection

✔ Input Validation

✔ Message Transmission

✔ Token Estimation

✔ Live Statistics

✔ Context Window Analysis
""")

    st.divider()

    # ----------------------------
    # System Status
    # ----------------------------

    st.subheader("System Status")

    st.success("Ready")

    st.metric(
        label="Context Window",
        value="4096",
        delta="Tokens"
    )

    st.divider()

    # ----------------------------
    # Version
    # ----------------------------

    st.caption("Version 1.0")
# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.markdown("""
<div class="header">

<div class="badge">
Session Active
</div>

<h1>Identity Echo Interface</h1>

<p>
Secure Communication Portal built using Streamlit.
Enter your identity and message to begin transmission.
</p>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Two Column Layout
# ---------------------------------------------------

left, right = st.columns([2,1], gap="large")

# ---------------------------------------------------
# LEFT COLUMN
# ---------------------------------------------------

with left:

    st.markdown("## Transmission Details")

    user_name = st.text_input(
        "Name",
        placeholder="Enter your full name"
    )

    user_message = st.text_area(
        "Message",
        height=170,
        placeholder="Type your message..."
    )

    transmit = st.button(
        "Transmit Message",
        use_container_width=True
    )

# ---------------------------------------------------
# RIGHT COLUMN
# ---------------------------------------------------

with right:

    st.markdown("## Live Statistics")

    characters = len(user_message)

    words = len(user_message.split())

    tokens = round(characters / 4,2)

    context_window = 4096

    usage = (tokens/context_window)*100

    st.metric(
        "Characters",
        characters
    )

    st.metric(
        "Words",
        words
    )

    st.metric(
        "Estimated Tokens",
        tokens
    )

    if usage < 25:
        status = "Safe"

    elif usage < 50:
        status = "Moderate"

    elif usage < 75:
        status = "High"

    else:
        status = "Critical"

    st.metric(
        "Context Status",
        status
    )

    st.write("Context Window Usage")

    st.progress(min(usage/100,1.0))

    st.caption(f"{usage:.2f}% of 4096-token context window")

    # ---------------------------------------------------
# Validation & Processing
# ---------------------------------------------------

if transmit:

    # ---------- Name Validation ----------

    if user_name.strip() == "":

        st.error("Please provide your name.")

    # ---------- Message Validation ----------

    elif user_message.strip() == "":

        st.warning("Please type a message to transmit.")

    # ---------- Success ----------

    else:

        current_time = datetime.now().strftime("%d %B %Y | %I:%M %p")

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("## Transmission Status")

        success_col1, success_col2 = st.columns([3,1])

        with success_col1:

            st.success(
                f"""
Transmission successful!

Greetings, **{user_name}**

We received your message successfully.
"""
            )

        with success_col2:

            st.metric(
                "Estimated Tokens",
                tokens
            )

        # -------------------------------------

        st.info(
            f"System Check: Your message will consume approximately **{tokens} tokens** from our context window."
        )
        
        st.divider()
        st.balloons()
        # -------------------------------------------------
        # Transmission Summary
        # -------------------------------------------------

        st.markdown("## Transmission Summary")

        summary1, summary2, summary3 = st.columns(3)

        with summary1:

            st.metric(
                "Characters",
                characters
            )

        with summary2:

            st.metric(
                "Words",
                words
            )

        with summary3:

            st.metric(
                "Context Usage",
                f"{usage:.2f}%"
            )

        st.divider()

        # -------------------------------------------------
        # Preview + Details
        # -------------------------------------------------

        left_card, right_card = st.columns(2)

        # ----------------------------

        with left_card:

            st.markdown("### Message Preview")

            st.code(
                user_message,
                language=None
            )

        # ----------------------------

        with right_card:

            st.markdown("### Transmission Details")

            st.write(f"**Operator**")

            st.write(user_name)

            st.write("**Submission Time**")

            st.write(current_time)

            st.write("**Context Status**")

            if usage < 25:
                st.success("Safe")

            elif usage < 50:
                st.info("Moderate")

            elif usage < 75:
                st.warning("High")

            else:
                st.error("Critical")

        st.divider()

        # -------------------------------------------------
        # Transmission Log
        # -------------------------------------------------

        with st.expander("View Transmission Log"):

            st.write("Transmission completed successfully.")

            st.write(f"Operator : {user_name}")

            st.write(f"Characters : {characters}")

            st.write(f"Words : {words}")

            st.write(f"Estimated Tokens : {tokens}")

            st.write(f"Context Usage : {usage:.2f}%")

            st.write(f"Submitted : {current_time}")

        st.divider()

        # -------------------------------------------------
        # Footer
        # -------------------------------------------------

        st.caption(
            "Developed for MirAI School of Technology • Virtual Summer Internship 2026"
        )