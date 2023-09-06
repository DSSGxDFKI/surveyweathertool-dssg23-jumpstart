import pandas as pd
from io import StringIO
from PIL import Image
import streamlit as st
from src.dashboard.utils import read_logos

def run_dashboard():
    # # Home Page Configuration
    # st.set_page_config(
    #         page_title="Home",
    #         page_icon="👋",
    #     )

    # Page Aesthetics and Texts
    st.write("# DSSG X UNICEF X STC 👋")
    st.markdown(
        """
        DSSGx 2023 Team JMPST worked in collaboration with the 
        United Nations International Children's Emergency Fund [(UNICEF)](https://www.unicef.org/social-policy/child-poverty) 
        and Save the Children [(STC)](https://www.savethechildren.de/?gclid=CjwKCAjw5_GmBhBIEiwA5QSMxKhDi4CiaQ_7w7UocSfSfLqV-RmiB5Wr5S-9KViLmK4fNqDA331CrRoCtiAQAvD_BwE)
        in order to help in the effort to connect extreme weather events with child poverty. 

        **👈 Select a Page from the sidebar** to view the tools our team created.

        ### Want to learn more?
        - Check out [Data Science for Social Good - Kaiserslautern, Germany](https://datasciapps.de/dssg/)
        - Jump into our [documentation](https://docs.streamlit.io) *Insert link to Sphinx?
    """
    )

    with st.expander("MIT License"):
        st.write(
            """
        MIT License

        Copyright (c) 2023 Data Science for Social Good (RPTU and DFKI)

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
        """
        )

    # Side Bar Set Up
    st.sidebar.markdown(
        """
            <style>
                [data-testid="stVerticalBlock"] > img:first-child {
                    margin-top: -60px;
                }

                [data-testid=stImage]{
                    text-align: center;
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 100%;
                }
            </style>
            """,
        unsafe_allow_html=True,
    )
    # Add Sidebar images
    STCimage, UNICEFimage, DSAimage, NOAAimage = read_logos("surveyweathertool/logos")
    st.sidebar.image(UNICEFimage, width=250)
    st.sidebar.image(STCimage, width=250)
    st.sidebar.image(DSAimage, width=125)

    st.sidebar.markdown(
        f"<h5 style='text-align: center; color: black;'>Copyright (c) 2023 Data Science for Social Good (RPTU and DFKI) </h4>",
        unsafe_allow_html=True,
    )

run_dashboard()
