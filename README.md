# What Is It?

This is a python script that builds custom mp3 files containing random arithmetic equations. You specify how
many equations you want, parameters for the operands, the operator and the answer (i.e. decimals to round to), as well as
the pause length between the question and the answer and between equations themselves, and you get an mp3 file that satisfies those parameters.

Why? Because I suck at arithmetic and I'm too lazy to sit and just practice. Now I can practice on the go like all the cool kids.


# Installation

1. Download this repository by clicking the "Clone or download" button and saving as a zip
2. Extract the zip to wherever, navigate into it, and run "python setup.py install"
3. That's it! See the next section.

# How to use

Use python 3.6. Untested with python 2. 

An example run would be:

```
python run.py  10#0(1)1000{+-}-50(2)60?5000(2)
```
This assumes you're in the directory where the Mathtraq package has been installed.


The following is copied from the help output of the app itself:

```
usage: run.py [-h] [-j OUTPUT_JSON] [-o OUTPUT_MP3] [-d MAX_DIGITS]
              [-b BUFFER_SIZE] [-v {0,1,2,3}] [-t TEMP_DIR] [-z] [-f]
              [-p pause_between_questions]
              template [template ...]

Create an mp3 to practice arithmetic on the go

positional arguments:
  template              Example: 10#0(1)1000{+/-}-50(2)60?3000(2) will create
                        10 questions where the lhs is between 0 and 1000 with
                        maximum 1 decimal place and the rhs is between -50 and
                        60 with a maximum of 2 decimal places. They will be a
                        mix of addition, division and subtraction, and a
                        3000ms pause will occur before the answer is given.
                        The answer will be rounded to 2 decimal places.
                        Operands can be decimals. Operators can be +, -, * or
                        / (note that one * in the ops is multiplication, two *
                        means 'to the power of' and three means both
                        multiplication and powers)

optional arguments:
  -h, --help            show this help message and exit
  -j OUTPUT_JSON, --json OUTPUT_JSON
                        Specify a file to which the equation data will be
                        written in JSON format
  -o OUTPUT_MP3, --output OUTPUT_MP3
                        MP3 file output (default: ['mathtraq.mp3'])
  -d MAX_DIGITS, --digits MAX_DIGITS
                        Maximum digits (precision) (default: [600])
  -b BUFFER_SIZE, --buffer_size BUFFER_SIZE
                        Mathtraq works by concatenating a number of small
                        files. This argument specifies how many to join at a
                        time. (default: [600])
  -v {0,1,2,3}, --verbosity {0,1,2,3}
                        0 is no output and 3 is a lot (default: [1])
  -t TEMP_DIR, --temp_dir TEMP_DIR
                        relative path to temporary folder (useful if multiple
                        instances running at once- default: ['temp'])
  -z, --forget_mp3      use with -j to only output the json
  -f, --flush_output    include to immediately flush the output stream
  -p pause_between_questions, --ms_pause pause_between_questions
                        Milliseconds to pause after each question. Rounds down
                        to nearest 500, minimum 500 (default: [500])

If you get an error whilst wanting a lot of precision, try raising the
precision (-d argument)
```

# Notes:

* Uses mp3cat (https://github.com/dmulholland/mp3cat) to concatenate the files - developed by Darren Mulholland

* Uses mpmath (http://mpmath.org/) to achieve arbitrary number length - developed by Fredrik Johansson

* You can replace the audio files for the sound bites - just make sure they're all the same bitrate. Feel free to share them if you do- I've slightly modified my own voice but still... no one wants to hear themselves speak.

* Add more places (eg. 'septillion') by adding the mp3 file into the place_values folder, adding the name of the place value into the audio.place_names list between the current highest and the default 'somethings', and finally add an entry into audio.audio_segments pointing to the audio file.