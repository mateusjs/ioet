[![codecov](https://codecov.io/gh/mateusjs/ioet/branch/master/graph/badge.svg?token=87JL7SZIPI)](https://codecov.io/gh/mateusjs/ioet)




# Ioet Acme Exercise

This projects consists on an simple application to solve a programming exercise.



## Requirements

To run this project make sure you have installed on your os:

```bash
 python >= 3.9
```

## Running the app

To actually run the project clone it in your desired folder

```
 https://github.com/mateusjs/ioet.git
```
Open the project, and a bash inside the root folder, then using the bash change to the app dir.

```bash
cd app
```


 **_NOTE:_**  Do not change the file **file.txt**  within **data** folder, it is the file to run the program correctly, so if you want to change the input, just edit the file.


Execute the file **main.py** file to run the application.
```bash
python main.py
```
After runit, a new file called **employees_payment.txt** will be generated on the **data** folder with the output. On your bash you can also check the output.

## Tests
The project has a coverage of 100%, to run the tests you need to be inside the **app** dir.

Then run the following command.

```bash
python -m unittest discover test/
```
## Exercise

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

| Monday - Friday 	| Payment per hour 	|   	| Saturday and Sunday 	| Payment per hour	|
|:---------------:	|:-------:	|:-:	|:-------------------:	|:-------:	|
|  00:01 - 09:00  	|  25 USD 	|   	|    00:01 - 09:00    	|  30 USD 	|
|  09:01 - 18:00  	|  15 USD 	|   	|    09:01 - 18:00    	|  20 USD 	|
|  18:01 - 00:00  	|  20 USD 	|   	|    18:01 - 00:00    	|  25 USD 	|


The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:
|     |             |              |                |               |             |               |            |
|:---:|:-----------:|:------------:|:--------------:|:-------------:|:-----------:|:-------------:|:----------:|
| Day | MO: Monday  | TU: Tuesday  | WE: Wednesday  | TH: Thursday  | FR: Friday  | SA: Saturday  | SU: Sunday |

**Input**: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

**Output**: indicate how much the employee has to be paid

For example:

**Case 1**
**Input**: RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
**Output**: The amount to pay RENE is: 215 USD

**Case 2**
**Input**: MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
**Output**: The amount to pay ASTRID is: 85 USD

## Solution
For the solution first i tried to see what could be done with the data and requirements collected, so then i could create a simple structure that would be easy to understand and also to code.

Using a c4 model, i was able to create the mvp structure of the project

![](https://i.gyazo.com/6b377208136942c28426981542ed9659.png)

With that in mind became easy code, so i created a component to process the file (read and write), after that i start to developing the next steps, creating some objects to handle the input processed.

While coding was possible notice the lack of some helper functions, so i created it.

After finishing to code, and test, i start to improve the app with some actions and documentation.
