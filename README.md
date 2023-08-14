<p align="center">
  <img src=".gitassets/Lumen.gif" alt="Description of GIF" loop="true" width="70%">
</p>

<h1 align="center">Lumen</h1>
<h3 align="center">Your AI Personal Assistant for PC</h3>

---

### 🌟 Introduction

Lumen is an **AI personal assistant** tailored for PCs. It's designed to assist with daily tasks, and when paired with a camera, it can aid in real-life scenarios. Additionally, Lumen can seamlessly interact with devices connected to it.

---


### 🚀 How to Setup

**1. Install Python Packages:**

Before you start, ensure you have the necessary python packages. In your terminal, execute:

```bash
python .\scripts\install_packages.py
```

This will install every package that *Lumen* needs.

**2. Configure API Key:**

Insert your OpenAi API key in the <a href="src/Lumen/config.json">config.json</a> file.

```json
{
    "name": "Lumen",
    "created": "12-8-2023",
    "username": "User",
    "api" : "API_HERE"
}
```

**3. Launch Lumen:**

```bash
python .\src\LumenApp.py
```

### 🎙️ How to Use **Lumen**

After Lumen is fully initialized, activate it by saying **"Lumen"** into your microphone. Lumen will then listen and respond to your prompts.

🔴 To deactivate Lumen, simply say **"Bye"**.

### 💼 Community
We're passionate about collaboration! Feel free to contribute to our project and help us enhance Lumen's capabilities.

### 📜 License

MIT License

Copyright (c) 2023 Firdo.dev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

<p align="center">
</p>
