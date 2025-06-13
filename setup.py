from setuptools import setup, find_packages

setup(
    name="strategic_debate_tot",
    version="0.1",
    description="Tree of Thought debate strategies using LLMs",
    packages=find_packages(),
    install_requires=[
        "litellm",
        "dspy-ai",
        "pydantic",
        "numpy",
        "tqdm",
        "networkx",
        "matplotlib",
        "datasets"
    ],
    python_requires=">=3.8",
)
