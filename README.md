# Inspiration
It has always been interesting to me that ChatGPT has struggled with math problems that computers have been able to answer for so long. Anytime you're dealing with numbers with many significant figures or less popular numbers, ChatGPT really struggles to produce the right answer. GPTs can mostly provide the correct reasoning and steps of a problem, it's just the actual calculations and algebra that it struggles with. Therefore, it makes the most sense to still have the GPT API generate the steps to solve the problem, but just not do any calculations. I then create a WolframScript file with the necessary calculations and return an answer containing this calculation.

# Methods
I utilized the GPT API from OpenAI as my GPT, specifically 3.5-turbo (default). Primarily because the model is so powerful, but I also wanted to show that the model becomes much more accurate with the calculations being executed properly. I used WolframScript to compute the computations. This is because this model is designed for mathematics, and is very powerful at tasks like solving systems of equations.
Here is a general pipeline of the code:
1. The problem is fed to a GPT model that has been prompted that it is an elegant mathematician and that it is to only determine the proper steps to solve the problem without ever doing a calculation.
2. These steps are then fed to another GPT model that has been prompted to be a mathematician who is an expert in WolframScript. I prompt the model to enclose its code blocks with three apostrophes to distinguish between the code and any other words produced.
3. These code blocks are then combined into one code block, where the last line is printing the value of the answer. This final code block is then saved into a text file and then executed on the command line using the Python package "os". I save this output of the calculated answer to a text file, "out.txt".
4. I then have a final GPT model evaluate what the question is really asking to confirm that it is generally appropriate, and append the right units. This provides a concise final answer to the problem.

# Using the Code
If you're interested in running the program, make sure to include your own API key from OpenAI in the HIDDEN.py file.
I have not yet added any UI components, so running this program will prompt an input from the user to type in their question. 

# Results
The program has been able to correctly answer the questions where ChatGPT fails due to large or higher-precision numbers. On problems that ChatGPT struggles with such as more advanced SAT Math questions, the program is still inconsistent. It is able to get the correct computation after a few tries, but it struggles to consistently provide a correct answer (when running the program, I increase the temperature to create more randomness and creativity in hopes that it will land on the right answer). I am still experimenting with different temperatures and prompts for the GPT APIs. It appears that most of the incorrect results happen when generating the Wolfram Script, I suspect because it’s not as popular of a language, so GPT APIs haven’t been fed enough information to produce bug-free code. It could also just be because GPT APIs struggle with generating code in general.

# Future Plans
I started this project for my AI @ UIUC application, but I plan to continue building it. I will add a UI and continue experimenting with different methods for performing computations, such as utilizing Python scripts instead, or moving to smaller individual WolframScript computations. I also hope to add some sort of functionality for vision in the future. At first, this would look like being able to read a problem that is submitted by photo, but then hopefully expand to more complex tasks, such as reading tables, analyzing geometric diagrams, and analyzing function graphs.


