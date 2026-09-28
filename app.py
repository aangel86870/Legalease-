import streamlit as st

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")

st.write(
    "Create customizable legal documents such as Employment Contracts, "
    "NDAs and Lease Agreements."
)

document_type = st.selectbox(
    "Document Type",
    [
        "Employment Contract",
        "Non-Disclosure Agreement (NDA)",
        "Lease Agreement",
        "General Legal Agreement"
    ]
)

parties = st.text_area(
    "Parties Involved",
    placeholder="Example: Employer: ABC Company; Employee: John"
)

terms = st.text_area(
    "Terms and Conditions",
    placeholder="Enter important terms separated by semicolons"
)

dates = st.text_input(
    "Effective Date",
    placeholder="Example: 01-10-2026"
)

if st.button("Generate Document"):
    if not parties or not terms or not dates:
        st.warning("Please enter all required details.")
    else:
        document = f"""LEGAL DOCUMENT

Document Type: {document_type}

Parties:
{parties}

Effective Date:
{dates}

Terms and Conditions:
{terms}

IMPORTANT NOTICE:
This document is generated for educational and drafting purposes.
Please have a qualified legal professional review it before use.
"""

        st.session_state["document"] = document
        st.success("Document generated successfully!")

if "document" in st.session_state:

    st.subheader("Document Preview")

    edited_document = st.text_area(
        "Edit Document",
        value=st.session_state["document"],
        height=400
    )

    st.session_state["document"] = edited_document

    st.download_button(
        "Download TXT",
        data=edited_document,
        file_name="LegalEase_Document.txt",
        mime="text/plain"
)
