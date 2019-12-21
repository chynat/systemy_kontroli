{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Copy of Untitled5.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/chynat/systemy_kontroli/blob/master/sobota.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Q-Q97Q7C-ga0",
        "colab_type": "code",
        "outputId": "1d0d1f24-7012-4272-e122-b70cef281bce",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        }
      },
      "source": [
        "#TODO: add more code\n",
        "import os\n",
        "import glob\n",
        "from collections import Counter\n",
        "import sys\n",
        "import urllib.request\n",
        "from urllib.request import urlopen\n",
        "from string import ascii_lowercase\n",
        "\n",
        "\n",
        "def print_menu():\n",
        "    \n",
        "    print(\"1. Pobierz plik z internetu \")\n",
        "    print(\"2. Zlicz liczbę liter w pobranym pliku \")\n",
        "    print(\"3. Zlicz liczbę wyrazów w pliku \")\n",
        "    print(\"4. Zlicz liczbę znaków interpunkcyjnych w pliku \")        \n",
        "    print(\"5. Wygeneruj raport o użyciu liter (A-Z) \")\n",
        "    print(\"6. Zapisz statystyki z punktów 2-5 do pliku statystyki.txt \")\n",
        "    print(\"7. Wyjście z programu \")\n",
        "\n",
        "\n",
        "try:\n",
        "      file = open(\"C:\\data.txt\", \"r\")\n",
        "      cont=file.read()\n",
        "      number_of_characters = len(cont)\n",
        "      print('Liczba znaków w tekście:', number_of_characters)\n",
        "\n",
        "      words = data.split(\" \")\n",
        "      number_of_words = len(words)\n",
        "      print('Liczba słów w tekście:',number_of_words)\n",
        "\n",
        "      file = file.replace(\"--\", \" \")\n",
        "      for symbol in \"-'\":\n",
        "          file = file.replace(symbol + \" \", \"\")\n",
        "          file = file.replace(\" \" + symbol, \"\")\n",
        "\n",
        "      for symbol in \".,/'-\":\n",
        "          print (symbol, file.count(symbol))\n",
        "      f.close()\n",
        "except FileNotFoundError:\n",
        "    print('error')\n",
        "    print('Plik nie istnieje')\n",
        "    "
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "error\n",
            "Plik nie istnieje\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8L6LdfbbHctE",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DG55TErn-ZFf",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}