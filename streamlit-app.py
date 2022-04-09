import streamlit as st

# Remove whitespace from the top of the page and sidebar
st.markdown("""
        <style>
                @media only screen and (max-width: 700px) {
                    .block-container {
                        padding-top: 0rem;
                        padding-left: 1rem;
                        padding-right: 1rem;
                        width: 100vw;
                        max-width: 100vw;
                    }
                    footer {
                        width: 100vw !important;
                        max-width: 100vw !important;
                    }
                }
                .block-container {
                    padding-top: 0rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                    min-width: 70vw;
                }
                footer {
                    min-width: 70vw !important;
                }
        </style>
        """, unsafe_allow_html=True)

st.title("Long Cat")

# text field
length = st.text_input('How long?', '3')

top = r"""`                                                         ..
                                                      ....
                                                     ,**,,.,.
                                ...                 ,*******.
                                  ,,,    ...      ...,**/((/.
                                   ,,.        .    ,/(*,  ,*.
                                    ..  .,,*//(##,(%%%&%#(/
.*,,*,                             . *&&%(/((#%%@%##%%%%###*  .
(#####((((//(((((((//*,.        .,..,#&&#...*////////(#((###(/**,.
  *(#####((##(######((((//**,,..   ,/**,,/(#(////((((((((/(####(((**,
                /((####(((((/(//**,,*////#%###((((((((((########((((/*,
                   *((((((#((((((((/*((((##%%####(((((############(((((/*..
                       */((((((((((((((((###(((#######################(/(/,
                            .*//((((####(//(((((#################(((((/*
                                        **/((((##################((((/*,
                                        .*/((((((#############(((((((/*,
                                         ,/(((((((############(((((((//,.
                                          *((((##########(####((((((///*.
                                          ,((((###############((((((///*,
                                          ,/((((###########((((((((////*,
                                         ./(((((############(((((((////**
                                         *//((((############(((((((/////,
                                        .//(((((#############((((((/////,
                                        ,*//((((##############((((((((/*.
                                        **/((((((############((((((((/*,.
                                       ,**/(((((((#############((((((//*.
                                      .,*//((((((#############((((((///*,
                                     .*,*///((((((#############((((((//**
"""

mid = r"""                                     ,***///(((((##########(##(((((((//**.
                                     ,***///(((((##############(((((///**.
                                     .**///(((((#############((((((////**
                                     .,*////(((##############((((((////**.
                                     .,*////((((((#############(((((///**.
                                     ,**///(((###############((((((////**.
                                     .**//((((((#############((((((////**
                                     ,**//(((((##(###%%######((((((////**
                                    .,*///((((((((###########(((((((//**,
                                    ,**//(((((((#############((((((///**.
                                    .**//((((#############%##(((((((///*,
"""

bot = r"""                                    ,**//(((((((##%%#########(((((((//*.
                                    ,**//(((((####%##########(((((((/*.
                                    .*//((####(#%%#%%#######((((((((/*.
                                    .*///(((((####%#####%####((((((//,
                                     ,*/((((#####%############(((((//.
                                     ,*/(((###################(((////*
                                     ,*/((((##%########%%###(((((////*
                                    .,*//(#(#%%%%%%%%%######(((((//***
                                    ,**//(((###%%%%##########(((///***
                                    ***/((((####%%%%%########((((///**
                                    ***/((#(###%%%%%%#######((((((///*.
                                   .**//(((#####%%%%#######(((((((///*,
                                   .***/((((####%%%#######(((((((((//*,.,
                                   .***///((#####%%%######(((((((((//**,,. .
                                   .***///(#####%%%######((((((((((/////***,..
                                   ,,**///(######%%######((((((((((/((((((((/**,,..
                                  ,,**//((((#####%%#######(((((//////(((((((((((////**,,,,,,,,,
                                  ,**//(((######%%########((((((///*    .*/((((((((((((((((///.
                                 .,*//((((######%#########(((((((//*
                                 ,**//((###########./#######((((((/.
                                 .*//((##########(  ,##########(((/
                                  */((((##(#####*   .##########(((.
                                  ,//(((#######(     (#########((
                                   //((########,     ((########(.
                                   ,/(((######/      (########(.
                                   .//(##((###,      /(######(*
                                    *///((((##.      *((#####(
                                   .,****/((#,       ,(((((((*
                                   ,,,,**/((/        ,////////
                                  .,,,,**/((         .//***///
                                  ,,,***/((          ./*******.
                                 ..,,,,,*(           .********,
                              ,,.,,,,****            .,,*,,,,,,,
                             ,,*****%%%%             *#%/***(/**#(
                              (%%%%%#*                  *%%%%%%#(.
                                                           .,,
"""


# proceed
if st.button('Proceed'):
     st.text(" \n" + top + int(length)*mid + bot)
     st.text(" ")
     st.write("[https://manytools.org/hacker-tools/convert-images-to-ascii-art](https://manytools.org/hacker-tools/convert-images-to-ascii-art)")

