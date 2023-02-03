# Afrilearn-AI-Learning-Personalisation
<p align="center">
    <a href="https://github.com/UNICEF-AFRILEARN/unicef_afrilearn/blob/main/LICENSE.md">
        <img alt="GitHub" src="https://img.shields.io/github/license/UNICEF-AFRILEARN/unicef_afrilearn?logo=GitHub&style=plastic">
    </a>
    <a href="https://bookbot-kids.github.io/g2p_id/">
        <img alt="Documentation" src="https://img.shields.io/website/http/bookbot-kids.github.io/g2p_id.svg?down_color=red&down_message=offline&up_message=online">
    </a>
    <a href="https://github.com/bookbot-kids/g2p_id/releases">
        <img alt="GitHub release" src="https://img.shields.io/github/release/bookbot-kids/g2p_id.svg">
    </a>
    <a href="https://github.com/bookbot-kids/g2p_id/blob/main/CODE_OF_CONDUCT.md">
        <img alt="Contributor Covenant" src="https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg">
    </a>
    <a href="https://github.com/bookbot-kids/g2p_id/actions/workflows/tests.yml">
        <img alt="Tests" src="https://github.com/bookbot-kids/g2p_id/actions/workflows/tests.yml/badge.svg">
    </a>
    <a href="https://codecov.io/gh/bookbot-kids/g2p_id">
        <img alt="Code Coverage" src="https://img.shields.io/codecov/c/github/bookbot-kids/g2p_id">
    </a>
    <a href="https://discord.gg/gqwTPyPxa6">
        <img alt="chat on Discord" src="https://img.shields.io/discord/1001447685645148169?logo=discord">
    </a>
    <a href="https://github.com/bookbot-kids/g2p_id/blob/main/CONTRIBUTING.md">
        <img alt="contributing guidelines" src="https://img.shields.io/badge/contributing-guidelines-brightgreen">
    </a>
</p>

This library is developed to convert Indonesian (Bahasa Indonesia) graphemes (words) to phonemes in IPA. We followed the methods and designs used in the English equivalent library, [g2p](https://github.com/Kyubyong/g2p).

## Installation

```bash
pip install g2p_id_py
```

## How to Use

```py
from g2p_id import G2p

texts = [
    "Apel itu berwarna merah.",
    "Rahel bersekolah di S M A Jakarta 17.",
    "Mereka sedang bermain bola di lapangan.",
]

g2p = G2p()
for text in texts:
    print(g2p(text))

>> [['a', 'p', 'ə', 'l'], ['i', 't', 'u'], ['b', 'ə', 'r', 'w', 'a', 'r', 'n', 'a'], ['m', 'e', 'r', 'a', 'h'], ['.']]
>> [['r', 'a', 'h', 'e', 'l'], ['b', 'ə', 'r', 's', 'ə', 'k', 'o', 'l', 'a', 'h'], ['d', 'i'], ['e', 's'], ['e', 'm'], ['a'], ['dʒ', 'a', 'k', 'a', 'r', 't', 'a'], ['t', 'u', 'dʒ', 'u', 'h'], ['b', 'ə', 'l', 'a', 's'], ['.']]
>> [['m', 'ə', 'r', 'e', 'k', 'a'], ['s', 'ə', 'd', 'a', 'ŋ'], ['b', 'ə', 'r', 'm', 'a', 'i', 'n'], ['b', 'o', 'l', 'a'], ['d', 'i'], ['l', 'a', 'p', 'a', 'ŋ', 'a', 'n'], ['.']]
```

## Algorithm

This is heavily inspired from the English [g2p](https://github.com/Kyubyong/g2p).

1. Spells out arabic numbers and some currency symbols, e.g. `Rp 200,000 -> dua ratus ribu rupiah`. This is borrowed from [Cahya's code](https://github.com/cahya-wirawan/text_processor).
2. Attempts to retrieve the correct pronunciation for homographs based on their [POS (part-of-speech) tags](#pos-tagging).
3. Looks up a lexicon (pronunciation dictionary) for non-homographs. This list is originally from [ipa-dict](https://github.com/open-dict-data/ipa-dict/blob/master/data/ma.txt), and we later made a modified version.
4. For OOVs, we predict their pronunciations using either a [BERT model](https://huggingface.co/bookbot/id-g2p-bert) or an [LSTM model](https://huggingface.co/bookbot/id-g2p-lstm).

## Phoneme and Grapheme Sets

```python
graphemes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
phonemes = ['a', 'b', 'd', 'e', 'f', 'ɡ', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'z', 'ŋ', 'ə', 'ɲ', 'tʃ', 'ʃ', 'dʒ', 'x', 'ʔ']
```

## Implementation Details

You can find more details on how we handled homographs and out-of-vocabulary prediction on our [documentation](https://bookbot-kids.github.io/g2p_id/algorithm/) page.

## References

```bib
@misc{g2pE2019,
  author = {Park, Kyubyong & Kim, Jongseok},
  title = {g2pE},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Kyubyong/g2p}}
}
```

```bib
@misc{TextProcessor2021,
  author = {Cahya Wirawan},
  title = {Text Processor},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/cahya-wirawan/text_processor}}
}
```

## Contributors

<a href="https://github.com/bookbot-kids/g2p_id/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=bookbot-kids/g2p_id" />
</a>




# UNICEF-AI-Personalisation
Some children learn best by watching videos, some by reading class notes, some by solving practice problems, and some by social collaboration. Beyond blending storytelling, social learning, and supplementary tech skills content, Afrilearn leverages artificial intelligence to give every child access to personalized learning using the unique method that works best for them. This can be solved using AI recommendation systems. The recommender system provides course recommendations based on user history and similar profiles.

This repo is deployed as a web app and api through Heroku [here](https://unicef-afrilearn-app.herokuapp.com/).

## Afrilearn Project Charter

## Community Statement

The educational landscape in Africa is in a coma with the high rate of out-ofschool children, over 50 percent failure in examinations and high cost of access to quality education. We created the Afrilearn platform for young people across Africa to access world-class education and excel by leveraging technology without the need to step foot into the four walls of a school. Our community is a crucible of expertise and collaboration amongst developers, tutors, animators, students and machine learning experts to ensure each student get the exact support, peculiar to their needs.

## Vision statement 

Become Africa’s most loved e-learning brand delivering affordable and worldclass education to 300 million young people Africans, anywhere

## Mission statement

We are committed to providing personalised affordable yet world-class education to Africans, anywhere.


## Installation
Clone this repository. Navigate to the repository and create a python virtual environment through your method of choosing. Activate the environment and install the required libraries through
```
git clone https://github.com/Afrilearn/UNICEF-AI-Personalisation.git
cd UNICEF-AI-Personalisation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Architecture
app.py --> templates/index.html --> recommender.py --> templates/results.html
- app.py opens the user interface for collecting student course levels, subjects and lessons.
- index.html is the user interface for collecting student course levels, subjects and lessons used in calling the machine learning recommender system.
- recommender.py loads pickle files containing the recommender system apriori rules and applies this in recommending similar lessons for students based on the student course levels, subjects and lessons.
- results.html displays the dataframe results in html.
- To use this app as an API, a POST reuquest can be sent directly to https://unicef-afrilearn-app.herokuapp.com/recommend with a json file containing student details for the school_level, subject and lesson.

## Dependencies
The backend is developed in python 3.x.x. Other libraries and packages, along with their versions, are included in [requirements.txt]('../../requirements.txt'). In short, you need the following libraries and their dependencies.
- pandas
- numpy
- flask_cors
- flask
- mlxtend

## Usage
<a href="https://unicef-afrilearn-app.herokuapp.com/">visit web app</a>
