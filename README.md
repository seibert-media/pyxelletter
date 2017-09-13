[![PyPI version](https://badge.fury.io/py/pyxelletter.svg)](https://badge.fury.io/py/pyxelletter)

# pyxelletter

## python-library for pixelletter


INSTALLATION

    pip install pyxelletter
  
  If you're confronted with problems, feel free to contact me: nnasri@seibert-media.net

## OPTIONS
  * Send letter
  * Get all letters (sended and ordered) or specific letter as PDF or JPG
  * Cancel ordered letter
  
## USAGE

### Initialize
  
  Initialize Pyxelletter by using your username(email) and password, provided by Pixelletter.
  
    from pyxelletter import Pyxelletter
    
    p = Pyxelletter(USERNAME, PASSWORD)

### Send letter
  
  Function returns the Pixelletter-ID of the sended file if successful. 
  Returns None if failed.
  
    p.send_letter(file_list, destination, duplex, color, user_transaction, test_environment)
  
  Function parameters
  
  * file_list: list of file-objects
  * destination: destination country, default: 'DE'
  * duplex: letter in duplex, else simplex, default: True
  * color: letter with color, default: False
  * user_transaction: custom transaction id, default: None
  * test_environment: enable test-mode, default: False
  
### Get all letters
  
  Function returns list of orders. 
  Returns empty list if failed.
    
    p.get_letters()
    
### Get status of a specific letter
  
  Function returns a dictionary containing information about the letter you were requesting.
    
    p.get_letter_status()

### Get specific letter (as pdf or image)
  
  Function returns letter as pdf (unicode string) or image (unicode string). 
  Returns None if failed
  
    p.get_letter_as_pdf(pixelletter_id)
    p.get_letter_as_image(pixelletter_id)
  
  Function parameters
  * pixelletter_id: Pixelletter-ID of the letter to get.

### Cancel letter
  
  Function returns true if sucessful else false
  
    p.cancel_letter(pixelletter_id)
  
  Function parameters
  * pixelletter_id: Pixelletter-ID of the letter to cancel.


  
  
  
