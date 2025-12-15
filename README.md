DESCRIPTION

This is a very simple web automation project written in Python using the Selenium WebDriver. The file contains a basic implementation of a GUI using Tkinter for those who are not familiar with a CLI.
The program is specifically designed for the Instagram website and uses many direct XPath and CSS selectors that are often dynamic and frequently changing. The version uploaded here runs well on my machine, but that is no guarantee it will work elsewhere, as the website may render differently based on things such as region, time, internet connection, or even account.

DISCLAIMER

I am a young programmer and guarantee that many of the practices I have used in this implementation are not the best. Please feel free to suggest and critique, as I am still learning and would love to improve. I am not sure if doing something like this violates the terms and conditions provided by Meta, but it is a fun project to play around with. I would recommend creating a separate account for testing and experimenting rather than using any personal accounts to avoid potential issues.
The design of the program is very brittle and will most likely need to be adapted for each machine and account. My specific program includes a custom click sequence to get around a “reduce the amount of times you need to log in” screen. Others may need to handle things such as 2FA or other types of notifications before the raw post stream is accessible. If this is your case, it should be simple to use the same method of finding elements by their XPath or CSS selectors and then performing the necessary operations with the WebDriver. Play around with it and see if you can get it to work!

INSTRUCTIONS

1: After downloading the bot.py file, you can open it in a virtual environment using whatever IDE you prefer (e.g., PyCharm or VS Code).

2: Ensure you have the dependencies installed, such as the Selenium package and Tkinter.

- Selenium 4.6+ will automatically fetch a driver for your specified browser, so none needs to be manually installed. However, if you encounter issues, you may need to install a driver such as ChromeDriver and provide the specific path for Selenium to locate it.

- The program currently uses ChromeDriver and Chromium, but Firefox is also available.

3: Run!

4: The GUI should appear on your screen—follow the steps and watch the magic happen as the machine logs you into Instagram and proceeds to comment on the first post as many times as you specified.

NOTES

Any information you enter into the GUI or your version of the program is not sent to me or stored in any way. The program runs locally and only sends to Instagram’s servers what you tell it to! Make sure to be safe with your accounts and not publish any sensitive or private information such as passwords or usernames.
