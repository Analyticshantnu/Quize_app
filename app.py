import streamlit as st

# Quiz Questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which language is used for web apps with Streamlit?",
        "options": ["Java", "Python", "C++", "PHP"],
        "answer": "Python"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "12", "13", "14"],
        "answer": "12"
    }
]

st.title("📝 Simple Quiz App")

st.write("Answer the questions below and click **Submit**.")

user_answers = []

# Display Questions
for i, q in enumerate(questions):
    answer = st.radio(
        f"Q{i+1}. {q['question']}",
        q["options"],
        key=f"q{i}"
    )
    user_answers.append(answer)

# Submit Button
if st.button("Submit"):
    score = 0

    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1

    st.success(f"🎉 Your Score: {score}/{len(questions)}")

    st.write("### Results")
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            st.write(f"✅ Q{i+1}: Correct")
        else:
            st.write(
                f"❌ Q{i+1}: Wrong\n"
                f"- Your answer: {user_answers[i]}\n"
                f"- Correct answer: {q['answer']}"
            )