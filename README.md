# Introspect
> A productivity monitoring app using Boostnote

### How to run :
- Create a virtual environment (preferably).
- Clone the repository. ( `git clone https://github.com/mohdomama/introspect` )
- Run `cd introspect`
- Install the requirements. (`pip install -r requirements.txt`)
- Run the script. (`python3 main.py`)
- If you are running it for the first time, it wil ask for the name and path of your boostnote checklist. The name can be anything.
    - It can be found at /home/< username >/Boostnote/notes/ < filename >
    - The file name is hashed. To get the required file name:
        * open your file in boostnote
        * press the small `i` on top right
        * In the 'Note Link', there wil be something like : [Heading] (1806ee3bee76f5c3e2d3-4c888182c7e9b7ac9932)
        * The second value in the link is your file name. In this case : '4c888182c7e9b7ac9932'
- The name and path inpput will look somethig like : < some_name > /home/< username >/Boostnote/notes/4c888182c7e9b7ac9932.cson
- Enjoy!

