# What Is It?

This is a python script that builds custom mp3 files containing random arithmetic equations. You specify how
many equations you want, parameters for both the operands and the operator, the pause length between the question
and the answer and between equations themselves, and you get an mp3 file that satifies those parameters.

Why? Because I suck at arithmetic and I'm too lazy to sit and just practice. Now I can practice on the go.

# How to use

The following is copied from the help output of the app itself:

usage: mathtraq.py [-h] [-j OUTPUT_JSON] [-o OUTPUT_MP3] [-d MAX_DIGITS]
                   [-b BUFFER_SIZE] [-v {0,1,2,3}]
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
                        The answer will be rounded to 2 decimal places

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
  -p pause_between_questions, --ms_pause pause_between_questions
                        Milliseconds to pause after each question. Rounds down
                        to nearest 500, minimum 500 (default: [500])

If you get an error whilst wanting a lot of precision, try raising the
precision (-d argument)


# Notes:

* Uses mp3cat (https://github.com/dmulholland/mp3cat) to concatenate the files - developed by Darren Mulholland

* You can replace the audio files for the sound bites - just make sure they're all the same bitrate

* Supports specifying power-of expressions as ** but, for now, it's not implemented and something somewhere will break