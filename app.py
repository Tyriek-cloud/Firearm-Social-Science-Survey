# No other libraries are needed.
import streamlit as st

def main():
    try:
        st.title('Firearm Social Science Survey')
        st.write('Instructions: Type in all answers carefully. Do not hit the space bar before typing answers. Answers are not case sensitive.')
        
# Creating a list of tuples. This will help me to only generate the next question after the previous question was answered.
        questions = [
            ("How many firearms do you own? Do not put commas or decimal points.", lambda x: x.isdigit() and int(x) >= 0, "You own {} firearm/firearms right now."),
            ("Would you use your firearm in self-defense (yes or no)?", lambda x: x.lower() in ('yes', 'no'), "You answered {}."),
            ("What is your gender identification? Male, Female, Nonbinary, Other?", lambda x: x.lower() in ('male', 'female', 'nonbinary', 'other'), "You answered {}."),
            ("Please select the first reason you can think of for why you decided to purchase a firearm: defense, constitution, or sport.", lambda x: x.lower() in ('defense', 'constitution', 'sport'), "You chose {}."),
            ("Which one of the selected options (numbers 1, 2, and 3) for the previous question is most important to you?", lambda x: x.isdigit() and int(x) in (1, 2, 3), "You answered {}."),
            ("How would you rate the amount of police presence in your neighborhood on a scale of 1-10, 10 being high?", lambda x: x.isdigit() and int(x) in range(1, 11), "Your selection is {}."),
            ("Do you feel threatened by racially motivated hate groups in the U.S. (yes or no)?", lambda x: x.lower() in ('yes', 'no'), "You chose {}."),
            ("Do you feel scared of the police in the U.S. (yes or no)?", lambda x: x.lower() in ('yes', 'no'), "You chose {}."),
            ("Have you ever been victimized by police or racially motivated offenders in the U.S. (yes or no)?", lambda x: x.lower() in ('yes', 'no'), "You chose {}.")
        ]
# Here is the actual while loop. It will iterate through user inputs. Basically, if a correct input is selected, than the user can continue.
        for question, validation, response in questions:
            st.write('')
            user_input = None
            while user_input is None or not validation(user_input):
                user_input = st.text_input(question)
                if user_input is None or not validation(user_input):
                    st.write('Invalid input. Try again.')

            st.write(response.format(user_input))

        st.write('')
        st.write('You have completed all of the questions. Thank you for taking this survey.')
    
    except:
        pass  # This suppresses all the exceptions silently. This is important because Streamlit shows errors by displaying my logs. I don't want users seeing that.

if __name__ == "__main__":
    main()
