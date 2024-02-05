import streamlit as st
import time


st.title("Gillian's pomodoro timer")
# def countdown(interval):
#     progress_bar = st.progress(0)
#     total_seconds = interval * 60
#     for i in range(total_seconds, 0, -1):
#         minutes, seconds = divmod(i, 60)
#         if minutes < 1:
#             st.text(f'You have just {seconds} seconds to go')
#         else:
#             st.text(f'You have {minutes} minutes and {seconds} seconds to go')
#         progress_bar.progress((total_seconds - i) / total_seconds)
#         time.sleep(1)
def countdown(interval):
    progress_bar = st.progress(0)
    timer_text = st.empty()  # Create a placeholder for the timer text
    total_seconds = interval * 60
    for i in range(total_seconds, 0, -1):
        minutes, seconds = divmod(i, 60)
        if minutes < 1:
            timer_text.text(f'You have just {seconds} seconds to go')
        else:
            timer_text.text(f'You have {minutes} minutes and {seconds} seconds to go')
        progress_bar.progress((total_seconds - i) / total_seconds)
        time.sleep(1)
        
def main():
    total_duration = st.number_input("Enter total duration", min_value=1, value=1, step=1)
    interval = st.number_input("Enter work interval", min_value=1, value=25, step=1)
    break_duration = st.number_input("Enter break duration", min_value=1, value=5, step=1)

    if st.button('Start Timer'):
        session_count = 0
        while session_count < total_duration:
            st.text("Time to get to work!")
            countdown(interval)
            st.text("Time for a break!")
            countdown(break_duration)
            session_count += 1
            st.text(f'Session number: {session_count}')
        st.text("Well done! You are getting better every day.")
        st.text("End of Session!")

if __name__ == "__main__":
    main()
