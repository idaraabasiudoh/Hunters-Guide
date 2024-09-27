cover_letter_standards = """
Cover Letter Standards:

GENERAL RULES:
- The cover letter must be 4 or 5 paragraphs long, including a subject, salutation and complimentary close.
- Do not use adverbs and adjectives and filler words.
- Include subject. Example: "Subject: Application xxxxxxxxx Position"
- Use the salutation: "Dear {Company Name} Recruiter"
- DO NOT USE "Honed", "Express", "Enthusiasm", "Thrilled", "Tenure", "Excited", "Enthusiastic", or "Strong" in the cover letter
- If the resume doesn't match the experience properly, highlight transferable skills that add value to the role (e.g., leadership, communication, problem-solving, project management).
- Incorporate known company facts and history to make the cover letter unique.

FORMAT:

Introductory Paragraph (1 Paragraph):
- Clearly state the purpose of the letter and provide a brief professional introduction.
- Specify why you are interested in the specific position and organization.
- Provide an overview of the main strengths and skills you bring to the role.

Body Paragraphs (2 - 3 Paragraphs):
- Cite examples from your technical experience that relate to the job and demonstrate your ability to succeed in the position.
- Offer additional details about key experiences without simply repeating your resume.
- Discuss developed technical skills (including certifications) that relate to the job.
- Include examples of soft skills that, while not directly related to the job, support your potential success in the role.

Closing Paragraph (1 Paragraph):
- Restate your interest in the role and summarize why you are a good candidate.
- Thank the reader for their time and consideration.
"""




refine = """
Rearranging the body based on significance to the role. Talk about relevant skills, projects and expereince first before the less relevant experiences.
After stating each skill, project or expereince explain briefly how this directly relates to the job based on the job description given.
Ensure cover letter is 4 or 5 paragraphs long
"""

refine_2 = """
Replacing use of "Honed", "Express", "Enthusiasm", "Thrilled", "Tenure", "Excited", "Enthusiastic", "Leverage" or "Strong" (if any) in the cover letter with better synonyms.
Removing unecessary adverbs, adjectives and other filler words to make cover letter breif, professional and to the point.
"""

grade_prompt = """
Give a resume score out of 10 in one line. Ex: Resume Score: 9/10. Then proceed to give insights and room for improvements in another line. List out all keywords to include in resume based on job description. If either resume or job description is missing tell user to input them.
"""