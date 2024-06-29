# Recommendation system using LLM

A recommendation system using LLM to recommend the best possible candidate for project completion.

## Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution)
- Git

## Getting Started

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/sumenchalla/Recommendation-system
cd your-repo-name
```

### Create and Activate Conda Environment
Make sure you have Anaconda installed and initialized. Then, create and activate a new Conda environment with Python 3.12:

```bash
conda create -n venv python=3.12
```
Activation
```bash
conda activate venv
```
### Install Required Packages
Install the required packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```
### Install PyTorch
Based on your machine configuration, visit the [PyTorch installation page](https://pytorch.org/get-started/locally/) to get the appropriate installation command. Copy the command and run it in your terminal. DONT FORGET TO SET compute platform as CPU if you dont have GPU in your machine

### Configure Hugging Face Token
Go to [Hugging Face](https://huggingface.co/) and create an access token.
Copy the token and create a .env file in the src/components directory:
#### Inside src/components/.env
HUGGING_FACE_TOKEN=your_access_token


### Run the Application
To run the application using Streamlit, execute the following command:

```bash
streamlit run src/app.py
```


