# Mortgage Calculator

### Objective
Students must write a mortgage calculator. The program must be able to take in specifics about a mortgage as listed below
 * The Principal to be borrowed
 * The Rate of the Loan
 * The term of Loan (in years)

The program must calculate the monthly payment for a Fixed Rate Mortgage based on the values of the parameters listed above. Additionally, the program must calculate the amortization table for the mortgage that lists out the payments required for each month of the duration of the mortgage along with the following details for each month

 * The month number
 * The principal component of this month's payment
 * The interest component of this month's payment
 * The principal balance left over after this month's payment
 * The cumulative interest paid on the mortgage upto this month
 * The cumulative principal paid on the mortgage upto this month
 * The cumulative payments made on the mortgage upto this month

Along with the monthly payments, the amortization table should also contain the following totals and metrics

 * The Sum total of all payments made
 * The Total principal paid during the life of the loan
 * The Total interest paid on the load
 * The Interest as a percentage of the overall payments
 * The Interest as a percentage of the principal borrowed (and repaid)

Finally, the program should plot out the payments made over the life of the mortgage on a line graph. Specifically the graph should show the following
 * The principal balance over time
  * This will be a plot of the principal balance and the month number from the monthly payments in the amoritzation schedule
 * The interest payment over time
  * This will plot the cumulative interest paid and the month number from the monthly payments in the amortization schedule
 * The total payments made over time
  * This plots the total payments from the monthly payments in the amortization schedule
The graph should be keyed by the month number on the X axis and show a separate line for each of the three numbers above on the Y axis

### Formula
You will need to implement the formulas as part of this project

#### To Calculate the monthly payment on a fixed mortgage
```
c = r * P / (1 - ((1 + r) ^ -N))

Where
 * r: The monthly interest rate that you get using R / 12 / 100 where R is the annual interest rate
 * P: The Principal borrowed on the loan
 * N: Number of monthly payments on the loan
 * c: The monthly payment
```

#### To Calculate the Interest Component of a monthly payment
```
i = P * r

Where
 * r: The monthly interest rate (R / 12 / 100 where R is the annual interest rate)
 * P: The outstanding principal balance
 * i: The monthly interest rate
```

### Guidelines
This problem is best approached by breaking it into separate components(classes) where each class handles a specific part of the solution. As such you should follow the model view controller (MVC) pattern to split up your code into various pieces
 
#### Model classes
These would be the objects that hold the data. There will be instances of these classes that are passed to or returned by methods of the calculator class. Specific possibilities for this project would be
 * MonthlyDetails
  * Instances of this class should hold the details of a particular monthly payment (The month number, interest component, principal component, etc.)
 * AmortizationSchedule
  * An instance of this class would hold details of an amortization schedule. It would have an array of MonthlyDetails instances, along with dictionary for the totals and metrics

#### The Controller class
This like any controller class should be the orchestrator that makes the call to the calculator to have it calculate data and return back instances of the model classes with the data filled in them. It should then pass this data over to the view classes which would know how to "display" the data

#### The View classes
You should a View class that handles the job of taking in data and either printing it out to the screen, or rendering it on a graph. In order to demonstrate the "pluggability" that MVC and Object Oriented programming gives you should create a separate class for each way you want to display the data.
 * PrintView: This class should take in the amortization schedule and simply print out its details to the terminal console
 * GraphView: This class should render the details of the amortization metrics out on a graph, using the matplotlib library


#### A Calculator class
This class should expose methods that implement all of the calculations needed for this project. Its methods should take in the inputs needed for the calculation and should return back the results of the calculation in model objects. This class as such should not hold any state, in that it simply exposes methods that take in inputs to a formula, runs them through the formula and return back the result. It should not need to store anything across calls. 
The methods of the Calculator class should be called from the Controller given that it is the orchestrator for the project.
 
> This class will be required to expose a given set of functions which should perform that various calculations required. **A test class will be provided which will make calls to a set of functions on the Calculator class and will check the results returned. You should look at the test cases to know what functions on the Calculator class you need to expose and implement.**

