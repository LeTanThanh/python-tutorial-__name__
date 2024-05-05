if __name__ == "__main__":
  # What’s Python __name__?

  """
  If you have gone through Python code, you've likely seen the __name__ variable like the following:
  """

  if __name__ == "__main__":
    print("main()")

  """
  And you might wonder what the __name__ variable is.

  Since the __name__ variable has double underscores at both sides, it's called dunder name.
  The dunder stands for double undersores.

  The __name__ is a special veriable in Python.
  It's special because Python assigns a different value to it depending on how its containing script executes.

  When you import a module, Python executes the file associated with the module.

  Often, you want to write a script that can be executed directly or imported as a module.
  The __name__ variable allows you to do that.

  When you run the script directly, Python sets the __name__ variable to "__main__".

  However, if you import a file as a module, Python sets the module name to __name__ variable.
  """

