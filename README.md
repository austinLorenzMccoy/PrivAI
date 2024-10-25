
# PrivAI Repository

## Overview
PrivAI is a browser extension that integrates advanced AI concepts including Keras, LoRA, Google Gemini, Differential Privacy, and Federated Learning. The extension communicates with a backend API to perform training and inference securely while preserving user privacy.

## Features
- **Browser Extension (Frontend)**: Simple user interface for model interaction.
- **Backend API**: Built with Flask to handle model training and inference requests.
- **Model Training**: Utilizes Keras with LoRA for fine-tuning models.
- **Differential Privacy**: Ensures secure training of models using Opacus.
- **Federated Learning**: Allows decentralized data usage (optional).
- **Inference**: Uses Google Gemini for secure model inference.

## Getting Started

### Prerequisites
- Python 3.x
- Node.js (for building the frontend)
- Google Cloud account with access to Google Gemini

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd PrivAI
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the `.env` File**
   Create a `.env` file in the root directory and add your Google API key:
   ```bash
   GOOGLE_API_KEY=your_google_gemini_api

_key_here
   ```

5. **Run the Backend Server**
   ```bash
   python api/server.py
   ```

6. **Build the Frontend**
   - Follow your specific instructions to set up the frontend (if applicable).

7. **Access the Extension**
   Load the unpacked extension in your browser (usually under Developer Mode).

## Usage
- Click the "Run AI" button on the extension popup to trigger inference using the selected model.

## Contributing
We welcome contributions! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.



