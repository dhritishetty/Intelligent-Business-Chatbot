# Intelligent Business Chatbot
## Overview
This project provides a chatbot to enhance business interactions using Flask and MistralAI. The chatbot can interact with users, understand queries and use indexed documents ('.pdf' and '.txt' documents) to provide accurate responses. When a query is out of scope, it directs users to contact the business directly.

## Features
- Easily customizable to fit specific business needs
- Minimalistic user interface for seamless interaction
- Handles out-of-scope questions by directing users to contact the business

## How to Run the Project

Follow these steps to set up and run the chatbot:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/dhritishetty/Intelligent-Business-Chatbot.git
   cd Intelligent-Business-Chatbot
	 ```
2. **Install Dependencies:**
   - **Create a virtual environment (optional but recommended):**
     ```bash
     python -m venv env
     env\Scripts\activate
     ```
   - **Install the required packages:**
     ```bash
     pip install -r requirements.txt
     ```
 
3. **Set Up the Environment:**
   - **Change the directory to main**
     ```bash
     cd main
     ```
     Please ensure you have your business information file (either in '.txt' or '.pdf' format) in the main directory. This file will be processed to extract text for the chatbot to use.

4. **Run the Application:**
   - **Update API Key:**
     - Update the **api_key** variable in python `chatbot.py` with your MistralAI API key.
   - **Make changes in extract_text.py according to your file:**
     - If your file is of '.pdf' format comment out the '.txt' format function and vice versa.
     - Place your business information file in the root directory and make changes in the path (in function) accordingly. The file should contain the content that the chatbot will reference.
   - **Run extract_text.py to extract text from the file:**
      ```bash
      python extract_text.py
      ```
   - **Run the chatbot.py to start the server:**
      ```bash
      python chatbot.py
      ```
Open your web browser and navigate to http://127.0.0.1:5000/ to interact with the chatbot.
