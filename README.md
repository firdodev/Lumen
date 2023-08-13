# Lumen

## Introduction

Lumen is a AI personal assistant for pc which will help you with daily tasks and if you need everything also in real life using camera view. It can also interact with devices that are connected to lumen.


## How to setup **Lumen**

1. First you need to install the python packages for *Lumen* to work. Open your terminal and write:
    ```bash
    python .\scripts\install_packages.py
    ```
    This will install every package that *Lumen* needs.

2. Add your api key from OpenAi into <a src="src/Lumen/config.json" >config.json</a>

    ```json
    {
    "name": "Lumen",
    "created": "12-8-2023",
    "username": "User",
    "api" : "API_HERE"
    }
    ```

2. Run the LumenApp.py
    ```bash
    python .\src\LumenApp.py
    ```

## How to use **Lumen**

When Lumen starts and everything is loaded fully you need to activate it for her to listen to you. To activate Lumen you need to say *Lumen* in your Microphone. Than Lumen will listen to your prompts and respond to it. 

To deactivate Lumen you just need to say *Bye*.

## Community
We are open for contribution in our project.

## Licesne

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
