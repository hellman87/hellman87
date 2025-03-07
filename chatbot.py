{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/hellman87/hellman87/blob/main/chatbot.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "dQ0K5FHja6UH",
        "collapsed": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b6026107-b31e-4d30-f607-d3e58d1dea32"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[?25l   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/1.2 MB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K   \u001b[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[91m╸\u001b[0m \u001b[32m1.2/1.2 MB\u001b[0m \u001b[31m59.7 MB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\r\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.2/1.2 MB\u001b[0m \u001b[31m30.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h"
          ]
        }
      ],
      "source": [
        "!pip install -q tiktoken"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install langchain"
      ],
      "metadata": {
        "collapsed": true,
        "id": "bvpS11k8WLu8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6865ac04-38ef-447d-8f33-c382ca0ede24"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: langchain in /usr/local/lib/python3.11/dist-packages (0.3.19)\n",
            "Requirement already satisfied: langchain-core<1.0.0,>=0.3.35 in /usr/local/lib/python3.11/dist-packages (from langchain) (0.3.40)\n",
            "Requirement already satisfied: langchain-text-splitters<1.0.0,>=0.3.6 in /usr/local/lib/python3.11/dist-packages (from langchain) (0.3.6)\n",
            "Requirement already satisfied: langsmith<0.4,>=0.1.17 in /usr/local/lib/python3.11/dist-packages (from langchain) (0.3.11)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.7.4 in /usr/local/lib/python3.11/dist-packages (from langchain) (2.10.6)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.11/dist-packages (from langchain) (2.0.38)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.11/dist-packages (from langchain) (2.32.3)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.11/dist-packages (from langchain) (6.0.2)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.11/dist-packages (from langchain) (3.11.13)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from langchain) (9.0.0)\n",
            "Requirement already satisfied: numpy<2,>=1.26.4 in /usr/local/lib/python3.11/dist-packages (from langchain) (1.26.4)\n",
            "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (2.4.6)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.3.2)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (25.1.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.5.0)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (6.1.0)\n",
            "Requirement already satisfied: propcache>=0.2.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (0.3.0)\n",
            "Requirement already satisfied: yarl<2.0,>=1.17.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.18.3)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.11/dist-packages (from langchain-core<1.0.0,>=0.3.35->langchain) (1.33)\n",
            "Requirement already satisfied: packaging<25,>=23.2 in /usr/local/lib/python3.11/dist-packages (from langchain-core<1.0.0,>=0.3.35->langchain) (24.2)\n",
            "Requirement already satisfied: typing-extensions>=4.7 in /usr/local/lib/python3.11/dist-packages (from langchain-core<1.0.0,>=0.3.35->langchain) (4.12.2)\n",
            "Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.17->langchain) (0.28.1)\n",
            "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.17->langchain) (3.10.15)\n",
            "Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.17->langchain) (1.0.0)\n",
            "Requirement already satisfied: zstandard<0.24.0,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.17->langchain) (0.23.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.7.4->langchain) (2.27.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langchain) (2025.1.31)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.11/dist-packages (from SQLAlchemy<3,>=1.4->langchain) (3.1.1)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.17->langchain) (3.7.1)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.17->langchain) (1.0.7)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->langsmith<0.4,>=0.1.17->langchain) (0.14.0)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.11/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<1.0.0,>=0.3.35->langchain) (3.0.0)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio->httpx<1,>=0.23.0->langsmith<0.4,>=0.1.17->langchain) (1.3.1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install langchain-openai"
      ],
      "metadata": {
        "collapsed": true,
        "id": "NXMxAQMUWLjp",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8c6c32c0-29f6-443e-b3fc-3aa14fc40b01"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting langchain-openai\n",
            "  Downloading langchain_openai-0.3.7-py3-none-any.whl.metadata (2.3 kB)\n",
            "Requirement already satisfied: langchain-core<1.0.0,>=0.3.39 in /usr/local/lib/python3.11/dist-packages (from langchain-openai) (0.3.40)\n",
            "Requirement already satisfied: openai<2.0.0,>=1.58.1 in /usr/local/lib/python3.11/dist-packages (from langchain-openai) (1.61.1)\n",
            "Requirement already satisfied: tiktoken<1,>=0.7 in /usr/local/lib/python3.11/dist-packages (from langchain-openai) (0.9.0)\n",
            "Requirement already satisfied: langsmith<0.4,>=0.1.125 in /usr/local/lib/python3.11/dist-packages (from langchain-core<1.0.0,>=0.3.39->langchain-openai) (0.3.11)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from langchain-core<1.0.0,>=0.3.39->langchain-openai) (9.0.0)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.11/dist-packages (from langchain-core<1.0.0,>=0.3.39->langchain-openai) (1.33)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.11/dist-packages (from langchain-core<1.0.0,>=0.3.39->langchain-openai) (6.0.2)\n",
            "Requirement already satisfied: packaging<25,>=23.2 in /usr/local/lib/python3.11/dist-packages (from langchain-core<1.0.0,>=0.3.39->langchain-openai) (24.2)\n",
            "Requirement already satisfied: typing-extensions>=4.7 in /usr/local/lib/python3.11/dist-packages (from langchain-core<1.0.0,>=0.3.39->langchain-openai) (4.12.2)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.5.2 in /usr/local/lib/python3.11/dist-packages (from langchain-core<1.0.0,>=0.3.39->langchain-openai) (2.10.6)\n",
            "Requirement already satisfied: anyio<5,>=3.5.0 in /usr/local/lib/python3.11/dist-packages (from openai<2.0.0,>=1.58.1->langchain-openai) (3.7.1)\n",
            "Requirement already satisfied: distro<2,>=1.7.0 in /usr/local/lib/python3.11/dist-packages (from openai<2.0.0,>=1.58.1->langchain-openai) (1.9.0)\n",
            "Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from openai<2.0.0,>=1.58.1->langchain-openai) (0.28.1)\n",
            "Requirement already satisfied: jiter<1,>=0.4.0 in /usr/local/lib/python3.11/dist-packages (from openai<2.0.0,>=1.58.1->langchain-openai) (0.8.2)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.11/dist-packages (from openai<2.0.0,>=1.58.1->langchain-openai) (1.3.1)\n",
            "Requirement already satisfied: tqdm>4 in /usr/local/lib/python3.11/dist-packages (from openai<2.0.0,>=1.58.1->langchain-openai) (4.67.1)\n",
            "Requirement already satisfied: regex>=2022.1.18 in /usr/local/lib/python3.11/dist-packages (from tiktoken<1,>=0.7->langchain-openai) (2024.11.6)\n",
            "Requirement already satisfied: requests>=2.26.0 in /usr/local/lib/python3.11/dist-packages (from tiktoken<1,>=0.7->langchain-openai) (2.32.3)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.11/dist-packages (from anyio<5,>=3.5.0->openai<2.0.0,>=1.58.1->langchain-openai) (3.10)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->openai<2.0.0,>=1.58.1->langchain-openai) (2025.1.31)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->openai<2.0.0,>=1.58.1->langchain-openai) (1.0.7)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai<2.0.0,>=1.58.1->langchain-openai) (0.14.0)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.11/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<1.0.0,>=0.3.39->langchain-openai) (3.0.0)\n",
            "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<1.0.0,>=0.3.39->langchain-openai) (3.10.15)\n",
            "Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<1.0.0,>=0.3.39->langchain-openai) (1.0.0)\n",
            "Requirement already satisfied: zstandard<0.24.0,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<1.0.0,>=0.3.39->langchain-openai) (0.23.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.5.2->langchain-core<1.0.0,>=0.3.39->langchain-openai) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.5.2->langchain-core<1.0.0,>=0.3.39->langchain-openai) (2.27.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests>=2.26.0->tiktoken<1,>=0.7->langchain-openai) (3.4.1)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests>=2.26.0->tiktoken<1,>=0.7->langchain-openai) (2.3.0)\n",
            "Downloading langchain_openai-0.3.7-py3-none-any.whl (55 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m55.3/55.3 kB\u001b[0m \u001b[31m2.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: langchain-openai\n",
            "Successfully installed langchain-openai-0.3.7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install cohere"
      ],
      "metadata": {
        "collapsed": true,
        "id": "umji_ozuWLUI",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6ff89b67-d33d-4a6f-e083-5eba1a6896e5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting cohere\n",
            "  Downloading cohere-5.14.0-py3-none-any.whl.metadata (3.4 kB)\n",
            "Collecting fastavro<2.0.0,>=1.9.4 (from cohere)\n",
            "  Downloading fastavro-1.10.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.5 kB)\n",
            "Requirement already satisfied: httpx>=0.21.2 in /usr/local/lib/python3.11/dist-packages (from cohere) (0.28.1)\n",
            "Collecting httpx-sse==0.4.0 (from cohere)\n",
            "  Downloading httpx_sse-0.4.0-py3-none-any.whl.metadata (9.0 kB)\n",
            "Requirement already satisfied: pydantic>=1.9.2 in /usr/local/lib/python3.11/dist-packages (from cohere) (2.10.6)\n",
            "Requirement already satisfied: pydantic-core<3.0.0,>=2.18.2 in /usr/local/lib/python3.11/dist-packages (from cohere) (2.27.2)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from cohere) (2.32.3)\n",
            "Requirement already satisfied: tokenizers<1,>=0.15 in /usr/local/lib/python3.11/dist-packages (from cohere) (0.21.0)\n",
            "Collecting types-requests<3.0.0,>=2.0.0 (from cohere)\n",
            "  Downloading types_requests-2.32.0.20250306-py3-none-any.whl.metadata (2.3 kB)\n",
            "Requirement already satisfied: typing_extensions>=4.0.0 in /usr/local/lib/python3.11/dist-packages (from cohere) (4.12.2)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.11/dist-packages (from httpx>=0.21.2->cohere) (3.7.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.11/dist-packages (from httpx>=0.21.2->cohere) (2025.1.31)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx>=0.21.2->cohere) (1.0.7)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from httpx>=0.21.2->cohere) (3.10)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx>=0.21.2->cohere) (0.14.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic>=1.9.2->cohere) (0.7.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.0.0->cohere) (3.4.1)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.0.0->cohere) (2.3.0)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.16.4 in /usr/local/lib/python3.11/dist-packages (from tokenizers<1,>=0.15->cohere) (0.28.1)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.11/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers<1,>=0.15->cohere) (3.17.0)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers<1,>=0.15->cohere) (2024.10.0)\n",
            "Requirement already satisfied: packaging>=20.9 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers<1,>=0.15->cohere) (24.2)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers<1,>=0.15->cohere) (6.0.2)\n",
            "Requirement already satisfied: tqdm>=4.42.1 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers<1,>=0.15->cohere) (4.67.1)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio->httpx>=0.21.2->cohere) (1.3.1)\n",
            "Downloading cohere-5.14.0-py3-none-any.whl (253 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m253.9/253.9 kB\u001b[0m \u001b[31m10.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading httpx_sse-0.4.0-py3-none-any.whl (7.8 kB)\n",
            "Downloading fastavro-1.10.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.3 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.3/3.3 MB\u001b[0m \u001b[31m67.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading types_requests-2.32.0.20250306-py3-none-any.whl (20 kB)\n",
            "Installing collected packages: types-requests, httpx-sse, fastavro, cohere\n",
            "Successfully installed cohere-5.14.0 fastavro-1.10.0 httpx-sse-0.4.0 types-requests-2.32.0.20250306\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install langchain_google_genai"
      ],
      "metadata": {
        "collapsed": true,
        "id": "IatmHIXFWhhq",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "67a919fc-505a-4602-dc89-07a65570d3f3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting langchain_google_genai\n",
            "  Downloading langchain_google_genai-2.0.11-py3-none-any.whl.metadata (3.6 kB)\n",
            "Collecting filetype<2.0.0,>=1.2.0 (from langchain_google_genai)\n",
            "  Downloading filetype-1.2.0-py2.py3-none-any.whl.metadata (6.5 kB)\n",
            "Collecting google-ai-generativelanguage<0.7.0,>=0.6.16 (from langchain_google_genai)\n",
            "  Downloading google_ai_generativelanguage-0.6.16-py3-none-any.whl.metadata (5.7 kB)\n",
            "Requirement already satisfied: langchain-core<0.4.0,>=0.3.37 in /usr/local/lib/python3.11/dist-packages (from langchain_google_genai) (0.3.40)\n",
            "Requirement already satisfied: pydantic<3,>=2 in /usr/local/lib/python3.11/dist-packages (from langchain_google_genai) (2.10.6)\n",
            "Requirement already satisfied: google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1 in /usr/local/lib/python3.11/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (2.24.1)\n",
            "Requirement already satisfied: google-auth!=2.24.0,!=2.25.0,<3.0.0dev,>=2.14.1 in /usr/local/lib/python3.11/dist-packages (from google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (2.38.0)\n",
            "Requirement already satisfied: proto-plus<2.0.0dev,>=1.22.3 in /usr/local/lib/python3.11/dist-packages (from google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (1.26.0)\n",
            "Requirement already satisfied: protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<6.0.0dev,>=3.20.2 in /usr/local/lib/python3.11/dist-packages (from google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (4.25.6)\n",
            "Requirement already satisfied: langsmith<0.4,>=0.1.125 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (0.3.11)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (9.0.0)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (1.33)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (6.0.2)\n",
            "Requirement already satisfied: packaging<25,>=23.2 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (24.2)\n",
            "Requirement already satisfied: typing-extensions>=4.7 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (4.12.2)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3,>=2->langchain_google_genai) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.11/dist-packages (from pydantic<3,>=2->langchain_google_genai) (2.27.2)\n",
            "Requirement already satisfied: googleapis-common-protos<2.0.dev0,>=1.56.2 in /usr/local/lib/python3.11/dist-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (1.69.0)\n",
            "Requirement already satisfied: requests<3.0.0.dev0,>=2.18.0 in /usr/local/lib/python3.11/dist-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (2.32.3)\n",
            "Requirement already satisfied: grpcio<2.0dev,>=1.33.2 in /usr/local/lib/python3.11/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (1.70.0)\n",
            "Requirement already satisfied: grpcio-status<2.0.dev0,>=1.33.2 in /usr/local/lib/python3.11/dist-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (1.62.3)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from google-auth!=2.24.0,!=2.25.0,<3.0.0dev,>=2.14.1->google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (5.5.2)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.11/dist-packages (from google-auth!=2.24.0,!=2.25.0,<3.0.0dev,>=2.14.1->google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (0.4.1)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.11/dist-packages (from google-auth!=2.24.0,!=2.25.0,<3.0.0dev,>=2.14.1->google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (4.9)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.11/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (3.0.0)\n",
            "Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (0.28.1)\n",
            "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (3.10.15)\n",
            "Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (1.0.0)\n",
            "Requirement already satisfied: zstandard<0.24.0,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (0.23.0)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (3.7.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (2025.1.31)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (1.0.7)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (3.10)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (0.14.0)\n",
            "Requirement already satisfied: pyasn1<0.7.0,>=0.4.6 in /usr/local/lib/python3.11/dist-packages (from pyasn1-modules>=0.2.1->google-auth!=2.24.0,!=2.25.0,<3.0.0dev,>=2.14.1->google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (0.6.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (3.4.1)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage<0.7.0,>=0.6.16->langchain_google_genai) (2.3.0)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio->httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.37->langchain_google_genai) (1.3.1)\n",
            "Downloading langchain_google_genai-2.0.11-py3-none-any.whl (39 kB)\n",
            "Downloading filetype-1.2.0-py2.py3-none-any.whl (19 kB)\n",
            "Downloading google_ai_generativelanguage-0.6.16-py3-none-any.whl (1.4 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.4/1.4 MB\u001b[0m \u001b[31m41.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: filetype, google-ai-generativelanguage, langchain_google_genai\n",
            "  Attempting uninstall: google-ai-generativelanguage\n",
            "    Found existing installation: google-ai-generativelanguage 0.6.15\n",
            "    Uninstalling google-ai-generativelanguage-0.6.15:\n",
            "      Successfully uninstalled google-ai-generativelanguage-0.6.15\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "google-generativeai 0.8.4 requires google-ai-generativelanguage==0.6.15, but you have google-ai-generativelanguage 0.6.16 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0mSuccessfully installed filetype-1.2.0 google-ai-generativelanguage-0.6.16 langchain_google_genai-2.0.11\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "application/vnd.colab-display-data+json": {
              "pip_warning": {
                "packages": [
                  "google"
                ]
              },
              "id": "5006351378274cbfbef729c69539dc2d"
            }
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install langchain-cohere"
      ],
      "metadata": {
        "collapsed": true,
        "id": "X3lWa-DCWNnh",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "32480491-d88f-4486-e359-64ac4f1aea62"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting langchain-cohere\n",
            "  Downloading langchain_cohere-0.4.2-py3-none-any.whl.metadata (6.6 kB)\n",
            "Requirement already satisfied: cohere<6.0,>=5.12.0 in /usr/local/lib/python3.11/dist-packages (from langchain-cohere) (5.14.0)\n",
            "Collecting langchain-community<0.4.0,>=0.3.0 (from langchain-cohere)\n",
            "  Downloading langchain_community-0.3.19-py3-none-any.whl.metadata (2.4 kB)\n",
            "Requirement already satisfied: langchain-core<0.4.0,>=0.3.27 in /usr/local/lib/python3.11/dist-packages (from langchain-cohere) (0.3.40)\n",
            "Requirement already satisfied: pydantic<3,>=2 in /usr/local/lib/python3.11/dist-packages (from langchain-cohere) (2.10.6)\n",
            "Collecting types-pyyaml<7.0.0.0,>=6.0.12.20240917 (from langchain-cohere)\n",
            "  Downloading types_PyYAML-6.0.12.20241230-py3-none-any.whl.metadata (1.8 kB)\n",
            "Requirement already satisfied: fastavro<2.0.0,>=1.9.4 in /usr/local/lib/python3.11/dist-packages (from cohere<6.0,>=5.12.0->langchain-cohere) (1.10.0)\n",
            "Requirement already satisfied: httpx>=0.21.2 in /usr/local/lib/python3.11/dist-packages (from cohere<6.0,>=5.12.0->langchain-cohere) (0.28.1)\n",
            "Requirement already satisfied: httpx-sse==0.4.0 in /usr/local/lib/python3.11/dist-packages (from cohere<6.0,>=5.12.0->langchain-cohere) (0.4.0)\n",
            "Requirement already satisfied: pydantic-core<3.0.0,>=2.18.2 in /usr/local/lib/python3.11/dist-packages (from cohere<6.0,>=5.12.0->langchain-cohere) (2.27.2)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from cohere<6.0,>=5.12.0->langchain-cohere) (2.32.3)\n",
            "Requirement already satisfied: tokenizers<1,>=0.15 in /usr/local/lib/python3.11/dist-packages (from cohere<6.0,>=5.12.0->langchain-cohere) (0.21.0)\n",
            "Requirement already satisfied: types-requests<3.0.0,>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from cohere<6.0,>=5.12.0->langchain-cohere) (2.32.0.20250306)\n",
            "Requirement already satisfied: typing_extensions>=4.0.0 in /usr/local/lib/python3.11/dist-packages (from cohere<6.0,>=5.12.0->langchain-cohere) (4.12.2)\n",
            "Collecting langchain-core<0.4.0,>=0.3.27 (from langchain-cohere)\n",
            "  Downloading langchain_core-0.3.41-py3-none-any.whl.metadata (5.9 kB)\n",
            "Collecting langchain<1.0.0,>=0.3.20 (from langchain-community<0.4.0,>=0.3.0->langchain-cohere)\n",
            "  Downloading langchain-0.3.20-py3-none-any.whl.metadata (7.7 kB)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.11/dist-packages (from langchain-community<0.4.0,>=0.3.0->langchain-cohere) (2.0.38)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.11/dist-packages (from langchain-community<0.4.0,>=0.3.0->langchain-cohere) (6.0.2)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.11/dist-packages (from langchain-community<0.4.0,>=0.3.0->langchain-cohere) (3.11.13)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from langchain-community<0.4.0,>=0.3.0->langchain-cohere) (9.0.0)\n",
            "Collecting dataclasses-json<0.7,>=0.5.7 (from langchain-community<0.4.0,>=0.3.0->langchain-cohere)\n",
            "  Downloading dataclasses_json-0.6.7-py3-none-any.whl.metadata (25 kB)\n",
            "Collecting pydantic-settings<3.0.0,>=2.4.0 (from langchain-community<0.4.0,>=0.3.0->langchain-cohere)\n",
            "  Downloading pydantic_settings-2.8.1-py3-none-any.whl.metadata (3.5 kB)\n",
            "Requirement already satisfied: langsmith<0.4,>=0.1.125 in /usr/local/lib/python3.11/dist-packages (from langchain-community<0.4.0,>=0.3.0->langchain-cohere) (0.3.11)\n",
            "Requirement already satisfied: numpy<3,>=1.26.2 in /usr/local/lib/python3.11/dist-packages (from langchain-community<0.4.0,>=0.3.0->langchain-cohere) (1.26.4)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.27->langchain-cohere) (1.33)\n",
            "Requirement already satisfied: packaging<25,>=23.2 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.27->langchain-cohere) (24.2)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3,>=2->langchain-cohere) (0.7.0)\n",
            "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community<0.4.0,>=0.3.0->langchain-cohere) (2.4.6)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community<0.4.0,>=0.3.0->langchain-cohere) (1.3.2)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community<0.4.0,>=0.3.0->langchain-cohere) (25.1.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community<0.4.0,>=0.3.0->langchain-cohere) (1.5.0)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community<0.4.0,>=0.3.0->langchain-cohere) (6.1.0)\n",
            "Requirement already satisfied: propcache>=0.2.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community<0.4.0,>=0.3.0->langchain-cohere) (0.3.0)\n",
            "Requirement already satisfied: yarl<2.0,>=1.17.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community<0.4.0,>=0.3.0->langchain-cohere) (1.18.3)\n",
            "Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json<0.7,>=0.5.7->langchain-community<0.4.0,>=0.3.0->langchain-cohere)\n",
            "  Downloading marshmallow-3.26.1-py3-none-any.whl.metadata (7.3 kB)\n",
            "Collecting typing-inspect<1,>=0.4.0 (from dataclasses-json<0.7,>=0.5.7->langchain-community<0.4.0,>=0.3.0->langchain-cohere)\n",
            "  Downloading typing_inspect-0.9.0-py3-none-any.whl.metadata (1.5 kB)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.11/dist-packages (from httpx>=0.21.2->cohere<6.0,>=5.12.0->langchain-cohere) (3.7.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.11/dist-packages (from httpx>=0.21.2->cohere<6.0,>=5.12.0->langchain-cohere) (2025.1.31)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx>=0.21.2->cohere<6.0,>=5.12.0->langchain-cohere) (1.0.7)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from httpx>=0.21.2->cohere<6.0,>=5.12.0->langchain-cohere) (3.10)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx>=0.21.2->cohere<6.0,>=5.12.0->langchain-cohere) (0.14.0)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.11/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.4.0,>=0.3.27->langchain-cohere) (3.0.0)\n",
            "Requirement already satisfied: langchain-text-splitters<1.0.0,>=0.3.6 in /usr/local/lib/python3.11/dist-packages (from langchain<1.0.0,>=0.3.20->langchain-community<0.4.0,>=0.3.0->langchain-cohere) (0.3.6)\n",
            "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-community<0.4.0,>=0.3.0->langchain-cohere) (3.10.15)\n",
            "Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-community<0.4.0,>=0.3.0->langchain-cohere) (1.0.0)\n",
            "Requirement already satisfied: zstandard<0.24.0,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-community<0.4.0,>=0.3.0->langchain-cohere) (0.23.0)\n",
            "Collecting python-dotenv>=0.21.0 (from pydantic-settings<3.0.0,>=2.4.0->langchain-community<0.4.0,>=0.3.0->langchain-cohere)\n",
            "  Downloading python_dotenv-1.0.1-py3-none-any.whl.metadata (23 kB)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.0.0->cohere<6.0,>=5.12.0->langchain-cohere) (3.4.1)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3.0.0,>=2.0.0->cohere<6.0,>=5.12.0->langchain-cohere) (2.3.0)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.11/dist-packages (from SQLAlchemy<3,>=1.4->langchain-community<0.4.0,>=0.3.0->langchain-cohere) (3.1.1)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.16.4 in /usr/local/lib/python3.11/dist-packages (from tokenizers<1,>=0.15->cohere<6.0,>=5.12.0->langchain-cohere) (0.28.1)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.11/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers<1,>=0.15->cohere<6.0,>=5.12.0->langchain-cohere) (3.17.0)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers<1,>=0.15->cohere<6.0,>=5.12.0->langchain-cohere) (2024.10.0)\n",
            "Requirement already satisfied: tqdm>=4.42.1 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub<1.0,>=0.16.4->tokenizers<1,>=0.15->cohere<6.0,>=5.12.0->langchain-cohere) (4.67.1)\n",
            "Collecting mypy-extensions>=0.3.0 (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain-community<0.4.0,>=0.3.0->langchain-cohere)\n",
            "  Downloading mypy_extensions-1.0.0-py3-none-any.whl.metadata (1.1 kB)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio->httpx>=0.21.2->cohere<6.0,>=5.12.0->langchain-cohere) (1.3.1)\n",
            "Downloading langchain_cohere-0.4.2-py3-none-any.whl (42 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m42.2/42.2 kB\u001b[0m \u001b[31m3.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langchain_community-0.3.19-py3-none-any.whl (2.5 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.5/2.5 MB\u001b[0m \u001b[31m64.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading langchain_core-0.3.41-py3-none-any.whl (415 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m415.1/415.1 kB\u001b[0m \u001b[31m34.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading types_PyYAML-6.0.12.20241230-py3-none-any.whl (20 kB)\n",
            "Downloading dataclasses_json-0.6.7-py3-none-any.whl (28 kB)\n",
            "Downloading langchain-0.3.20-py3-none-any.whl (1.0 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.0/1.0 MB\u001b[0m \u001b[31m58.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydantic_settings-2.8.1-py3-none-any.whl (30 kB)\n",
            "Downloading marshmallow-3.26.1-py3-none-any.whl (50 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m50.9/50.9 kB\u001b[0m \u001b[31m4.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)\n",
            "Downloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)\n",
            "Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)\n",
            "Installing collected packages: types-pyyaml, python-dotenv, mypy-extensions, marshmallow, typing-inspect, pydantic-settings, dataclasses-json, langchain-core, langchain, langchain-community, langchain-cohere\n",
            "  Attempting uninstall: langchain-core\n",
            "    Found existing installation: langchain-core 0.3.40\n",
            "    Uninstalling langchain-core-0.3.40:\n",
            "      Successfully uninstalled langchain-core-0.3.40\n",
            "  Attempting uninstall: langchain\n",
            "    Found existing installation: langchain 0.3.19\n",
            "    Uninstalling langchain-0.3.19:\n",
            "      Successfully uninstalled langchain-0.3.19\n",
            "Successfully installed dataclasses-json-0.6.7 langchain-0.3.20 langchain-cohere-0.4.2 langchain-community-0.3.19 langchain-core-0.3.41 marshmallow-3.26.1 mypy-extensions-1.0.0 pydantic-settings-2.8.1 python-dotenv-1.0.1 types-pyyaml-6.0.12.20241230 typing-inspect-0.9.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# import getpass\n",
        "# import os\n",
        "# from google.colab import userdata\n",
        "# userdata.get('COHERE-API-KEY')"
      ],
      "metadata": {
        "collapsed": true,
        "id": "Xa_w-ZLQXKL-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import getpass\n",
        "import os\n",
        "os.environ[\"COHERE_API_KEY\"] = getpass.getpass()\n"
      ],
      "metadata": {
        "id": "nQmAlPOEXmvS",
        "collapsed": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "033f0007-41a3-47da-ae46-8c76aa7d0549"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "··········\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ye3gDxaRY3Xx"
      },
      "source": [
        "import getpass\n",
        "import os\n",
        "os.environ[\"KwFRyl8wL1kQgw4blZnI8ceIv2kV2kjrlRCHNCTe\"] = getpass.getpass()"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "from langchain_cohere.llms import Cohere\n",
        "model = Cohere(temperature=0.1)"
      ],
      "metadata": {
        "id": "WSVzMlQ-YBX-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_cohere.llms import Cohere\n",
        "model= Cohere(temperature=0.1)"
      ],
      "metadata": {
        "id": "-O1Hp387af34"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install langchain-ollama"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "412MR9-nOOtq",
        "outputId": "b9295ad6-5558-439e-dc70-ff1826521b4d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting langchain-ollama\n",
            "  Downloading langchain_ollama-0.2.3-py3-none-any.whl.metadata (1.9 kB)\n",
            "Requirement already satisfied: langchain-core<0.4.0,>=0.3.33 in /usr/local/lib/python3.11/dist-packages (from langchain-ollama) (0.3.41)\n",
            "Collecting ollama<1,>=0.4.4 (from langchain-ollama)\n",
            "  Downloading ollama-0.4.7-py3-none-any.whl.metadata (4.7 kB)\n",
            "Requirement already satisfied: langsmith<0.4,>=0.1.125 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.33->langchain-ollama) (0.3.11)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.33->langchain-ollama) (9.0.0)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.33->langchain-ollama) (1.33)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.33->langchain-ollama) (6.0.2)\n",
            "Requirement already satisfied: packaging<25,>=23.2 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.33->langchain-ollama) (24.2)\n",
            "Requirement already satisfied: typing-extensions>=4.7 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.33->langchain-ollama) (4.12.2)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.5.2 in /usr/local/lib/python3.11/dist-packages (from langchain-core<0.4.0,>=0.3.33->langchain-ollama) (2.10.6)\n",
            "Requirement already satisfied: httpx<0.29,>=0.27 in /usr/local/lib/python3.11/dist-packages (from ollama<1,>=0.4.4->langchain-ollama) (0.28.1)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.11/dist-packages (from httpx<0.29,>=0.27->ollama<1,>=0.4.4->langchain-ollama) (3.7.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.11/dist-packages (from httpx<0.29,>=0.27->ollama<1,>=0.4.4->langchain-ollama) (2025.1.31)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx<0.29,>=0.27->ollama<1,>=0.4.4->langchain-ollama) (1.0.7)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from httpx<0.29,>=0.27->ollama<1,>=0.4.4->langchain-ollama) (3.10)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx<0.29,>=0.27->ollama<1,>=0.4.4->langchain-ollama) (0.14.0)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.11/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.4.0,>=0.3.33->langchain-ollama) (3.0.0)\n",
            "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.33->langchain-ollama) (3.10.15)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.33->langchain-ollama) (2.32.3)\n",
            "Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.33->langchain-ollama) (1.0.0)\n",
            "Requirement already satisfied: zstandard<0.24.0,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.33->langchain-ollama) (0.23.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.5.2->langchain-core<0.4.0,>=0.3.33->langchain-ollama) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.5.2->langchain-core<0.4.0,>=0.3.33->langchain-ollama) (2.27.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.33->langchain-ollama) (3.4.1)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langsmith<0.4,>=0.1.125->langchain-core<0.4.0,>=0.3.33->langchain-ollama) (2.3.0)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio->httpx<0.29,>=0.27->ollama<1,>=0.4.4->langchain-ollama) (1.3.1)\n",
            "Downloading langchain_ollama-0.2.3-py3-none-any.whl (19 kB)\n",
            "Downloading ollama-0.4.7-py3-none-any.whl (13 kB)\n",
            "Installing collected packages: ollama, langchain-ollama\n",
            "Successfully installed langchain-ollama-0.2.3 ollama-0.4.7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_cohere import ChatCohere\n",
        "from langchain_core.prompts import ChatPromptTemplate\n",
        "chat = ChatCohere(model='command-r-plus', temperature=0.1)"
      ],
      "metadata": {
        "id": "pF81t_tsXy-d"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install langchain_core\n",
        "from langchain_core.messages import HumanMessage, SystemMessage"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "1Ui3CBIPZl3q",
        "outputId": "01f294eb-4cd5-4482-bf36-4f1014e0025a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: langchain_core in /usr/local/lib/python3.11/dist-packages (0.3.41)\n",
            "Requirement already satisfied: langsmith<0.4,>=0.1.125 in /usr/local/lib/python3.11/dist-packages (from langchain_core) (0.3.11)\n",
            "Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from langchain_core) (9.0.0)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.11/dist-packages (from langchain_core) (1.33)\n",
            "Requirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.11/dist-packages (from langchain_core) (6.0.2)\n",
            "Requirement already satisfied: packaging<25,>=23.2 in /usr/local/lib/python3.11/dist-packages (from langchain_core) (24.2)\n",
            "Requirement already satisfied: typing-extensions>=4.7 in /usr/local/lib/python3.11/dist-packages (from langchain_core) (4.12.2)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.5.2 in /usr/local/lib/python3.11/dist-packages (from langchain_core) (2.10.6)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.11/dist-packages (from jsonpatch<2.0,>=1.33->langchain_core) (3.0.0)\n",
            "Requirement already satisfied: httpx<1,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain_core) (0.28.1)\n",
            "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain_core) (3.10.15)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain_core) (2.32.3)\n",
            "Requirement already satisfied: requests-toolbelt<2.0.0,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain_core) (1.0.0)\n",
            "Requirement already satisfied: zstandard<0.24.0,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from langsmith<0.4,>=0.1.125->langchain_core) (0.23.0)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.5.2->langchain_core) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.27.2 in /usr/local/lib/python3.11/dist-packages (from pydantic<3.0.0,>=2.5.2->langchain_core) (2.27.2)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain_core) (3.7.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain_core) (2025.1.31)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain_core) (1.0.7)\n",
            "Requirement already satisfied: idna in /usr/local/lib/python3.11/dist-packages (from httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain_core) (3.10)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.11/dist-packages (from httpcore==1.*->httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain_core) (0.14.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langsmith<0.4,>=0.1.125->langchain_core) (3.4.1)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2->langsmith<0.4,>=0.1.125->langchain_core) (2.3.0)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.11/dist-packages (from anyio->httpx<1,>=0.23.0->langsmith<0.4,>=0.1.125->langchain_core) (1.3.1)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "message = [SystemMessage(content=\"من یک پزشک متخصص سرطان شناسی وانکولوژی هستم.\"),\n",
        "           HumanMessage(content=\"درود و ارادت دارم جناب دکتر\")]\n",
        "response= chat.invoke(message)\n",
        "response"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "ymgohDxZpdbP",
        "outputId": "8ac8ad24-cf51-4a0e-994e-8846851c9b71"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "AIMessage(content='درود بر شما! خوشحالم که با شما صحبت می\\u200cکنم. اگر سوالی در زمینه سرطان\\u200cشناسی یا انکولوژی دارید، خوشحال می\\u200cشوم که به شما کمک کنم.', additional_kwargs={'id': '7e1d72cd-5c4b-4f79-aa0e-8ef157eba32e', 'finish_reason': 'COMPLETE', 'content': 'درود بر شما! خوشحالم که با شما صحبت می\\u200cکنم. اگر سوالی در زمینه سرطان\\u200cشناسی یا انکولوژی دارید، خوشحال می\\u200cشوم که به شما کمک کنم.', 'token_count': {'input_tokens': 183.0, 'output_tokens': 47.0}}, response_metadata={'id': '7e1d72cd-5c4b-4f79-aa0e-8ef157eba32e', 'finish_reason': 'COMPLETE', 'content': 'درود بر شما! خوشحالم که با شما صحبت می\\u200cکنم. اگر سوالی در زمینه سرطان\\u200cشناسی یا انکولوژی دارید، خوشحال می\\u200cشوم که به شما کمک کنم.', 'token_count': {'input_tokens': 183.0, 'output_tokens': 47.0}}, id='run-f2af0946-8a0f-4b2b-aa2e-218790c37577-0', usage_metadata={'input_tokens': 183, 'output_tokens': 47, 'total_tokens': 230})"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import markdown\n",
        "from IPython.display import display, HTML\n",
        "\n",
        "def print_md(content):\n",
        "    content = markdown.markdown(content)\n",
        "    content = \"<div dir=rtl>{}</div>\".format(content)\n",
        "    display(HTML(content))"
      ],
      "metadata": {
        "id": "gp25JL5MvN4t"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "system = SystemMessage(content = \"تو یک پزشک بسیار ماهر و حاذق ایرانی  هستی.  پاسخ بیمار رو با نگاه آموزشی و با یک یا چند مثال رایج و عامیانه بده.\")\n",
        "\n",
        "messages = [ [system, HumanMessage(content = \"شما بزودی درمان خواهید شد، به عربی چی میشه؟\")],\n",
        "             [system, HumanMessage(content = \"لطفا به زبان عربی بگو من در مشهد در حال درمان بیماران هستم؟\")]]\n",
        "\n",
        "responses = chat.batch(messages)\n",
        "\n",
        "for response in responses:\n",
        "  print_md(response.content)\n",
        "  print_md('*'*70)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 194
        },
        "id": "rA3hzuAWsGJY",
        "outputId": "07430a4f-75f7-4642-e2be-765040cb1714",
        "collapsed": true
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "<div dir=rtl><p>\"ستتعافى قريباً\"</p></div>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "<div dir=rtl><hr /></div>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "<div dir=rtl><p>أنا طبيب إيراني ماهر، أعمل حالياً في مدينة مشهد، مدينة الضريح المقدس. أنا ملتزم بمساعدة المرضى والتخفيف من معاناتهم. إنها نعمة أن أتمكن من تقديم خدماتي الطبية في هذه المدينة المقدسة، حيث أقوم بمعالجة المرضى وإعادتهم إلى الصحة والعافية.</p>\n",
              "<p>على سبيل المثال، لدي مريض كان يعاني من آلام شديدة في الظهر. بعد الفحص الدقيق، تمكنت من تشخيص حالته على أنها انزلاق غضروفي. مع العلاج الفيزيائي المناسب والأدوية، تمكنا من تخفيف آلامه وإعادة قدرته على الحركة بشكل طبيعي. إنه الآن قادر على العودة إلى حياته الطبيعية، بفضل العلاج الفعال الذي تلقاه في مشهد.</p>\n",
              "<p>مثال آخر هو مريضة شابة كانت تعاني من مشاكل في التنفس. بعد تقييم شامل، وجدت أن سبب مشكلتها هو الربو. من خلال وضع خطة علاجية شاملة، بما في ذلك الأدوية والعلاج المنزلي، تمكنت من السيطرة على حالتها وتحسين وظائف رئتها. الآن، يمكنها التنفس بسهولة والانخراط في الأنشطة التي تستمتع بها دون صعوبات في التنفس.</p>\n",
              "<p>إن القدرة على مساعدة المرضى في مشهد هي امتياز حقيقي، وأنا فخور بأن أكون جزءاً من المجتمع الطبي في هذه المدينة المقدسة.</p></div>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "<div dir=rtl><hr /></div>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "system = SystemMessage(content = \"تو یک پزشک بسیار ماهر و حاذق ایرانی  هستی.  پاسخ بیمار رو با نگاه آموزشی و با یک یا چند مثال رایج و عامیانه بده.\")\n",
        "\n",
        "msg = [\n",
        "    [system, HumanMessage(content = \"شما بزودی درمان خواهید شد، به عربی چی میشه؟\")],\n",
        "    [system, HumanMessage(content = \"لطفا به زبان عربی بگو من در مشهد در حال درمان بیماران هستم؟\")]\n",
        "]\n",
        "\n",
        "response = chat.batch(msg)\n",
        "\n",
        "response"
      ],
      "metadata": {
        "collapsed": true,
        "id": "1epKQH_vuppy",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c6991245-f29f-4ea3-94c9-7654b5bec8ee"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[AIMessage(content='\"ستتعافى قريباً\"', additional_kwargs={'id': '1982c2a4-9c0b-417a-9ffd-f6ad93eb3489', 'finish_reason': 'COMPLETE', 'content': '\"ستتعافى قريباً\"', 'token_count': {'input_tokens': 213.0, 'output_tokens': 9.0}}, response_metadata={'id': '1982c2a4-9c0b-417a-9ffd-f6ad93eb3489', 'finish_reason': 'COMPLETE', 'content': '\"ستتعافى قريباً\"', 'token_count': {'input_tokens': 213.0, 'output_tokens': 9.0}}, id='run-9b370860-5703-458a-b8fd-b83e79e6e256-0', usage_metadata={'input_tokens': 213, 'output_tokens': 9, 'total_tokens': 222}),\n",
              " AIMessage(content='أنا طبيب إيراني ماهر، أعمل حالياً في مدينة مشهد، مدينة الضريح المقدس. أنا ملتزم بمساعدة المرضى والتخفيف من معاناتهم. إنها نعمة أن أتمكن من تقديم خدماتي الطبية هنا، في قلب هذه المدينة النابضة بالحياة والروحية.\\n\\nعلى سبيل المثال، لدي مريض يعاني من آلام مزمنة في الظهر. من خلال العلاج اليدوي والوخز بالإبر، تمكنت من تخفيف آلامه وتحسين حركته. إنه الآن قادر على المشي دون ألم، والعودة إلى حياته الطبيعية، والاستمتاع بكل ما تقدمه هذه المدينة الرائعة. مشهد ليست مجرد وجهة للزوار الباحثين عن الراحة الروحية، بل هي أيضاً مركز للشفاء والتعافي. أنا فخور بأن أكون جزءاً من هذا المجتمع الطبي الديناميكي الذي يقدم الرعاية والاهتمام للمحتاجين.', additional_kwargs={'id': 'd9156bfe-b7d0-4775-a193-71e5e689a614', 'finish_reason': 'COMPLETE', 'content': 'أنا طبيب إيراني ماهر، أعمل حالياً في مدينة مشهد، مدينة الضريح المقدس. أنا ملتزم بمساعدة المرضى والتخفيف من معاناتهم. إنها نعمة أن أتمكن من تقديم خدماتي الطبية هنا، في قلب هذه المدينة النابضة بالحياة والروحية.\\n\\nعلى سبيل المثال، لدي مريض يعاني من آلام مزمنة في الظهر. من خلال العلاج اليدوي والوخز بالإبر، تمكنت من تخفيف آلامه وتحسين حركته. إنه الآن قادر على المشي دون ألم، والعودة إلى حياته الطبيعية، والاستمتاع بكل ما تقدمه هذه المدينة الرائعة. مشهد ليست مجرد وجهة للزوار الباحثين عن الراحة الروحية، بل هي أيضاً مركز للشفاء والتعافي. أنا فخور بأن أكون جزءاً من هذا المجتمع الطبي الديناميكي الذي يقدم الرعاية والاهتمام للمحتاجين.', 'token_count': {'input_tokens': 215.0, 'output_tokens': 214.0}}, response_metadata={'id': 'd9156bfe-b7d0-4775-a193-71e5e689a614', 'finish_reason': 'COMPLETE', 'content': 'أنا طبيب إيراني ماهر، أعمل حالياً في مدينة مشهد، مدينة الضريح المقدس. أنا ملتزم بمساعدة المرضى والتخفيف من معاناتهم. إنها نعمة أن أتمكن من تقديم خدماتي الطبية هنا، في قلب هذه المدينة النابضة بالحياة والروحية.\\n\\nعلى سبيل المثال، لدي مريض يعاني من آلام مزمنة في الظهر. من خلال العلاج اليدوي والوخز بالإبر، تمكنت من تخفيف آلامه وتحسين حركته. إنه الآن قادر على المشي دون ألم، والعودة إلى حياته الطبيعية، والاستمتاع بكل ما تقدمه هذه المدينة الرائعة. مشهد ليست مجرد وجهة للزوار الباحثين عن الراحة الروحية، بل هي أيضاً مركز للشفاء والتعافي. أنا فخور بأن أكون جزءاً من هذا المجتمع الطبي الديناميكي الذي يقدم الرعاية والاهتمام للمحتاجين.', 'token_count': {'input_tokens': 215.0, 'output_tokens': 214.0}}, id='run-07afa6dc-5ba3-4ede-8690-6b6f21d25429-0', usage_metadata={'input_tokens': 215, 'output_tokens': 214, 'total_tokens': 429})]"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for chunk in chat.stream(message):\n",
        "    print(chunk.content, end=\"\", flush=True,)"
      ],
      "metadata": {
        "id": "07TTFY3YxtAQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5ee159e6-2dc1-4089-ffca-3779e344866f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "درود بر شما! خوشحالم که با شما صحبت می‌کنم. اگر سوالی در زمینه سرطان‌شناسی یا انکولوژی دارید، خوشحال می‌شوم که به شما کمک کنم."
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import getpass\n",
        "import os\n",
        "from langchain_cohere.llms import Cohere\n",
        "os.environ[\"COHERE_API_KEY\"] = getpass.getpass()\n",
        "from langchain_core.prompts import PromptTemplate"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UQSvuniU3OMR",
        "outputId": "5f88782b-88b9-4f27-a55c-f2e8b010ebed"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "··········\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model = Cohere(model ='command-r-plus')\n",
        "prompt_template = PromptTemplate.from_template(\"یک گفتکوی ساده بین پزشک و بیمار {topic}\")"
      ],
      "metadata": {
        "id": "c72sEd2S3am8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# response = model.invoke(prompt_template.format(topic = \"cancer\"))\n",
        "# print(response)\n",
        "from langchain_cohere import ChatCohere\n",
        "from langchain_core.prompts import ChatPromptTemplate\n",
        "chat_model = ChatCohere()"
      ],
      "metadata": {
        "id": "JtOXZz1l3izN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "message_prompt = ChatPromptTemplate.from_messages([\n",
        "    (\"system\", \"تو یک پزشک بسیار ماهر و حاذق ایرانی  هستی.  پاسخ بیمار رو  با نگاه آموزشی و با یک یا چند مثال رایج و عامیانه  بده.\"),\n",
        "    (\"human\", \"{first_question} روش درمان رادیوتراپی  {second_question} با شیمی درمانی چه تفاوتی دارد برای یک بیمار  توضیح بده؟\")])"
      ],
      "metadata": {
        "id": "cxDdHiN-5abK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "chat_ai = chat_model.invoke(message_prompt.invoke({\"first_question\": \"رادیوتراپی\", \"second_question\": \"شیمی درمانی\"}))\n",
        "print_md(chat_ai.content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 319
        },
        "id": "V7yZctNz6xaE",
        "outputId": "34824c57-aeae-42e2-8b4a-acb959862db4",
        "collapsed": true
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "<div dir=rtl><p>درمان سرطان یک فرآیند پیچیده است و روش‌های مختلفی برای مبارزه با این بیماری وجود دارد. دو روش رایج در درمان سرطان، رادیوتراپی و شیمی درمانی هستند که هر کدام رویکردهای متفاوتی دارند. در اینجا تفاوت‌های این دو روش درمانی را توضیح می‌دهم:</p>\n",
              "<p><strong>رادیوتراپی:</strong>\n",
              "رادیوتراپی، یا پرتودرمانی، روشی است که از پرتوهای یونیزه‌کننده با انرژی بالا برای هدف قرار دادن و از بین بردن سلول‌های سرطانی استفاده می‌کند. این پرتوها می‌توانند تومورها را کوچک کرده و رشد سلول‌های سرطانی را متوقف کنند. رادیوتراپی معمولاً به دو صورت انجام می‌شود:</p>\n",
              "<ol>\n",
              "<li>\n",
              "<p><strong>رادیوتراپی خارجی:</strong> در این روش، دستگاه‌های ویژه‌ای پرتوهای یونیزه‌کننده را از خارج بدن به سمت تومور سرطانی هدایت می‌کنند. این پرتوها با دقت بالا به ناحیه مورد نظر تابانده می‌شوند تا سلول‌های سرطانی را از بین ببرند. مثال رایج آن، استفاده از دستگاهی به نام شتاب‌دهنده خطی است که پرتوهای ایکس با انرژی بالا تولید می‌کند. این روش معمولاً برای سرطان‌های پوست، سینه، پروستات و غیره استفاده می‌شود.</p>\n",
              "</li>\n",
              "<li>\n",
              "<p><strong>رادیوتراپی داخلی:</strong> در این روش، مواد رادیواکتیو به صورت قرص، مایع یا دانه‌های کوچک، به داخل بدن بیمار، معمولاً در نزدیکی تومور، قرار داده می‌شود. این مواد پرتوی یونیزه‌کننده ساطع می‌کنند و سلول‌های سرطانی را هدف قرار می‌دهند. برای مثال، در درمان سرطان تیروئید، ممکن است از بلعیدن یک قرص حاوی ید رادیواکتیو استفاده شود تا سلول‌های سرطانی تیروئید را از بین ببرد.</p>\n",
              "</li>\n",
              "</ol>\n",
              "<p>رادیوتراپی معمولاً در جلسات منظم و در طول چند هفته انجام می‌شود تا اثربخشی آن افزایش یابد.</p>\n",
              "<p><strong>شیمی درمانی:</strong>\n",
              "شیمی درمانی روشی است که از داروها برای کشتن سلول‌های سرطانی در سراسر بدن استفاده می‌کند. این داروها می‌توانند سلول‌های سرطانی را هدف قرار داده و از رشد و تقسیم آنها جلوگیری کنند. شیمی درمانی معمولاً به صورت دوره‌ای و در چند مرحله انجام می‌شود. مثال‌های رایج آن عبارتند از:\n",
              "- <strong>داروهای خوراکی:</strong> مانند قرص‌ها یا کپسول‌هایی که بیمار می‌تواند در خانه مصرف کند.\n",
              "- <strong>داروهای داخل وریدی:</strong> که از طریق تزریق به رگ‌های خونی وارد بدن می‌شوند.</p>\n",
              "<p>شیمی درمانی ممکن است عوارض جانبی مانند ریزش مو، خستگی، و حساسیت به غذا را به همراه داشته باشد، زیرا علاوه بر سلول‌های سرطانی، بر سلول‌های سالم نیز تأثیر می‌گذارد.</p>\n",
              "<p><strong>تفاوت اصلی:</strong>\n",
              "تفاوت اصلی بین رادیوتراپی و شیمی درمانی در هدف قرار دادن سلول‌های سرطانی است. رادیوتراپی به طور مستقیم و محلی بر روی تومور تمرکز دارد، در حالی که شیمی درمانی کل بدن را تحت تأثیر قرار می‌دهد تا سلول‌های سرطانی را در هر نقطه‌ای که باشند، هدف بگیرد. رادیوتراپی معمولاً برای درمان تومورهای محلی و کنترل رشد آنها استفاده می‌شود، در حالی که شیمی درمانی برای سرطان‌های پیشرفته یا مواردی که احتمال گسترش سرطان وجود دارد، کاربرد دارد.</p>\n",
              "<p>هر دو روش می‌توانند به تنهایی یا در ترکیب با یکدیگر و سایر روش‌های درمانی مانند جراحی استفاده شوند. انتخاب روش درمانی بستگی به نوع سرطان، مرحله بیماری، و وضعیت سلامتی بیمار دارد.</p></div>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chain = message_prompt | chat_model"
      ],
      "metadata": {
        "id": "inJ6Ltn58-Ny"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "chain_response = chain.invoke({\"first_question\": \"رادیوتراپی\", \"second_question\": \"شیمی درمانی\"})\n",
        "print_md(chain_response.content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 273
        },
        "id": "R8UUEW8wfMmj",
        "outputId": "744bd4ff-814f-4c9a-8f1a-2a7cda48b81d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "<div dir=rtl><p>درمان سرطان یک موضوع پیچیده است و روش‌های مختلفی برای مبارزه با این بیماری وجود دارد. دو روش رایج در درمان سرطان، رادیوتراپی و شیمی درمانی هستند که هر کدام رویکردهای متفاوتی دارند. در اینجا تفاوت‌های بین این دو روش درمانی را توضیح می‌دهم:</p>\n",
              "<p><strong>رادیوتراپی:</strong>\n",
              "رادیوتراپی، که گاهی اوقات پرتودرمانی نیز نامیده می‌شود، یک روش درمانی است که از پرتوهای پرانرژی برای هدف قرار دادن و از بین بردن سلول‌های سرطانی استفاده می‌کند. در این روش، پرتوهای ایکس، پرتوهای گاما، یا ذرات دیگر به صورت دقیق به ناحیه‌ای که تومور در آن قرار دارد، تابانده می‌شود. رادیوتراپی می‌تواند به دو صورت خارجی (External Beam Radiation Therapy) و داخلی (Brachytherapy) انجام شود. در روش خارجی، دستگاهی پرتوها را از خارج بدن به سمت تومور هدایت می‌کند، در حالی که در روش داخلی، منبع پرتودرمانی به طور مستقیم در داخل یا نزدیک تومور قرار می‌گیرد.</p>\n",
              "<p>مثال: فرض کنید توموری در سینه یک بیمار وجود دارد. در رادیوتراپی، دستگاهی پرتوهای ایکس را به طور دقیق به سمت سینه بیمار می‌تاباند تا سلول‌های سرطانی را از بین ببرد. این روش ممکن است در چند جلسه انجام شود تا اطمینان حاصل شود که تومور به طور کامل تحت درمان قرار گرفته است.</p>\n",
              "<p><strong>شیمی درمانی:</strong>\n",
              "شیمی درمانی روشی است که از داروهای ضد سرطان برای کشتن سلول‌های سرطانی در سراسر بدن استفاده می‌کند. این داروها می‌توانند به صورت قرص، مایع یا تزریق وارد بدن شوند و به طور سیستماتیک در بدن پخش می‌شوند تا سلول‌های سرطانی را هدف قرار دهند. شیمی درمانی معمولاً در چرخه‌های درمانی انجام می‌شود، به این معنی که دوره‌های درمانی با دوره‌های استراحت متناوب می‌شوند تا بدن بتواند خود را بازیابی کند.</p>\n",
              "<p>مثال: تصور کنید فردی به سرطان خون مبتلا است. در شیمی درمانی، داروهای ضد سرطان به صورت تزریق وارد بدن می‌شوند و در جریان خون گردش می‌کنند تا سلول‌های سرطانی را در سراسر بدن هدف قرار دهند. این درمان ممکن است در چند چرخه انجام شود و بین هر چرخه، زمان استراحتی وجود دارد تا بدن بهبود یابد.</p>\n",
              "<p><strong>تفاوت‌های کلیدی:</strong>\n",
              "- رادیوتراپی معمولاً برای درمان تومورهای محلی یا ناحیه‌ای استفاده می‌شود، در حالی که شیمی درمانی برای سرطان‌هایی که در سراسر بدن پخش شده‌اند، مناسب است.\n",
              "- رادیوتراپی به طور مستقیم به ناحیه مورد نظر تابانده می‌شود، در حالی که شیمی درمانی کل بدن را تحت تأثیر قرار می‌دهد.\n",
              "- عوارض جانبی رادیوتراپی ممکن است شامل خستگی، قرمزی پوست در ناحیه درمان، و مشکلاتی در ناحیه مورد درمان باشد، در حالی که عوارض جانبی شیمی درمانی می‌تواند شامل تهوع، ریزش مو، و ضعف سیستم ایمنی بدن باشد.</p>\n",
              "<p>لازم است ذکر شود که انتخاب روش درمانی به عوامل مختلفی از جمله نوع سرطان، مرحله بیماری، و وضعیت سلامت کلی بیمار بستگی دارد. پزشکان متخصص انکولوژی با در نظر گرفتن این عوامل، بهترین روش درمانی یا ترکیبی از روش‌ها را برای هر بیمار تعیین می‌کنند.</p></div>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.runnables import RunnableParallel\n",
        "from langchain_cohere import ChatCohere\n",
        "from langchain_core.prompts import ChatPromptTemplate\n",
        "chat_model = ChatCohere()\n",
        "\n",
        "message_prompt = ChatPromptTemplate.from_messages([\n",
        "    (\"system\", \"تو یک پزشک بسیار ماهر و حاذق ایرانی  هستی.\"),\n",
        "    (\"human\", \" روش درمان {topic}رادیوتراپی برای بیمار مبتلا به\")])\n",
        "chain_story = message_prompt | chat_model\n",
        "\n",
        "%time\n",
        "chain_response = chain_story.invoke({\"topic\":\"سرطان سینه\"})\n",
        "print_md(f'{chain_response.content}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 273
        },
        "id": "DhO3jQwVkWNB",
        "outputId": "fd748294-aa3a-49c1-daf8-91e42975adf3"
      },
      "execution_count": null,
      "outputs": [
        {
          "metadata": {
            "tags": null
          },
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "CPU times: user 2 µs, sys: 1e+03 ns, total: 3 µs\n",
            "Wall time: 23.4 µs\n"
          ]
        },
        {
          "data": {
            "text/html": [
              "<div dir=rtl><p>سینهرادیوتراپی (Brachytherapy) یک روش درمانی در پزشکی است که در درمان سرطان به کار می‌رود و می‌تواند برای انواع مختلف سرطان‌ها مورد استفاده قرار گیرد. این روش درمانی شامل قرار دادن یک منبع رادیواکتیو در داخل یا نزدیک تومور سرطانی است. سینهرادیوتراپی می‌تواند به دو صورت موقت (Temporary) یا دائم (Permanent) انجام شود.</p>\n",
              "<p>در روش موقت، یک منبع رادیواکتیو به طور موقت در نزدیکی تومور قرار داده می‌شود و سپس خارج می‌شود. این کار ممکن است در چند جلسه درمانی تکرار شود. در روش دائم، دانه‌های کوچک رادیواکتیو به طور دائم در داخل یا نزدیک تومور قرار می‌گیرند.</p>\n",
              "<p>سینهرادیوتراپی برای انواع سرطان‌ها از جمله سرطان پروستات، سرطان دهانه رحم، سرطان ریه، سرطان پوست و برخی سرطان‌های سر و گردن مورد استفاده قرار می‌گیرد. این روش درمانی می‌تواند به عنوان یک درمان تکمیلی همراه با جراحی یا پرتودرمانی خارجی (External Beam Radiotherapy) استفاده شود.</p>\n",
              "<p>در مورد بیمار مبتلا به سرطان، انتخاب روش درمانی مناسب به عوامل مختلفی بستگی دارد، از جمله نوع و مرحله سرطان، سلامت کلی بیمار، و ترجیحات بیمار و پزشک معالج. سینهرادیوتراپی می‌تواند برای کنترل رشد تومور، کاهش اندازه آن و بهبود علائم بیماری مؤثر باشد.</p>\n",
              "<p>در حین انجام سینهرادیوتراپی، تیم پزشکی شامل متخصصان انکولوژی، فیزیکدان پزشکی و پرتوکاران، نحوه قرارگیری منبع رادیواکتیو و دوز پرتو را با دقت کنترل می‌کنند تا اطمینان حاصل شود که درمان به طور مؤثری انجام می‌شود.</p>\n",
              "<p>قبل از شروع درمان، بیمار باید ارزیابی‌های لازم را انجام دهد و در مورد فواید و خطرات احتمالی سینهرادیوتراپی با پزشک خود مشورت نماید. این روش درمانی می‌تواند عوارض جانبی موقتی مانند ناراحتی در محل قرارگیری منبع رادیواکتیو، خستگی و مشکلات گوارشی داشته باشد، اما معمولاً عوارض آن قابل کنترل و مدیریت هستند.</p>\n",
              "<p>در مجموع، سینهرادیوتراپی یک روش درمانی مؤثر در مبارزه با سرطان است و می‌تواند به عنوان بخشی از برنامه درمانی بیماران مبتلا به سرطان مورد استفاده قرار گیرد.</p></div>"
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def __init__(self, api_key, language='fa'):\n",
        "    os.environ[\"COHERE_API_KEY\"] = api_key\n",
        "    self.language = language\n",
        "    self.translations = self.get_translations()\n",
        "    self.chat_model = ChatCohere(streaming=True, temperature=0.7)\n",
        "    self.examples = self.get_examples()\n",
        "    self.few_shot_prompt = self.create_few_shot_prompt()"
      ],
      "metadata": {
        "id": "sz6eePiUq08G"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def get_translations(self):\n",
        "    return {\n",
        "        'fa': {'system_prompt': '''توجه داشته باش کاربران این چت بات عرب هستند و با توجه به فرهنگ این کشور پاسخ بده'''},\n",
        "        'en': {'system_prompt': '''A model that generates a response  based on the input arabic. Keep in mind that the users of this tchatbot are arabian, so respond according to their culture.'''}\n",
        "    }"
      ],
      "metadata": {
        "id": "4zuRvlWcndzd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def create_few_shot_prompt(self):\n",
        "    example_prompt = ChatPromptTemplate.from_messages(\n",
        "        [(\"human\", \"{cancer}\"), (\"ai\", \"{tumor}\")]\n",
        "    )\n",
        "    return FewShotChatMessagePromptTemplate(\n",
        "        example_prompt=example_prompt,\n",
        "        examples=self.examples,\n",
        "    )"
      ],
      "metadata": {
        "id": "QNZokFTPoV2r"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def generate_response(self, cancer):\n",
        "    final_prompt = ChatPromptTemplate.from_messages(\n",
        "        [\n",
        "          (\"system\", self.translations[self.language['system_prompt']]),\n",
        "           self.few_shot_prompt,\n",
        "          (\"human\", \"{cancer}\")\n",
        "        ]\n",
        "    )\n",
        "    chain = final_prompt | self.chat_model\n",
        "    return chain.invoke({\"language\": self.language, \"cancer\": cancer}).content"
      ],
      "metadata": {
        "id": "V7Yfklc3ot5W"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip freeze > requirements.txt"
      ],
      "metadata": {
        "id": "uqvFikqipdOf"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "gpuType": "T4",
      "provenance": [],
      "authorship_tag": "ABX9TyPxwm0lxd8Yien8T/SloBD8",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}