import scipy.stats
import streamlit as st
import time

st.header('Jogando uma moeda')

chart = st.line_chart([0.5])

def toss_coin(n): # função que emula o lançamento de uma moeda

    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)
start_button = st.button('Executar')

if start_button:
    st.write(f'Executando o experimento de {number_of_trials} tentativas.')
Não se preocupe se não entender completamente a função toss_coin(). É absolutamente normal – você não precisa entender todas as funções que usar. Por exemplo, quando você chama a função read_csv() de Pandas, você não precisa saber como ela funciona, mas consegue usá-la. O mesmo princípio funciona aqui.

Agora vamos fazer a chamada de toss_coin quando start_button é clicado (obtém o valor True).

import scipy.stats
import streamlit as st
import time

st.header('Jogando uma moeda')

chart = st.line_chart([0.5])

def toss_coin(n):

    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)
start_button = st.button('Executar')

if start_button:
    st.write(f'Executando o experimento de {number_of_trials} tentativas.')
    mean = toss_coin(number_of_trials)
