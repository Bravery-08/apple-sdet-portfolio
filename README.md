# apple-sdet-portfolio

## How to run

`pytest tests/ -v`

-   For HTML reporting:

` pytest tests/ -v --html=report.html --self-contained-html`

## Tests covered (10)

### Tests for https://www.automationexercise.com

1. Cart:

-   Whether products show in cart after being added to cart
-   Whether products get removed from cart successfully
-   Whether product quantity increases suitably

2. Login:

-   Whether error message is shown when incorrect credentials are used for login

3. Search:

-   Whether products are shown and not shown when respective search strings are entered

4. Signup:

-   Whether clicking on an option from a dropdown selects it
-   Whether email with no "@" is flagged suitably

### Tests for https://the-internet.herokuapp.com/

1. Iframe:

-   Whether switching to and from an iframe works

2. Javascript:

-   Whether JS alerts, confirm dialogs and prompts can be suitably handled
