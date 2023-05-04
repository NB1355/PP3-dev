
import gspread
from google.oauth2.service_account import Credentials
import json
import pandas as pd
import pyinputplus as pyip


# ..........................................TEMP: tests for adding new features
from tests import test01


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('PP3-data-sets')





def get_settings():

    ## Open the file seting.json ##
    with open('setings.json') as json_file:
        data = json.load(json_file)

    ## Extract the defined options ##
    options = data['options']

    ## Use Panda DataFrame to format the output ##
    df = pd.DataFrame(options).set_index('Op')
    dfp = df.drop('id', axis=1)

    print(dfp.to_string(header=False))

    ## Options list rows to define the Max of unput range ##
    return len(options)


def f_00():

    ## Exit the program ##
    print('... execute function 0')


def f_01():
    print('... execute function 1')


def f_02():
    print('... execute function 2')


def f_03():
    print('... execute function 3')


def options_run():

    ## Executes the function corresponding to the user input ##
    try:
        op = pyip.inputInt('\n... Your option: ', min=0, max=get_settings()-1)
        match op:
            case 0:
                f_00()
            case 1:
                f_01()
            case 2:
                f_02()
            case 3:
                f_03()

    except KeyboardInterrupt:
        print('\n\nO O P S! \n... run whatever intrruption logic is!')
         
      
def check_value(sht,col,val):

  
    data = SHEET.worksheet(sht).get_all_records()

    df = pd.DataFrame(data).astype('string')

    # print(df[col].values , val)

    if val in df[col].values:
    # if str(val) in str(df[col].values):
        out='exist'
    
    else:
        out= 'not exis'
    return out


def main():

    i=1
    # test = [ 'username','name0','name003','1',1,' ','!']
    test = ['password',2,'2','12','a', 'L&kpN8wZ*E$q6%5C8y4M',' ','!']

    print(test[0], 'input check')
    
    while i < len(test):
        print(test[i],'---' , check_value('user', test[0], test[i]))

        i = i+1

    # print('\nW E L C O M E ! \n... Choose form options below to proceed\n')
    # options_run()     
    # print('\nD O N E !\n')

main()
