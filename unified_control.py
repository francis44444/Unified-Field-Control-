{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO9cfy3CJxE9m5DH++OF5ku",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/francis44444/Unified-Field-Control-/blob/main/unified_control.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install pennylane"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HhzwTX16zhph",
        "outputId": "d30f4bf3-9fc3-444e-aeee-4cf1f2b580be"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting pennylane\n",
            "  Downloading pennylane-0.45.0-py3-none-any.whl.metadata (10 kB)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.12/dist-packages (from pennylane) (1.16.3)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.12/dist-packages (from pennylane) (3.6.1)\n",
            "Collecting rustworkx>=0.14.0 (from pennylane)\n",
            "  Downloading rustworkx-0.17.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (10 kB)\n",
            "Requirement already satisfied: autograd in /usr/local/lib/python3.12/dist-packages (from pennylane) (1.8.0)\n",
            "Collecting appdirs (from pennylane)\n",
            "  Downloading appdirs-1.4.4-py2.py3-none-any.whl.metadata (9.0 kB)\n",
            "Collecting autoray==0.8.4 (from pennylane)\n",
            "  Downloading autoray-0.8.4-py3-none-any.whl.metadata (6.1 kB)\n",
            "Requirement already satisfied: cachetools in /usr/local/lib/python3.12/dist-packages (from pennylane) (6.2.6)\n",
            "Collecting pennylane-lightning>=0.45 (from pennylane)\n",
            "  Downloading pennylane_lightning-0.45.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (11 kB)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.12/dist-packages (from pennylane) (2.32.4)\n",
            "Requirement already satisfied: tomlkit in /usr/local/lib/python3.12/dist-packages (from pennylane) (0.13.3)\n",
            "Requirement already satisfied: typing_extensions in /usr/local/lib/python3.12/dist-packages (from pennylane) (4.15.0)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.12/dist-packages (from pennylane) (26.2)\n",
            "Collecting diastatic-malt (from pennylane)\n",
            "  Downloading diastatic_malt-2.15.3-py3-none-any.whl.metadata (2.9 kB)\n",
            "Requirement already satisfied: numpy>=2.0 in /usr/local/lib/python3.12/dist-packages (from pennylane) (2.0.2)\n",
            "Requirement already satisfied: gast in /usr/local/lib/python3.12/dist-packages (from pennylane) (0.7.0)\n",
            "Collecting scipy-openblas32>=0.3.26 (from pennylane-lightning>=0.45->pennylane)\n",
            "  Downloading scipy_openblas32-0.3.33.0.0-py3-none-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (57 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m57.3/57.3 kB\u001b[0m \u001b[31m2.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: termcolor in /usr/local/lib/python3.12/dist-packages (from diastatic-malt->pennylane) (3.3.0)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests->pennylane) (3.4.7)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests->pennylane) (3.15)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests->pennylane) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests->pennylane) (2026.5.20)\n",
            "Downloading pennylane-0.45.0-py3-none-any.whl (5.4 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m5.4/5.4 MB\u001b[0m \u001b[31m50.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading autoray-0.8.4-py3-none-any.whl (937 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m937.5/937.5 kB\u001b[0m \u001b[31m37.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pennylane_lightning-0.45.0-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (25.5 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m25.5/25.5 MB\u001b[0m \u001b[31m57.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading rustworkx-0.17.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.2 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m2.2/2.2 MB\u001b[0m \u001b[31m32.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading appdirs-1.4.4-py2.py3-none-any.whl (9.6 kB)\n",
            "Downloading diastatic_malt-2.15.3-py3-none-any.whl (167 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m167.2/167.2 kB\u001b[0m \u001b[31m12.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading scipy_openblas32-0.3.33.0.0-py3-none-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (8.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.8/8.8 MB\u001b[0m \u001b[31m95.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: appdirs, scipy-openblas32, rustworkx, diastatic-malt, autoray, pennylane-lightning, pennylane\n",
            "Successfully installed appdirs-1.4.4 autoray-0.8.4 diastatic-malt-2.15.3 pennylane-0.45.0 pennylane-lightning-0.45.0 rustworkx-0.17.1 scipy-openblas32-0.3.33.0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install pennylane-ionq"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mL4iwpEGz7IZ",
        "outputId": "f768b0f8-2e01-4526-ef46-1544fc36611b"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting pennylane-ionq\n",
            "  Downloading pennylane_ionq-0.45.0-py3-none-any.whl.metadata (7.7 kB)\n",
            "Requirement already satisfied: pennylane>=0.44 in /usr/local/lib/python3.12/dist-packages (from pennylane-ionq) (0.45.0)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.12/dist-packages (from pennylane-ionq) (2.0.2)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.12/dist-packages (from pennylane-ionq) (2.9.0.post0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.12/dist-packages (from pennylane-ionq) (2.32.4)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.12/dist-packages (from pennylane>=0.44->pennylane-ionq) (1.16.3)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.12/dist-packages (from pennylane>=0.44->pennylane-ionq) (3.6.1)\n",
            "Requirement already satisfied: rustworkx>=0.14.0 in /usr/local/lib/python3.12/dist-packages (from pennylane>=0.44->pennylane-ionq) (0.17.1)\n",
            "Requirement already satisfied: autograd in /usr/local/lib/python3.12/dist-packages (from pennylane>=0.44->pennylane-ionq) (1.8.0)\n",
            "Requirement already satisfied: appdirs in /usr/local/lib/python3.12/dist-packages (from pennylane>=0.44->pennylane-ionq) (1.4.4)\n",
            "Requirement already satisfied: autoray==0.8.4 in /usr/local/lib/python3.12/dist-packages (from pennylane>=0.44->pennylane-ionq) (0.8.4)\n",
            "Requirement already satisfied: cachetools in /usr/local/lib/python3.12/dist-packages (from pennylane>=0.44->pennylane-ionq) (6.2.6)\n",
            "Requirement already satisfied: pennylane-lightning>=0.45 in /usr/local/lib/python3.12/dist-packages (from pennylane>=0.44->pennylane-ionq) (0.45.0)\n",
            "Requirement already satisfied: tomlkit in /usr/local/lib/python3.12/dist-packages (from pennylane>=0.44->pennylane-ionq) (0.13.3)\n",
            "Requirement already satisfied: typing_extensions in /usr/local/lib/python3.12/dist-packages (from pennylane>=0.44->pennylane-ionq) (4.15.0)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.12/dist-packages (from pennylane>=0.44->pennylane-ionq) (26.2)\n",
            "Requirement already satisfied: diastatic-malt in /usr/local/lib/python3.12/dist-packages (from pennylane>=0.44->pennylane-ionq) (2.15.3)\n",
            "Requirement already satisfied: gast in /usr/local/lib/python3.12/dist-packages (from pennylane>=0.44->pennylane-ionq) (0.7.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil->pennylane-ionq) (1.17.0)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests->pennylane-ionq) (3.4.7)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests->pennylane-ionq) (3.15)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests->pennylane-ionq) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests->pennylane-ionq) (2026.5.20)\n",
            "Requirement already satisfied: scipy-openblas32>=0.3.26 in /usr/local/lib/python3.12/dist-packages (from pennylane-lightning>=0.45->pennylane>=0.44->pennylane-ionq) (0.3.33.0.0)\n",
            "Requirement already satisfied: termcolor in /usr/local/lib/python3.12/dist-packages (from diastatic-malt->pennylane>=0.44->pennylane-ionq) (3.3.0)\n",
            "Downloading pennylane_ionq-0.45.0-py3-none-any.whl (26 kB)\n",
            "Installing collected packages: pennylane-ionq\n",
            "Successfully installed pennylane-ionq-0.45.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "PRgs8tAm1Oei"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}