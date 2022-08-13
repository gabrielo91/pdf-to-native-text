# pdf-to-native-text

## How to run it

Beforehand you may need to install following dependencies:

```
brew install tesseract
```

and

```
brew install ghostscript
```

Then, please install needed requirements using the following command (you can use a virtual environment to do so):

```
pip install -r requirements.txt
```

Finally, in order to run it:

```
python main.py
```

The input pdf must be named `sample.pdf` and the output will be stored as `output.pdf` and `output.txt`
