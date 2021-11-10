print("""
      +---------------------------------+
        Welcome to Simple Calculator v2
      
      A much better desgined program made
       for mainly lazyness but also for
      studying purposes and ppl to learn
      python, a really nice programming
      high-class language :)

      +---------------------------------+
      """)

print("")

print("""
      +---------------------------------+
      Available operations:
      
      1. Sum 2 values
      2. Substract 2 values
      3. Multiply 2 values
      4. Divide 2 values

      5. (BETA) Get the percentage of
          a specific value
      6. (BETA) Get a value to the power
      from 1 to 10

      To end the session, just type 0
      +---------------------------------+
      """)

choice = int(input("Choose an option:"))

while choice != 0:
    if choice == 1:
        value1 = int(input("Alright, what is the first value:"))
        print("")
        value2 = int(input("Now the second one:"))
        print("")
        result1 = value1 + value2
        result2 = value2 + value1
        print(f"""
              Alright, here are the results:
              
              Value 1 + Value 2 = {result1}

              Value 2 + Value 1 = {result2}

              """)
        choice = int(input("Choose an option:"))
    if choice == 2:
        value1 = int(input("Alright, what is the first value:"))
        print("")
        value2 = int(input("Now the second one:"))
        print("")
        result1 = value1 - value2
        result2 = value2 - value1
        print(f"""
              Alright, here are the results:

              Value 1 - Value 2 = {result1}

              Value 2 - Value 1 = {result2}

              """)
        choice = int(input("Choose an option:"))
    if choice == 3:
        value1 = int(input("Alright, what is the first value:"))
        print("")
        value2 = int(input("Now the second one:"))
        print("")
        result1 = value1 * value2
        result2 = value2 * value1
        print(f"""
              Alright, here are the results:

              Value 1 x Value 2 = {result1}

              Value 2 x Value 1 = {result2}

              """)
        choice = int(input("Choose an option:"))
    if choice == 4:
        value1 = int(input("Alright, what is the first value:"))
        print("")
        value2 = int(input("Now the second one:"))
        print("")
        result1 = value1 / value2
        result2 = value2 / value1
        print(f"""
              Alright, here are the results:

              Value 1 - Value 2 = {result1}

              Value 2 - Value 1 = {result2}

              """)
        choice = int(input("Choose an option:"))
    if choice == 5:
        value1 = int(input("Alright, what is the value we are getting\nthe percentage from:"))
        print("")
        value2 = int(input("And what is the precentage we are getting:"))
        print("")
        result1 = value1 * value2 / 100
        print(f"""
              Alright, here is the percentage:

              The {value2}% of {value1} is: {result1}

              """)
        choice = int(input("Choose an option:"))
    if choice == 6:
        value1 = int(input("Alright, what number should we work with:"))
        #pls help with this cos i don't want this huge line here ._.
        result2 = value1 * value1
        result3 = value1 * value1 * value1
        result4 = value1 * value1 * value1 * value1
        result5 = value1 * value1 * value1 * value1 * value1
        result6 = value1 * value1 * value1 * value1 * value1 * value1
        result7 = value1 * value1 * value1 * value1 * value1 * value1 * value1
        result8 = value1 * value1 * value1 * value1 * value1 * value1 * value1 * value1
        result9 = value1 * value1 * value1 * value1 * value1 * value1 * value1 * value1 * value1
        result10 = value1 * value1 * value1 * value1 * value1 * value1 * value1 * value1 * value1 * value1
        print(f"""
              Such job! - Well here are the results:

              {value1} to the power of 1 = {value1}
              {value1} to the power of 2 = {result2}
              {value1} to the power of 3 = {result3}
              {value1} to the power of 4 = {result4}
              {value1} to the power of 5 = {result5}
              {value1} to the power of 6 = {result6}
              {value1} to the power of 7 = {result7}
              {value1} to the power of 8 = {result8}
              {value1} to the power of 9 = {result9}
              {value1} to the power of 10 = {result10}

              """)
        choice = int(input("Choose an option:"))
    else:
        print("""

              Either you entered a string value, a boolean
              or a number that isn't handled properly, try
              again with a valid one next time :(

              """)
        choice = int(input("Choose an option:"))
    #oh and also I need to handle in the case of the user using
    #a string value otherwise python stops running :P

print("""
      
      Goodbye! - Thanks for using me for your tasks

      And stay strong in this trying times :D
      - minecon099

      """)
