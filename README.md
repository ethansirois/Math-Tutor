# Inspiration
It has always been interesting to me that ChatGPT has struggled with math problems that computers have been able to answer for so long. Anytime you're dealing with numbers with many significant figures or less common numbers, ChatGPT really struggles to produce the right answer. GPTs can mostly provide the correct reasoning and steps of a problem, it's just the actual calculations and algebra that it struggles with. Therefore, it makes the most sense to still have the GPT API generate the steps to solve the problem, and even generate the correct code for the steps, but just not do any calculations. I have the model generate a Python code block to compute the necessary calculations, which is then executed to get the answer.

# Methods
I utilized the GPT API from OpenAI as my GPT, specifically 3.5-turbo (default). I primarily chose a GPT API because it is so powerful for NLP, but I also wanted to show that ChatGPT has potential for answer math problems well. I chose to use Python scripts because there are plenty of Python packages that are great for solving math problems, and Python is a well documented language, so I thought GPT would know how to program it well. I previously had the model generate WolframScript code blocks, but this was causing some errors and I don't know WolframScript so it was harder for me to debug.
Here is a general pipeline of the program:
1. The problem is fed to a GPT model that has been prompted that it is an elegant mathematician and Python expert. It has the ability to create Python code blocks by enclosing them in three backticks. It also has the ability to install any packages that are not downloaded by using ```os.system(‘pip install {insert package name here}’)```. I previously told the model that it could check if the package was installed using importlib.util.find_spec({package name}), but this seemed to be too much information or something because then the model stopped downloading packages when necessary.
2. The code that is enclosed in the three backticks is then turned into one string, with the contents of the string being what the entire Python file should contain.
3. A temporary Python file named “py.py” that will run this program is created, and then the code is written to this file. This file is then executed using ```os.system(“python py.py > out.txt”)``` to write the output of this file, which is the calculated answer, to out.txt.
4. I then have a final GPT model evaluate what the question is really asking to confirm that this answer is generally appropriate, and append the right units. This provides a concise final answer to the problem.

# Using the Code
If you're interested in running the program, make sure to include your own API key from OpenAI in the HIDDEN.py file.
I have not yet added any UI components, so running this program will prompt an input from the user to type in their question. 

# Results
The program has been able to correctly answer the questions where ChatGPT fails due to large or higher-precision numbers. On problems that ChatGPT struggles with such as more advanced SAT Math questions, the program is still inconsistent. It is able to get the correct computation after a few tries, but it struggles to consistently provide a correct answer (when running the program, I offer to regenerate the answer, increasing the temperature to create more randomness in hopes that it will land on the right answer). I am still experimenting with different temperatures and prompts for the GPT APIs. It appears that most of the incorrect results happen when generating the WolframScript, I suspect because it’s not as popular of a language, so GPT APIs haven’t been fed enough information to produce bug-free code. It could also just be because GPT APIs struggle with generating code in general.

# Note to AI @ UIUC
I just wanted to state that I had no prior experience creating or using an AI program before. I hope what I've been able to learn and program in this short timespan demonstrates my interest in developing many more AI applications with the development team (and hopefully research team next year), and my ability to learn new APIs, packages, and tools. I hope to hear back soon!

# Future Plans
I started this project for my AI @ UIUC application, but I plan to continue building it. I will add a UI and experiment with different temperatures and generations. I also hope to add some sort of functionality for vision in the future. At first, this would look like being able to read a problem that is submitted by photo, but then hopefully expand to more complex tasks, such as reading tables, analyzing geometric diagrams, and analyzing function graphs.

