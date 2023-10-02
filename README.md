# Inspiration
It has always been interesting to me that ChatGPT has struggled with math problems that computers have been able to answer for so long. Anytime you're dealing with numbers with many significant figures or less common numbers, ChatGPT really struggles to produce the right answer. GPTs can mostly provide the correct reasoning and steps of a problem, it's just the actual calculations and algebra that it struggles with. Therefore, it makes the most sense to still have the GPT API generate the steps to solve the problem, and even generate the correct code for the steps, but just not do any calculations. I have the model generate a Python code block to compute the necessary calculations, which is then executed to get the answer.

# Methods
I utilized the GPT API from OpenAI as my GPT, specifically 3.5-turbo (default). I primarily chose a GPT API because it is so powerful for NLP, but I also wanted to show that ChatGPT has potential to answer math problems well. I chose to use Python scripts because there are plenty of Python packages that are great for solving math problems, and Python is a well documented language, so I thought GPT would know how to program it well. I previously had the model generate WolframScript code blocks, but this was causing some errors and I don't know WolframScript so it was harder for me to debug.
Here is a general pipeline of the program:
1. The problem is fed to a GPT model that has been prompted that it is an elegant mathematician and Python expert. It has the ability to create Python code blocks by enclosing them in three backticks. It also has the ability to install any packages that are not downloaded by using ```os.system(‘pip install {insert package name here}’)```. I told the model that it could check if the package was installed using importlib.util.find_spec({package name}).
2. The code that is enclosed in the three backticks is then turned into one string, with the contents of the string being what the entire Python file should contain.
3. A temporary Python file named “py.py” that will run this program is created, and then the code is written to this file. This file is then executed using ```os.system(“python py.py > out.txt”)``` to write the output of this file, which is the calculated answer, to out.txt.
4. I then have a final GPT model evaluate what the question is really asking to confirm that this answer is generally appropriate, and append the right units. This provides a concise final answer to the problem.

# Demo
Here's an example where my program is able to correctly answer the question, and ChatGPT falls quite short. And there are plenty of examples where GPT will calculate a big/precise number wrong and mine is correct, but this one is especially demonstrative.
The problem is the following:
What's the probability that two randomly generated numbers, one representing an x-coordinate and one representing a y-coordinate, that are between 0 and 1 inclusive, are inside a circle centered at the origin with radius 1?
(This can be used to approximate pi using Monte Carlo methods. The correct answer is pi / 4, which is approximately 0.78539816339.)
![Screenshot 2023-10-01 at 2 31 06 PM](https://github.com/ethansirois/Math-tutor/assets/114622541/ae9683f5-409e-4f03-bd54-39787506f71d)
<img width="839" alt="Screenshot 2023-10-01 at 2 31 40 PM" src="https://github.com/ethansirois/Math-tutor/assets/114622541/48c2ce6d-a8e2-4cf6-85f9-1309d9505796">

Here's another example with linear algebra. Linear algebra seems to be one of the areas with the biggest differences; ChatGPT really struggles but this model utilizing Python scripts performs much better. 

<img width="1353" alt="Screenshot 2023-10-02 at 12 13 38 PM" src="https://github.com/ethansirois/Math-tutor/assets/114622541/7b7c9d24-99e9-431f-8743-7629530dd191">

<img width="680" alt="Screenshot 2023-10-02 at 12 07 42 PM" src="https://github.com/ethansirois/Math-tutor/assets/114622541/6508a0d2-cc0d-45fb-b5e3-c0942ca4bb9a">
<img width="464" alt="Screenshot 2023-10-02 at 12 15 42 PM" src="https://github.com/ethansirois/Math-tutor/assets/114622541/12c568a7-b923-484b-9a37-bf54d0997b7a">


The inputted question was "determine the inverse of the following matrix: [(1, -1, 1), (1, 1, 1), (1, 2, 4)]"
The answer is, like my model said, [(1/3, 1, -1/3), (-1/2, 1/2, 0), (1/6, -1/2, 1/3)]
. So again, ChatGPT by itself, not very good at math, but GPT models have the ability to create Python files that can get the correct answer, so leveraging this creates huge improvements at their math capabilities.

# Results
The program has been able to correctly answer the questions where ChatGPT fails due to large or higher-precision numbers. On problems that ChatGPT struggles with such as more advanced SAT Math questions, the program is still inconsistent, and this is a limitation due to GPT models not understanding the problem. The model is very good at problems that involve "plug and chug" formulas like linear algebra problems or integrating, because there are many existing tools to do these computations in Python like NumPy and SymPy.

# Note to AI @ UIUC
I just wanted to state that I had no prior experience creating or using an AI program before. I hope what I've been able to learn and program in this short timespan demonstrates my interest in developing many more AI applications with the development team (and hopefully research team next year), and my ability to learn new APIs, packages, and tools. I hope to hear back soon!

# Using the Code
If you're interested in running the program, make sure to include your own API key from OpenAI in the HIDDEN.py file.
I have not yet added any UI components, so running this program will prompt an input from the user to type in their question. 

# Future Plans
I started this project for my AI @ UIUC application, but I plan to continue building it. I will add a UI and experiment with different temperatures and generations. I also hope to add some sort of functionality for vision in the future. At first, this would look like being able to read a problem that is submitted by photo, but then hopefully expand to more complex tasks, such as reading tables, analyzing geometric diagrams, and analyzing function graphs.


