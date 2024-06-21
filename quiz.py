import streamlit as st

# Define questions and answers
quiz_data = [

    # Question 7
    {
        "question": "Which method is used to display the first rows of a DataFrame in PySpark?",
        "options": ["show()", "head()", "display()", "first()"],
        "answer": "show()"
    },

    # Question 8
    {
        "question": "Which transformation is used to sort a DataFrame in descending order in PySpark?",
        "options": ["sort(desc())", "orderBy(desc())", "sort_desc()", "desc_sort()"],
        "answer": "orderBy(desc())"
    },

    # Question 9
    {
        "question": "Which function is used to aggregate data in PySpark?",
        "options": ["group()", "aggregate()", "collect()", "groupBy()"],
        "answer": "groupBy()"
    },

    # Question 10
    {
        "question": "What is the difference between cache() and persist() in PySpark?",
        "options": [
            "No difference, they are synonyms.",
            "cache() stores data in memory, while persist() allows specifying other storage options.",
            "persist() stores data in memory, while cache() stores it on disk.",
            "cache() is used for DataFrames, while persist() is used for RDDs."
        ],
        "answer": "cache() stores data in memory, while persist() allows specifying other storage options."
    },

    # Question 11
    {
        "question": "Which method is used to rename a column in a PySpark DataFrame?",
        "options": ["renameColumn()", "withColumnRenamed()", "alterColumn()", "changeColumnName()"],
        "answer": "withColumnRenamed()"
    },

    # Question 12
    {
        "question": "Which function is used to calculate the average of a numeric column in PySpark?",
        "options": ["mean()", "average()", "avg()", "calculate_mean()"],
        "answer": "avg()"
    },
]

def main():
    st.title("PySpark Quiz")

    score = 0
    for i, q in enumerate(quiz_data):
        st.subheader(f"Question {i+1}")
        st.write(q["question"])
        options = q["options"]
        answer = st.radio("Choose an option", options, key=i)

        if st.button(f"Submit Answer {i+1}", key=f"submit_{i}"):
            if answer == q["answer"]:
                st.write("Correct!")
                score += 1
            else:
                st.write(f"Wrong! The correct answer is {q['answer']}.")

    st.write(f"Your final score is {score}/{len(quiz_data)}")

    st.write('Sofiane Chehboune/https://www.linkedin.com/in/sofiane-chehboune-5b243766/')

if __name__ == "__main__":
    main()
