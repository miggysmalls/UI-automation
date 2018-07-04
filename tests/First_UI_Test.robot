*** Settings ***
Documentation       Simple example using SeleniumLibrary.


Library             SeleniumLibrary
Library             WestField

Suite Setup         UI Setup
Suite Teardown      UI Teardown

*** Variables ***
${site}                     https://www.westfield.com/
${Close_Take_Over}          icon--action.js-close-modal
${Enter_Take_Over}          modal__newsletter_body
${xp_Select_Store}          //main[@id='main']/section/div/div/div[2]/div/div/div[7]/div/a/div/h2
${css_Select}               \#firstName
${form_id}                  firstName
${Fisrt_Name}               Westfield
${Email}                    westfield-robot3@dispostable.com
${xp_form_First_Name}       //*[@id="firstName"]
${xp_form_Email}            //*[@id="email"]
${Subscribe_Class}                button button--primary u-s-m-none
${Subscribe_XPath}                /html/body/div[1]/main/section/div[2]/div[1]/form/div/div[2]/div/div/div/button

${Edit}                 /html/body/div[1]/main/section/div[2]/div[2]/div[2]/div/div/form/div/div/div/div/div/button

*** Test Cases ***
Go into take over
#    UI Setup
    Go To Page              ${site}
    enter take over         ${Enter_Take_Over}
    click_by_xpath          ${xp_Select_Store}
    sleep  5s
    Enter ${Fisrt_Name} into ${xp_form_First_Name}
    Enter ${Email} into ${xp_form_Email}
    sleep  5s
#    Enter Take Over         ${Subscribe}
    Click By XPath          ${Subscribe_XPath}
    sleep  5s