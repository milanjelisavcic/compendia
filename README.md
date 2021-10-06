# TEMIS Summarizer
Testing summary AI on Heroku

## Installation

The system use Python Flask as the core framework.
Installation is straightforward.
First, clone the project:

```bash
git clone https://github.com/Temis-AI/temis-core.git
cd temis-core/
```

Within the `temis-core/` root directory create Python virtual environment:

```bash
conda create -n temis python=3.7.10
conda activate temis
conda install -r requirements.txt
```

Finally, run the application:

```bash
flask run
```

To verify the installation, the application home screen is visible on URI https://localhost:5000/
