import streamlit as st
import pandas as pd

from resume_parser import (
    extract_text,
    extract_skills
)

from ranking import (
    calculate_score,
    skill_gap
)

from export_csv import (
    export_candidates
)

st.set_page_config(
    page_title="AI Resume Screening System",
    layout="wide"
)

st.title("🤖 AI Resume Screening & Candidate Ranking System")

job_description = st.text_area(
    "Paste Job Description"
)

uploaded_files = st.file_uploader(
    "Upload Resumes (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Analyze Resumes"):

    if job_description == "":

        st.warning(
            "Please enter job description."
        )

    else:

        results = []

        required_skills = extract_skills(
            job_description.lower()
        )

        for file in uploaded_files:

            resume_text = extract_text(file)

            skills = extract_skills(
                resume_text
            )

            score = calculate_score(
                resume_text,
                job_description
            )

            gaps = skill_gap(
                skills,
                required_skills
            )

            results.append({

                "Candidate":
                    file.name,

                "Score (%)":
                    score,

                "Skills":
                    ", ".join(skills),

                "Missing Skills":
                    ", ".join(gaps)
            })

        df = pd.DataFrame(results)

        df = df.sort_values(
            by="Score (%)",
            ascending=False
        )

        st.subheader(
            "🏆 Candidate Rankings"
        )

        st.dataframe(df)

        st.subheader(
            "🔟 Top Candidates"
        )

        st.dataframe(
            df.head(10)
        )

        csv_file = export_candidates(
            df
        )

        with open(csv_file, "rb") as f:

            st.download_button(
                "📥 Download Shortlisted CSV",
                data=f,
                file_name=
                "shortlisted_candidates.csv",
                mime="text/csv"
            )