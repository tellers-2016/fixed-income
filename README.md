# Fixed Income Securities

## Time Value of Money

### Money today is worth more than the same amount tomorrow
Time has value
  * Money received today can be invested and grown to a larger amount by tomorrow (financial perspective). 
  * $100 today buys a lot less than $100 30 years ago due to inflation (economics perspective)
Therefore investors that provide money today will demand interest when it is returned to them tomorrow to compensate them for the **risk** they take with the investment, and the **time** that their money is tied up in investment.


### Present Value, Future Value, Yield
Present Value (PV), when invested at a Yield (annual interest rate) of R grows to the Future Value (FV)

#### Single payment Securities
eg. Bank CDs, Zero Coupon Bonds, etc. 

Future Value is obtained by multiplying the Present Value with the Future Value compounding factor.
 
 <code>FV = PV * (1 + R)<sup>T</sup></code>

* Investing for a single period: <code>FV = PV * (1 + R)</code>
 * Future Value is the Present Value plus the Simple Interest earned
* Investing for multiple periods: <code>FV = PV * (1 + R)<sup>T</sup></code>
 * Future Value is the Present Value plus the Simple Interest plus the Compounding factor (Interest on Interest)

eg. How much is $1000 invested for two years at an annual interest rate of 5% worth ?
<code>FV = 1000 * (1 + 0.05)<sup>2</sup> = 1102.50</code>

```
FV = 1000 + 2 * (1.05) + 0.05 * 0.05 * 1000 
Where
1000: Principal
2 * 1.05: Simple Interest
0.05 * 0.05 * 1000: Compond Interest (Interest on Interest)
```

Conversely, Present Value is the Future Value **discounted** by the Interest rate. To get the past value of money in the future you have to divide it by the interest at which it grew. Answers the question, how much is money in the future worth today ? 

 <code>PV = FV / (1 + R)<sup>T</sup></code>

eg. For an investment with an annual interest rate of 8%, how much do I need to invest today in order to get $1000 a year from now ?

<code>
PV = 1000 / (1 + 0.05) = 952.38
</code>

How about for $1000 two years from now ?

<code>
PV = 1000 / (1 + 0.05)<sup>2</sup> = 907.3
</code>

The Yield is calculated by a similar algebraic adjustment of the Future Value equation.

<code>R = (FV/PV)<sup>1/T</sup> - 1</code>

eg. At what annual rate does an investment of $1000 need to grow to be worth $1500 at the end of one year ? 

<code>
R = (1500 / 1000) -1 = 0.5  or 50%
</code>

In two years ?

<code>
R = (1500 / 1000)<sup>1/2</sup> - 1 = 0.22  or 22%
</code>

Note that the yield or rate of return that we calculate is always the annualized one. i.e. the rate at which the investment grew each year. 

This is different from the total yield which is calculated as 

<code>
R<sub>total</sub> = (FV/PV) - 1
</code>

#### Multiple Payment Securities
eg. Bonds, Annuities, that payout a stream of cash payments for the duration of the investment

The Present Value is calculated by discounting all of the Future Cash flows C(0), C(1), ...., C(T) obtained from the investment by the yield and summing them all up.
 
<code>
PV = C(0) + C(1)* 1/(1+R) + C(2)*1/(1+R)<sup>2</sup> + ...... + C(T)*1/(1+R)<sup>T</sup>
</code>

Similarly the Future value is the sum of future values of all of the Cash flows C(0), C(1), ..... , C(T)

<code>
FV = C(0)*(1+R)<sup>T</sup> + C(1)*(1+R)<sup>T-1</sup> + ....... + C(T)
</code>

The yield for these securities is the Internal Rate of Return that equates the Present Value to the sum of the discounted cash flows. Essentially it is the value of R that solves the equation

<code>
PV = C(0) + C(1)* 1/(1+R) + C(2)*1/(1+R)<sup>2</sup> + ...... + C(T)*1/(1+R)<sup>T</sup>
</code>

Unlike the other cases, the yield for multi-securities cannot be analytically calculated. Instead it is obtained by pure trial and error (solved that way in Excel and Scientific Calculators). To get the IRR in Python you would use the `irr function in the numpy package`  [numpy.irr()](http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.irr.html)

#### Applications
The Present Value of money is used fairly widely in Corporate and Project finance to evaluate new prospetive projects. When considering a new project, corporations determine how much they would need to initially invest in the project to get it up and running. They then estimate the revenue that the project would bring in and the time for which the project would run. Once they have all of the numbers, the discount all of the estimated future cash flows from the project to get their present value and compare it to amount needed to invest in the project. Based on the difference in the present value of the investment and present value of the future returns they decide whether to go ahead or abandon the project.

This is known as the **Net Present Value (NPV)*** evaluation. Specifically the Net Present value is the present value of all the cash flows. It is the revenues Net of the investments in the project.

* NPV: Done in two ways
 * The future cash flows are discounted by the project's **Cost of Capital** and summed up to get their present values. If the Sum of the future Cash Flows **Net** of the initial investment is > 0, the project is profitable: Adds value
 * The IRR that equates the future cash flows to the initial investment is calculated. IF the IRR is > the project cost of capital the project is profitable: Adds value

> eg. P&G wants to evaluate the viability of introducing a new Dishwashing Liquid to the market. The estimates of the potential project are the following
> Initial Investment: $100K
> Sales in Year 1: $20K
> Sales in Year 2: $30K
> Sales in Year 3: $40K
> Sales in Year 4: $10K (Machines are depreciated and sold)

> To get the IRR: Solve for 
> -100 + 20*1/(1 + IRR) + 30*1/(1 + IRR)<sup>2</sup> + 30*1/(1 + IRR)<sup>3</sup> + 30*1/(1 + IRR)<sup>4</sup> = 0


## Bonds: Main Features
A Bond is a fixed income instrument IOU issued by organizations to raise money (loan). The issuer (borrower) issues a bond that investors invest in
(lenders). The investors are compensated with a periodic interest payment (coupon) during the life of the bond (term). At the time of maturity, the investors are paid back the amount 
of their initial investment (face value).

### Issuer
The institution selling the bond to the market. Could be governments (US Treasury/States/Municipalities), Corporations, etc. This is the party that is borrowing money (short) from investors (long) that is to be paid back at termination time.

### Term
The number of years to maturity (at which time the initial investment is to be repaid).  
 * Short Term Bonds: Less than 1 year (T-bills, CDs)
 * Long Term Bonds: More than 1 year (T-bonds, Corporate Bonds)

### Par Value
Also called Face-value, is the payment made at maturity to the bond holders.
 * This is **different** from the price an investor pays to buy a bond.
 * Depending on how the bond is trading on the secondary market, the price of the bond may go up or down. But the face value or par value of the bond remains constant up until maturity.
 
### Coupon
The periodic interest paid out to holding investors during the life of the bond
 * Coupon Rate: The total annual interest payment per dollar face value
 * Period: The time between consecutive coupon payments (usually 6 months: semi-annual)
 * Can be fixed or variable (floating). We will assume fixed for our discussions.
 * For a Coupon rate of c on a bond with face value of F
  * The annual coupon payment (C) is calculated as: `C = F * c`
  * The semi-annual coupon payment (C) is calculated as: `C = F * c/2`

There are also financially engineered bonds that pay no coupons at all, instead, pay one large lump sum at the time of maturity. These are known as **Zero Coupon Bonds** and as such behave a lot like CDs that are offered by banks where the interest for each year is accured and paid out at the end. 

### Credit Risk
Metric associated with the bond to indicate the risk of default: i.e. whether the bond issuer will be able to re-pay the face value amount at the time of maturity.
Is one of the drivers of the Coupon Rate on the bond (The higher the risk of default, the higher the coupon rate demanded by investors)

### Pricing
A bond is traded on the secondary market between investors, and as such, its price will fluctuate during the life of the bond.

#### Pricing Factors 
 * Credit Risk: What is the current credit rating of the issuer ? Will it be able to pay back the face-value amount ?
  * eg. During the financial crisis, banks issued bonds at unusually high coupon rates seeking to obtain capital to cover its souring debts. Once the trouble passed and the banks came back on their feet again, those bonds soared in value. The reason being the credit rating of the issuing bank had greatly improved and you would be hard pressed to get another bond from that kind of corporate with that kind of a coupon rate.
 * Interest Risk: Have interest rates in the market risen or fallen since the bond was issued ? Is this bond still a good investment given its interest rate or are there higher lucrative coupon rate investments out there now ?
  * eg. When Interest rates rise, newly issued bonds have a higher coupon rate than those of their predecessors. Therefore in a rising interest rate environment, the prices of bonds go down. Since bonds that were previously issued have lower coupon rates than those recently available in the market, and will therefore see diminishing investor demand for them.
 * Time (Term of the bond): The term of the bond also plays a factor in the price of the bond and how sensitive it is to market movements. The longer the term of the bond, the higher coupon rate demanded by investors because:
  * Investors want to be compensated for *tying up* their money for a longer time (exposed to price fluctuations for a longer period of time in case they want to sell before maturity. Investors will also *miss out* out on a larger number of other investment opportunities should they arise)
  * A longer maturity period provides the issuer a longer period for which they can *lock in* the coupon rate. Issuers need to compensate investors for receiving this *luxury*
 
Based on how favourably the market views a bond, it could trade either at a premium (higher) or a discount (lower) to its face-value

### Option Provisions
Bonds can carry options on them, that allow issuers or holders a right that they can exercise
 * Callable bonds: The issuer can call back the bond, i.e. pay back the loan before it matures (essentially eliminating any pending coupon payments to holders)
 * Putability: The bondholder has the right to demand payment of the loan before maturity
 * Convertability: The bondholder has the right to exchange the bondh for stock (equity) in the issuer
 
 A bond with options, will have it reflected in the price at which it trades (options also affect bond price)

### Seniority and security
 * Senior, subordinated senior, junior bond holders. Senior holders get paid first in the event of bankruptcy.
 * Secured by properties, equipment (assets / collateral) or the issuer. Could also be secured by liquid assets like another income stream owned by the issuer.


## Yield to Maturity (YTM)
The Yield to Maturity or book yield is the theoretical rate of return that a bond investor would receive assuming the bond is held up to maturity. This is the internal rate of return on a bond that when used to time-discount the sum of all its future cash flows would equal the price paid for the bond.

Essentially, the YTM is the rate that would solve the equation

```
Price = Coupon(1)/(1 + YTM)^1  + Coupon(2)/(1 + YTM)^2  + Coupon(3)/(1 + YTM)^3 + .... + (Coupon(n) + Face Value)/(1 + YTM) ^ n
```

This is an important measure of the price at which the bond is currently trading at to determine whether it is priced at a premium or a discount, and thereby whether it is or is not a good investment. 
> The reason this is a theoretical number is because it assumes all of the coupon payments made during the life of the bond will also be re-invested at the same rate, which is rare given how prices and rates constantly move. More later...

### YTM based on Price
It is important to note that the YTM differs from the coupon rate which is set at the time of issues as a percentage of the face value of the bond. The coupon rate and the face value remain fixed for the life of the bond, therefore the coupon payments made out too will remain fixed for the life of the bond. The YTM is based on the **price** that an investor pays to invest in the bond and varies as the bond is traded up or down in the secondary market. 

Based on the equation for YTM, we can see that the Price and the YTM are **negatively correlated**. i.e. The higher the price you pay for the bond, the lower your Yield will be (because you are paying a higher price for a fixed stream of incoming payments) and vice versa.

### YTM on a Semi-Annual Coupon Bond
For a semi-Annual coupon bond (one that pays its coupons every 6 months) the YTM is calculated in 2 steps.

 1. Find the IRR that solves the equation based on the coupon cash flow, knowing that coupons are paid out twice as often at half the rate as that of an annual Coupon bond 
 `Price = Coupon(1)/(1 + IRR)^1  + Coupon(2)/(1 + IRR)^2  + .... + (Coupon(2n) + Face Value)/(1 + IRR) ^ 2n`
 2. The Annualized YTM will then be twice that of the IRR calculated in step 1: `YTM = 2 * IRR`
 3. The effective annual rate, that incorporates the effect of semi-annual componding is `(1 + YTM/2)^2 - 1`

### Effective Realized Return vs YTM
The Yield to Maturity is largely theoretical rate, in that if you invest in a bond and add up the stream of payments that it gives back up until maturity and calculate the actual return that you received it will rarely equal the calculated YTM at the time of investment. It could be close, but is rarely equal. This is because
 * The YTM makes a key assumption that all coupon payments are invested at the exact same rate
  * In reality this is rarely possible. You would either have to find another investment at the same rate, or if you want to re-invest in the same bond, would need the bond to be trading at the same price at which you initially invested in it.
 * The YTM also assumes that you are holding on to the bond upto maturity
  * This is practically possible but in reality bonds are often sold before maturity at prices that correspond to different YTMs
   
  
The realized return is calculated using the following steps.

* Determine the time and price at which the bond is sold
* Calculate the future value of each of the coupon payments received based on the rate at which each coupon was re-invested upto the time of maturity
* Sum up the future values of the coupon payments and the sale price of the bond to get the total realized value at maturity V(Mat)
* Calculate the annualized realized return using the folowing formula
```
Return = ((V(Mat) / V(start))^ (1/T)) - 1

Where T is the number of years between the time of investment and the time of sale
```
 
## Yield Curve or Term Structure of Interest
A Plot of the bond yields of Zero Coupon bonds against their term periods is known as the Yield Curve of Term Structur of Interest. The term structure is often used by financiers and economists alike to see visually where the current short and long term yields are  since it reflects the market sentiment about future changes in interest rates.

The shape of the term structure could be
 * Upward sloping (Regarded as a normal yield curve)
 * Downward sloping (Inverted Yield Curve. Usually indicates an impending recession)
 * Flat

This is often regarded as a key guage of the economy and whether it is headed for growth or a recession.

## Duration

### What is Duration ?
Duration is a concept heavily used to analyse bonds.

* *Defined* as the "average" time you have to wait for your payments.
* *Used* to determine how sensetive the price of a bond is to changes in the yield.


### Calculation 
The Duration is calcualted as the average of the cash flow times, weighted by its contribution to the present value of the price of the bond

<code>D = w<sub>1</sub>t<sub>1</sub> + w<sub>2</sub>t<sub>2</sub> + ... + w<sub>n</sub>t<sub>n</sub></code> 

Given that Duration is the average `time` you have to wait to get the payments back, the formula for Duration should be an avarage of the time periods. Given that the payments are not all equal (payment at maturity vs payment for coupons) it needs to be a weighted average, Weighted by the amount each payment contributes to the Price (Present value of the payment at time t divided by the Price).

<code>w = Cashflow(t)/(1 + y)<sup>t</sup>/ P </code>

To calculate the Duration for a bond with Yield to Maturity y:
1. Calculate the Present value of each coupon payment and the payment at maturity and the given YTM y
1. Sum up these payment present values to get the Price P of the bond
1. Calculate the Duration Weights of each payment (calculated in Step 1) by dividing the present value of each payment by the Price (calculated in Step 2)
1. Multiply each weight by the payment period number, and sum up these values to get the Duration D


If the Yield on my Bond changes by &#916;y percent, what is the percentage change in the Price ?

To Calculate the change in Price P of a Bond if the Yield to Maturty changes from y<sub>1</sub> to y<sub>2</sub>

<code>&#916;P = - D * &#916;y / (1 + y)</code>

### Duration Matching: Risk Management
One of the applications of Duration is by Financial Institutions to control the risk of their bond portfolios.

* Banks often have Bonds in their Assets and Liabilities with different Times to Maturity, and thereby with different sensitivities to changes in interest rates.
 * eg. a hike in the interest rates would cause their Liabilities to drop by a larger percentage than their assets, leaving the banks in a net loss scenario (assets do not cover their liabilities)
* The way the banks manage this risk, is by ensuring that the durations of their overall assets, matches the duration of their liabilities.
 * This way the sensitivity of the liabilities and assets to changes in interest rates is the same. i.e. A hike in interest rates, would cause their liabilities and assets to drop by the same amount. 
* This is called *Duration Matching* and the portfolio is set to be *Immunized*


