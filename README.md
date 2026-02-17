
# AI Ask PDF

A local tool powered by Ollama, LangChain, and deepseek-r1:8b to read a PDF using advanced embeddings and a large language model. Designed for efficiency, it utilizes an NVIDIA GPU with 12 GB VRAM.

---

## How It Works

1. **PDF Reading**: The script reads the data from a specified PDF file.
2. **Embedding Selection**: Relevant data is selected using embeddings.
3. **LLM Query**: The language model generates responses based on your questions.

---

## Example Output using Testdata `main.py`

`Question: Wer sind Formwandler?`

````
Die Hauptdarsteller in diesem Kontext sind:  1. 
*
*Miss de Bourgh
*
* – Eine prominente Figur, deren Heiratsprojekt im Mittelpunkt steht. 2. 
*
*Mr. Darcy
*
* – Ein zentraler Held, dessen Handlungen und Widerspruch zu den Ereignissen hervorgehoben werden. 3. 
*
*Miss Bennet (Elizabeth)
*
* – Die Hauptfigur, die sich aktiv in die Handlungen einmischt und deren Reaktionen zentral sind. 4. 
*
*Lady Catherine
*
* – Als eine mächtige Persönlichkeit, die durch ihre Meinungen und die Folgen ihrer Aussagen betont wird. 5. 
*
*Mr. Bingley
*
* – Ein weiterer wichtiger Figür, dessen Beziehung und Interaktionen Teil des Geschehens sind. 6. 
*
*Mrs. Bennet
*
* – Die Mutter, die durch ihre Anliegen und Handlungen die Familiengeschichte vorantreibt.  Diese Personen treiben die Handlungen und Diskussionen voran und bilden die Kernfigur des Textes.````
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