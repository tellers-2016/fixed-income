# Exercises
In doing the exercises below, I would recommend you implement the solutions to these problems as generic re-usable functions, so that a solution that you write for one problem, can be used (at least in part) to solve the next question in the exercises. In general formulas should be implemented as static, generic functions so that any solution that needs that formula can just call the function that you've written once.

## Time Value
* A CD from Chasing bank offers a 2.5% annual interest for a term of 4 years. If an investor decides to invest $4,000 into this CD what would be the value of the of their investment at the end of the term ? 
* For the same CD if an investor would receive proceeds of $6,850 what must be the Present Value of this investment ?
* An investor buying in to a Zero Coupon Bond paid $9000 as the initial investment, and received proceeds of $14000 at the end of 8 years. Calculate the yield (annualized return) that the investor received for this investment ?
* A 10 year bond with a $1000 face value that pays a 5% coupon rate ? The cash flows on this investment would be as follows
  * T1 through T9: $50
  * T10: $1050 
  * What is the Present value of this Bond if the investor received a yield of 6% at T10 (Proceeds of $1050 at T10) ?
  * What is the Present value of this bond if the yield was 5% ? 
  * If the investor paid $1200 for this bond at T0 (Present), what is the future value of this bond at maturity (T10) ? 
* Calculate the Internal Rate of Return on the following stream of payments
 * Initial Investment: $5000
 * Payouts from Year 1 - 5: $2000
 * Payout in year 6: $1000  `Use the IRR function in numpy`
* Fracker Inc is considering a project to drill for Shale oil in North Dakota. It has evauated that the project would require an initial investment of $1 Million and a further investment of $20,000 for years 1 and 2. In Year 3 it expects the drilling to complete and anticipates revenues of $50,000 for each of the next 12 years. In year 12 it intends to sell off the assets and equipment for a then value of $10,000. Assuming a cost of capital of 7%
 * Calculate the Net Present Value for this project. `Do not use the numpy.irr function for this. Write the code to manually discount thec cash flows`
 * Calcuate the IRR For this project.
 * Should Fracker proceed with this project ?

## Bonds
* General Electric has issued a 5 year bond to the market with a face value of $1000 and a coupon rate of 7%. Write a program that would 
  * print out the payments that an investor in this bond would receive from inception to maturity
  * If the current yield on this bond is 12%, print out what must be the current price of this bond
  * Assume now that GE has also issued another bond with the same face value and coupon rate, but the term of this new bond is 10 years. If this bond is also providing a yield of 12% print the price that it would be trading at
  * Calculate the percentage change in price for each bond if the yields on both of them changed to 14%. Which bond shows a larger change in price ?
 
* Suppose a 5 year bond has a face value of $1000 and a coupon rate of 8%. Calculate the yield to maturity on this bond for the following scenarios
  * The price of this bond is $800
  * The price is $1000
  * The price is $1200

* Calculate the Yield to Maturity and the Effective Annual Yield on a 5 year semi-annual coupon paying bond with a 4% coupon rate and face value of $5000. 
 
* A 4 year annual coupon bond at 5% coupon rate with $1000 face value and a yield to maturity of 6%.
  * What is the current price of this bond ? 
  * What is the future value of this bond ? 
  * What is the Annualized Realized Return on this bond ? Compare this to the Yield to maturity
  * If the coupon payments in Years 2 and 3 are re-invested at a yield of 10% 
   * What is the future value of the bond ? 
   * What is the Annualized Realized Return on this bond ? Compare this to the Yield to maturity 

* Calculate the Duration of a 4 year coupon bond with a coupon rate of 8% and face-value of $1000 with a Yield to Maturity of 10%
 * If the Yield to Maturity changes to 12% what is the percentage change in Price of this bond ?
