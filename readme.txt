
Welcome to the Morse Code Translator

About
This is a script that translates Morse Code to text and vise versa. It is programmed using Python and utilizes the Tkinter package for GUI.

The script is run from 'main.py'. Relevant dictionaries are located in 'data.py'.


How It Works
1) Select the mode in which you would like to translate via the dropdown list (Default: Text to Morse Code).

2) Enter text or code into the Input Box.
    Valid Characters:
        Text to Morse Code
            English Letters: A-Z, a-z (Morse Code is not case sensitive, but both are accepted as inputs)
            Numbers: 0-9
            Symbols: .  ,  ?  !  '  "  :  ;  (  )  +  -  =  /  _  @  $  &
        Morse Code to Text
            Dits/dahs are represented by periods(.)/dashes(-) respectively.
            Separate code blocks with a single space(" ").

3) Click the submit button. The results will populate in the Translation Box below.
    ' / ' represents word breaks when translating text to Morse Code.
    Morse Code is not case sensitive, by default output text is in all caps.
    If desired, the output text can be toggled between uppercase and lowercase using the buttons below the Translation Box.
    When submitting an additional translation, the Translation Box will clear before generating the new translation.