# A simple ATM controller

The controller consists of two Class
- Class Bank
  - Hold informations: Name, Card Number, PIN, Account No, Balance 
  - Could use functions 
    - add_information(name, card_num, pin, account, balance)
      : adding data to database
    - add_account(card_num, account, balance)
      : add addtional accounts 
    - check_pin(card_num, pin)
      : checking for valid pin 
    - update_account(card_num, account, balance)
      : updating account balance after actions from controller
 
- Class Contoller:
  - Enables follwoing actions by functions
    - insert_card(card_num, pin)
      : checks pin number 
    - select_account(account)
      : selects_account
     - account_actions(card_num, account, action, amount)
       : defaut amount is 0 considering check balance action
       :  

##The controller should work with the flow
###1. Insert Card
###2. Enter Pin number
###3. Select Account
###4. View Balance, Deposit, Withdraw
