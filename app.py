import streamlit as st

def main():
    try:
        st.title('Social Science Survey')
        st.write('Instructions: Type in all answers carefully. Do not hit the space bar before typing answers. Answers are not case sensitive.')

        st.write('')
        myFirearms = None
        while myFirearms is None:
            input_value = st.text_input('How many firearms do you own? Do not put commas or decimal points.')
            try:
                myFirearms = int(input_value)
            except ValueError:
                st.write(f"{input_value} is not a number, please enter a number only")
                continue
        if myFirearms > 0:
            st.write('You own ' + str(int(myFirearms)) + ' firearm/firearms right now.')

        st.write('')
        while True:
            Use = st.radio('Would you use your firearm in self-defense?', ('Yes', 'No'), key="use_radio")
            if Use.lower() not in ('yes', 'no'):
                st.write('Not yes or no. Try again.')
            else:
                break
        if Use.lower() == 'yes':
            st.write('You answered yes.')
        elif Use.lower() == 'no':
            st.write('You answered no.')

        st.write('')
        while True:
            Gender = st.radio('What is your gender identification? Male, Female, Nonbinary, Other?', ('Male', 'Female', 'Nonbinary', 'Other'), key="gender_radio")
            if Gender.lower() not in ('male', 'female', 'nonbinary', 'other'):
                st.write('Not one of the listed answer choices. Try again.')
            else:
                break
        if Gender.lower() == 'male':
            st.write('You answered Male.')
        elif Gender.lower() == 'female':
            st.write('You answered Female.')
        elif Gender.lower() == 'nonbinary':
            st.write('You answered Non-Binary.')
        elif Gender.lower() == 'other':
            st.write('You answered Other.')

        st.write('')
        while True:
            Reason = st.radio('Please select the first reason you can think of for why you decided to purchase a firearm:', ('Defense', 'Constitution', 'Sport'), key="reason_radio")
            if Reason.lower() not in ('defense', 'constitution', 'sport'):
                st.write('Incorrect answer choice. Try again.')
            else:
                break
        if Reason.lower() == 'defense':
            st.write('You chose Defense.')
        elif Reason.lower() == 'constitution':
            st.write('You chose Constitution.')
        elif Reason.lower() == 'sport':
            st.write('You chose Sport.')

        st.write('')
        while True:
            myOption = st.radio('Which one of the selected options (numbers 1, 2, and 3) for the previous question is most important to you?', ('1', '2', '3'), key="option_radio")
            if myOption.lower() not in ('1', '2', '3'):
                st.write("Not an appropriate choice.")
            else:
                break
        if myOption == '1':
            st.write('You answered Defense.')
        elif myOption == '2':
            st.write('You answered 2nd_Amendment_Right.')
        elif myOption == '3':
            st.write('You answered Sport.')

        st.write('')
        while True:
            Presence = st.radio('How would you rate the amount of police presence in your neighborhood on a scale of 1-10, 10 being high?', tuple(str(i) for i in range(1, 11)), key="presence_radio")
            if Presence.lower() not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
                st.write('ONLY select a value from 1 to 10.')
            else:
                break 
        st.write('Your selection is ' + str(int(Presence)))

        st.write('')
        while True:
            Threatened = st.radio('Do you feel threatened by racially motivated hate groups in the U.S.?', ('Yes', 'No'), key="threatened_radio")
            if Threatened.lower() not in ('yes', 'no'):
                st.write('Not yes or no. Try again.')
            else:
                break
        if Threatened.lower() == 'yes':
            st.write('You chose yes.')
        elif Threatened.lower() == 'no':
            st.write('You chose no.')

        st.write('')
        while True:
            Scared = st.radio('Do you feel scared of the police in the U.S.?', ('Yes', 'No'), key="scared_radio")
            if Scared.lower() not in ('yes', 'no'):
                st.write('Not yes or no. Try again.')
            else:
                break
        if Scared.lower() == 'yes':
            st.write('You chose Yes.')
        elif Scared.lower() == 'no':
            st.write('You chose No.')

        st.write('')
        while True:
            Victimized = st.radio('Have you ever been victimized by police or racially motivated offenders in the U.S.?', ('Yes', 'No'), key="victimized_radio")
            if Victimized.lower() not in ('yes', 'no'):
                st.write('Not yes or no. Try again.')
            else:
                break
        if Victimized.lower() == 'yes':
            st.write('You chose yes.')
        elif Victimized.lower() == 'no':
            st.write('You chose no.')

        st.write('')
        st.write('You have completed all of the questions. Thank you for taking this survey.')
    
    except:
        pass  # Suppress all exceptions silently

if __name__ == "__main__":
    main()
