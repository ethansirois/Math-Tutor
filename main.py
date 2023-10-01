import os
import openai
from HIDDEN import API_KEY
openai.api_key = API_KEY


def generate_steps(problem, temp):
    messages = [
        {"role": "system", "content": "You are an elegant mathematician and the user needs your help solving the "
                                      "problem. You know that the user has a very precise "
                                      "calculator, so you guide them on how to solve the problem by telling them"
                                      " what the necessary calculations they need to input to their calculator are. "
                                      "You must never calculate something yourself, instead you write out the solution"
                                      " so that someone could evaluate it all with a calculator. You plan "
                                      "your solution with what the problem is really asking for in mind, keeping out "
                                      "any unnecessary calculations."},
        {"role": "user", "content": "Provide a solution on how someone could solve the following problem: " +
                                    problem + '\n'}
    ]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temp
    )
    return completion.choices[0].message["content"]


def generate_code(steps):
    messages = [
        {"role": "system", "content": "You are an elegant mathematician and a mathematica expert."
                                      "Given a step-by-step solution on how to solve a problem, you generate the "
         "necessary mathematica code to compute the solution in the variable 'answer'. You do this in a clear "
                                      "manner, maximizing readability and minimizing potential errors. After"
                                      " calculating the correct "
                                      "value for 'answer', you always have the following line: 'Print[N[answer]]'."
                                      " You always surround"
                                      " your code blocks with triple apostrophes---i.e., you have a line of triple"
                                      " apostrophes before the code block, and a line of triple apostrophes after"
                                      " the code block."},
        {"role": "user", "content": "I will provide you with the necessary steps to solve a mathematics problem. You "
                                    "will then generate the correct mathematica code to compute the necessary "
                                    "calculations. Here are the steps to the problem: " + steps + '\n'}
    ]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    return completion.choices[0].message["content"]


def generate_pure_code(code):
    split_up = code.splitlines()
    in_block = False
    code_blocks = []
    start_block = -1
    for i in range(len(split_up)):
        if "'''" in split_up[i]:
            if in_block:
                code_blocks.append((start_block, i))
            else:
                start_block = i
            in_block = not in_block
    pure_code = ""
    if len(code_blocks) == 0:
        pure_code = code
    elif start_block == -1:
        return 'FAILURE'
    for block in code_blocks:
        for i in range(block[0] + 1, block[1]):
            pure_code += split_up[i] + '\n'
    return pure_code


def compute(code):
    pure_code = generate_pure_code(code)
    with open('wls.txt', 'w') as fp:
        fp.write(pure_code)
    os.system('wolframscript -file wls.txt > out.txt')
    f = open('out.txt', 'r')
    content = f.read()
    if len(content) == 0:
        print("failure, the steps have some mistakes")
    else:
        lines = content.splitlines()
        answer = lines[0]
        return answer


def provide_answer(problem, steps, answer):
    messages = [
        {"role": "system", "content": "You are an elegant mathematician, whose job is to verify that someone's work "
                                      "is correct. You will first be given the problem. Determine what the problem is "
                                      "asking, and keep this in mind while evaluating the solution. You will then be"
                                      " given the steps of the solution you are supposed to evaluate. "
                                      "You will lastly be given a calculated answer to the "
                                      "problem. Ignoring any calculations in the steps, it is your primary duty to "
                                      "determine if the answer that is provided "
                                      "is an acceptable answer to the problem. If the problem has not been solved--- "
                                      "i.e., the answer is blank--- "
                                      "you need to clearly state that the solution is most likely wrong."},
        {"role": "user", "content": "Here is the problem: " + problem + ". Here are the steps of the solution which"
                                        "you are evaluating: " + steps + ". Here is the "
                                        "calculated answer: " + answer + ". Describe to me if the problem has been "
                                        "solved, and if it has, then what does my "
                                        "answer represent? Be sure to include proper "
                                        "units. Reference the units provided in the problem if they exist." + '\n'}
    ]
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    return completion.choices[0].message["content"]


def clear():
    os.remove('wls.txt')
    os.remove('out.txt')


def main():
    temp = 0
    still_going = True
    print("Please input your question")
    problem = str(input())
    print("\nHappy to help! One moment please.")
    while still_going and temp <= 2:
        print("answering...")
        steps = generate_steps(problem, temp)
        code = generate_code(steps)
        answer = compute(code)
        response = provide_answer(problem, steps, answer)
        print("here is the answer:")
        print(response)
        print("Is this answer sufficient? If not, we'll turn up the temp and hope for the best (answer with 'y' or "
              "'n')")
        user_input = input()
        still_going = user_input == 'n'
        temp += 1
        print("want to see the steps produced? (answer with 'y' or 'n'")
        user_input = input()
        if user_input == 'y':
            print(steps)
        print("want the temporary code files to be cleared? (answer with 'y' or 'n')")
        user_input = input()
        if user_input == 'y':
            clear()


def not_main():
    os.system('wolframscript -file tester.txt > t.txt')
    f = open('t.txt', 'r')
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        print(line)



nm = False
if nm:
    not_main()
else:
    main()

