*** Settings ***
Documentation       Simple example using SeleniumLibrary.


Library             SeleniumLibrary
Library             WestField

Suite Setup         UI Setup
Suite Teardown      UI Teardown

*** Variables ***
${site}             https://www.westfield.com/
${Close_Take_Over}  icon--action.js-close-modal
${Enter_Take_Over}  modal__newsletter_body

#${xp_enter_take_over}  //newsletter-modal[@id='newsletter-modal']      /html/body/div[1]/main/div[7]/div[2]/div[2]/a
${xp_Select_Store}  //main[@id='main']/section/div/div/div[2]/div/div/div[7]/div/a/div/h2
${css_Select}       \#firstName
${form_id}          firstName
${xp_form_id}       //*[@id="firstName"]


*** Test Cases ***
#Go to site
#    Go To Page      ${site}
#
#Click on an element by class
#    Click on ${Close_Take_Over} to close window
#    UI Teardown

Go into take over
#    UI Setup
    Go To Page          ${site}
    enter take over      ${Enter_Take_Over}
    click_by_xpath      ${xp_Select_Store}
    sleep  5s

