# Debugging #

- Act of finding errors, bugs in code and removing them is called debugging. It is very import for a python developer to
  know, how to debug a code. If you can't debug your code, you are not a good developer.
- Debugging helps us a lot to understand code flow, various cases, root cause of error and in a way we understand how to
  solve those errors.
- Best way to become good at it comes from experience, just keep coding and keep debugging. Eventually you become good
  at it.

## Tips for debugging ## 

- Please make sure you are using linter which gives you errors and all.
- Use IDEs like Pycharm for Python which gives you best suggestions and has inbuilt linting.
- Use pdb module (Python inbuilt debugger) for debugging code. pdb has many inbuilt functions which helps us to debug
  our code. Once bug is fixed, remove pdf commands from your code and push it for testing/QA.
- To know more about pdb functions: Type **help** once you code runs and goes into pdb terminal environment. To read
  documentation of any pdf function type **help function_name**
- [Learn more about pdb](https://www.geeksforgeeks.org/python-debugger-python-pdb/)
- Learn how to debug code in the IDE which you are using, set break points and start running code.
- Please make sure, you don't name files same as standard built in files otherwise debugger will fail specially in
  Pycharm

```python
import pdb


def add(a, b):
    pdb.set_trace()
    return a + b


print(add(1, "hello"))
```