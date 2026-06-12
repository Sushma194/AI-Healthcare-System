def get_healthcare_response(user_query):

    query = user_query.lower()

    if "fever" in query:

        return """
🤒 Fever Suggestions

• Drink plenty of water
• Take adequate rest
• Monitor temperature
• Eat nutritious food

Consult a doctor if fever lasts more than 3 days.
"""

    elif "headache" in query or "head ache" in query:

        return """
🤕 Headache Suggestions

• Drink plenty of water
• Take proper sleep
• Reduce screen time
• Avoid stress
• Rest in a quiet environment

Seek medical attention if:
• Severe headache occurs suddenly
• Vision problems occur
• Headache lasts several days
"""

    elif "cough" in query:

        return """
😷 Cough Suggestions

• Drink warm water
• Steam inhalation
• Avoid cold drinks
• Take adequate rest
"""

    elif "diabetes" in query:

        return """
🩺 Diabetes Care

• Monitor blood sugar regularly
• Follow healthy diet
• Exercise daily
• Take medications as prescribed
"""

    else:

        return f"""
Healthcare Guidance:

For symptoms like:
• Fever
• Headache
• Cough
• Diabetes

Please describe your symptoms in more detail.
"""