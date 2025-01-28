
# AI Ask PDF

A local tool powered by Ollama, LangChain, and llama3.2 to read a PDF using advanced embeddings and a large language model. Designed for efficiency, it utilizes an NVIDIA GPU with 12 GB VRAM.

---

## How It Works

1. **PDF Reading**: The script reads the data from a specified PDF file.
2. **Embedding Selection**: Relevant data is selected using embeddings.
3. **LLM Query**: The language model generates responses based on your questions.

---

## Example Output using Testdata `main.py`

`Question: Wer sind Formwandler?`

````
Basierend auf dem Kontext, die Formwandler könnten höher entwickelte Wesen sein, die sich in Menschen verwandeln oder durch eine 
Beeinflussung des Menschen als Menschen erscheinen. Sie könnten verschiedene Arten der Formwandlung haben, wie zum Beispiel die Fähigkeit, 
sich in andere Tiere zu verwandeln oder physisch ein anderes Wesen zu sein und den Menschen so zu machen, dass er ihre Form annimmt.  
Es gibt auch Hinweise darauf, dass es zwischen diesen Wesen und Menschen eine Art von Kooperation oder sogar Kontrolle geben könnte, 
insbesondere im Zusammenhang mit Mönchen und Trancezuständen. Es ist jedoch unklar, ob die Absichten dieser Wesen positiv oder negativ sind.
````

## Preparation

### Install Ollama

Download and install Ollama from [their official website](https://ollama.com/).

### Create a Virtual Environment

In the root directory of the project:
```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
.venv\Scripts\activate   # For Windows
```

### Install Dependencies

Run the following command to install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## Usage

### Start the Ollama Server

Ensure the Ollama server is running. You can start it with:
```bash
ollama serve
```

Pull Model:
```bash
ollama pull llama3.2
```

Pull Embedding Model:
```bash
ollama pull nomic-embed-text
```

### Run the Script

Execute the main script to use the tool:
```bash
python main.py
```

---

## Legal Information

- This tool uses open-source models and embeddings. Refer to their respective licenses for compliance.
- Ensure your use case complies with data protection regulations, particularly when handling sensitive or personal information.
- The authors provide no warranty and assume no liability for any issues arising from the use of this tool.

---