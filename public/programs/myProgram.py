from nada_dsl import *
import random

def nada_main():

    # heyy party karenge
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")

    # Define kiya maine
    secret_age1 = SecretInteger(Input(name="secret_age1", party=party1)) 
    secret_age2 = SecretInteger(Input(name="secret_age2", party=party2)) 
    secret_age3 = SecretInteger(Input(name="secret_age3", party=party3)) 

    # random stuff
    random_int1 = Integer(random.randint(1, 1000000000000000000))
    random_int2 = Integer(random.randint(1, 1000000000000000000))
    random_int3 = Integer(random.randint(1, 1000000000000000000))

    
    secret_result = (secret_age1 - Integer(17)) * random_int1 + \
                    (secret_age2 - Integer(18)) * random_int2 + \
                    (secret_age3 - Integer(19)) * random_int3

    # tata
    output1 = Output(secret_result, "secret_result", party1)
    output2 = Output(secret_result, "secret_result", party2)
    output3 = Output(secret_result, "secret_result", party3)

    return [output1, output2, output3]