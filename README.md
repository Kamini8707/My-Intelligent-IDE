# My Intelligent-IDE

An AI-powered IDE that automates code generation, debugging, testing, and documentation using OpenAI's API.

---

## 🚀 Features

- **Code Generation**: Automatically generate code based on user prompts.
- **Debugging**: AI-assisted debugging for efficient error detection.
- **Testing**: Run automated tests on your code.
- **Documentation**: Generate structured documentation for your code.

---

## 🔧 Prerequisites

- **Python 3.6 or higher** ➝ [Download Python](https://www.python.org/downloads/)
- **OpenAI API Key** ➝ [Get API Key](https://platform.openai.com/account/api-keys)

---

## 📥 Setup

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/your-username/intelligent-ide.git
cd intelligent-ide
```

### **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3️⃣ Add Your OpenAI API Key**

- Create a `.env` file in the project root.
- Add your OpenAI API key:

```bash
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

---

## 🚀 Running the Application

```bash
python main.py
```

---

## 🛠 Usage

### **1️⃣ Code Generation**

- Type a prompt in the text editor (e.g., "Create a function to sort a list").
- Click the **Generate Code** button.
- The AI will generate and insert the corresponding code into the editor.

### **2️⃣ Debugging**

- Write some code in the editor.
- Click the **Debug Code** button.
- A new window will show the debugging output.

### **3️⃣ Testing**

- Write some code in the editor.
- Click the **Run Tests** button.
- A new window will show the test results.

### **4️⃣ Documentation**

- Write some code in the editor.
- Click the **Generate Docs** button.
- A new window will show the generated documentation.

---

## 📂 Project Structure
```bash
intelligent-ide/
│── main.py              # Main application file
│── code_generator.py    # AI-powered code generation module
│── debugger.py          # Debugging module
│── tester.py            # Testing module
│── documentation.py     # Documentation module
│── README.md            # Project documentation
```

---

## 🔧 Troubleshooting

### **1️⃣ Invalid API Key**

- Ensure the API key is correctly copied and pasted.
- Generate a new API key if necessary.

### **2️⃣ Library Issues**

- Ensure you’re using the latest version of the OpenAI library:

```bash
pip install --upgrade openai
```

### **3️⃣ Model Name**

- Use the correct model name (`text-davinci-003` or later versions).

---

## 🔒 Securing Your API Key

Do **not** share your API key publicly or commit it to version control. Use environment variables to store the API key securely:

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

### **Set the environment variable:**

#### **Windows:**

```cmd
setx OPENAI_API_KEY "your-api-key-here"
```

#### **macOS/Linux:**

```bash
export OPENAI_API_KEY="your-api-key-here"
```

---

## 💡 Example Workflow

1. Open the IDE.
2. Type a prompt like **"Create a function to calculate factorial"**.
3. Click **Generate Code**.
4. The IDE generates:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

5. Click **Debug Code** to debug the function.
6. Click **Run Tests** to test the function.
7. Click **Generate Docs** to create documentation.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeatureName`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/YourFeatureName`
5. Open a pull request.

---

## 📜 License

This project is licensed under the **MIT License**. See the LICENSE file for details.

---

## 📞 Contact

For questions or feedback, please contact:

- **Email**: [kaminiprajapati727@gmail.com](mailto\:kaminiprajapati727@gmail.com)


