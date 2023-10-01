# Inspiration
It has always been interesting to me that ChatGPT has struggled with math problems that comptuers have been able to answer for so long. Anytime you're dealing with numbers with many significant figures or less popular numbers, ChatGPT really struggles to produce the right answer. GPTs can mostly provide the correct reasonings and steps of a problem, it's just the actual calculations and algebra that it struggles with. Therefore, it makes the most sense to still have the GPT API generate the steps to solve the problem, but just not do any calculations. I then create a Wolframscript with the necessary calculations and return an answer containing this calculation.

# Methods
I utilized the GPT API from OpenAI as my GPT, specifically 3.5-turbo (default). Primarily because the model is so powerful, but I also wanted to show that the model becomes much more accurate with the calculations being executed properly. I used Wolframscript to compute the computations. This is because this model is designed for mathematics, and is very powerful at tasks like solving systems of equations.
Here is a genearl pipeline of the code:
1. The problem is fed to a GPT model that has been prompted that it is an elegant mathematician and that it is to only determine the proper steps to solve the problem without ever doing a calculation.
2. These steps are then fed to another GPT model that has been prompted that it is also a mathematician who is an expert in Wolframscript. I prompt the model to enclose its code blocks with three apostrophes.
3. These code blocks are then combined into one code block, where the last line is printing the value of the answer. This final code block is then saved into a text file and then executed on the command line using the Python package "os". I save this output to a text file, "out.txt". 

# Using the Code
I have not yet added any UI components, so running this program will prompt an input from the user to type in their question. The Wolframscript
