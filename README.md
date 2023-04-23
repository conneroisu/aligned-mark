# Introduction
An opensourced chat/completions/inferencing/generations markup Language based on markdown striving to provide an open-souce alternative to  Chat Markup Language (ChatML) is a **syntax being developed by OpenAI**. ChatGPT uses currently the version v0 of ChatML. Essentially, ChatML allows for the structuring of chat-based conversations with an AI model, like ChatGPT, in a more intuitive and human-readable format. Inspired by this idea, we aim to create an open-source alternative that helps users better control their conversation flow and presentation. ChatML markup has a few resources: [Some examples of ChatML Sytax](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/chatgpt?pivots=programming-language-chat-ml), 
Because this repository is aimed to promote progress, it provides each given training file with two syntaxes: a aligned-markup syntax and ChatML syntax.



Our open-sourced language will have features similar to ChatML such as:

1. Support for turns: Users can easily define alternating user and assistant inputs within their document.
2. Clear dialogue structure: Use indentation or other formatting options to maintain a visually appealing representation of the conversation.
3. Inline instructions: Provide context or guidance for the AI's responses directly within the document without cluttering up the user messages.
4. Role assignment: Specify which role (user or assistant) is responsible for a particular message in order to generate appropriate replies from your AI model.

We believe that our approach will make it even more seamless when engaging with models like ChatGPT while also allowing developers and researchers greater flexibility in designing interactive conversations between humans and machines.

As this project is community-driven, we encourage contributions from anyone interested in improving this language further!

The basic idea behind ChatML is ensure the LLM model inputs are sent in structured format following ChatML and not as unstructured text.
An **alignment solution** for language models requiring language models/generational models to store information inside of a vault(folder) of markdown files allowing for analysis of alignment standards. This repository hopes also to offer a python package for inference of models on varius prompts and chains of contexts and windows of those prompts asynchronously. 

One way to address the issue of alignment is by testing and analyzing AI models using various prompts and contexts. This can be done effectively by expressing their inference inside markdown files. Additionally, markdown provides an expandable scoped environment for the gradual increasing of scope needed for affirm model alignment and safety. With many applications built for viewing, editing, and otherwise consuming markdown files, markdown provides an optimal place for athe analysis of generational models.

You can read more about how the idea this respository implements inside of the docs.
# Getting started 


# Contributing

We welcome contributions from anyone interested in advancing the field of AGI research! If you have an idea for an experiment or would like to improve upon existing ones:



## Citation 
```
@misc(aligned-mark,
	title={Aligned Mark:Aligning Models with Markdown},
	author:{Conner Ohnesorge},
	journal={arXiv},
	year={2023}
```


## Citations
Nori, Harsha, et al. "Accuracy, Interpretability, and Differential Privacy via Explainable Boosting." _ArXiv_, 2021, /abs/2106.09680. Accessed 12 Apr. 2023.


```
@misc{selfinstruct,
  title={Self-Instruct: Aligning Language Model with Self Generated Instructions},
  author={Wang, Yizhong and Kordi, Yeganeh and Mishra, Swaroop and Liu, Alisa and Smith, Noah A. and Khashabi, Daniel and Hajishirzi, Hannaneh},
  journal={arXiv preprint arXiv:2212.10560},
  year={2022}
}
```


```
@misc{alpaca,
  author = {Rohan Taori and Ishaan Gulrajani and Tianyi Zhang and Yann Dubois and Xuechen Li and Carlos Guestrin and Percy Liang and Tatsunori B. Hashimoto },
  title = {Stanford Alpaca: An Instruction-following LLaMA model},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/tatsu-lab/stanford_alpaca}},
}
```

```
@software{openchatkit,
  title = {{OpenChatKit: An Open Toolkit and Base Model for Dialogue-style Applications}},
  author = {Together Computer},
  url = {https://github.com/togethercomputer/OpenChatKit}
  month = {3},
  year = {2023},
  version = {0.15},
}
```