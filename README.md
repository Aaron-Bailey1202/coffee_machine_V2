# Coffee Machine Simulator

This is a Python program that simulates the functionality of a coffee machine. Users can select from a menu of drinks, insert coins to pay for their order, and receive their drink along with any change due.

## Features

- **Drink Selection**: Choose from a variety of drinks such as latte, espresso, and cappuccino.
- **Resource Management**: The program manages resources like water, milk, and coffee beans, ensuring there are enough ingredients to fulfill orders.
- **Payment Handling**: Users can insert coins of various denominations to pay for their orders, with the program calculating change if necessary.
- **Reporting**: Generate reports to view the current status of the coffee machine, including remaining resources and profit earned.

## Usage

1. **Running the Program**: Execute the `coffee_machine.py` file
   ```
   python coffee_machine.py
   ```
2. **Ordering Drinks**: Follow the prompts to select a drink from the available menu options.
3. **Payment**: Insert the required coins when prompted to pay for the selected drink.
4. **Receipt and Change**: Receive the ordered drink and any change due.

## Dependencies

- The program requires Python 3 to run.
- There are no external dependencies beyond the Python standard library.

## File Structure

- `coffee_machine.py`: Main Python script containing the coffee machine simulation logic.
- `menu.py`: Defines the menu of available drinks and their ingredients.
- `coffee_maker.py`: Contains the `CoffeeMaker` class responsible for managing resources and making drinks.
- `money_machine.py`: Defines the `MoneyMachine` class for handling payments and change.


## Acknowledgements

- The project was inspired by various tutorials and resources on Python programming and object-oriented design.
