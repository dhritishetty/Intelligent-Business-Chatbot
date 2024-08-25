import fitz

# # Function to extract text from PDF
# def extract_text_from_pdf(pdf_path):
#     document = fitz.open(pdf_path)
#     text_content = ""
#     for page_num in range(len(document)):
#         page = document.load_page(page_num)
#         text_content += page.get_text()
#     return text_content

# # Extract text from the PDF
# pdf_path = 'constitution.pdf'
# text_content = extract_text_from_pdf(pdf_path)


#Function to extract text from txt file
def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        text_content = file.read()
    return text_content

# Extract text from txt
txt_path = 'constitution.txt'
text_content = extract_text_from_txt(txt_path)


# Save the extracted text to a file
with open('extracted_text.txt', 'w', encoding='utf-8') as text_file:
    text_file.write(text_content)

print("Text content extracted and saved to 'extracted_text.txt'")