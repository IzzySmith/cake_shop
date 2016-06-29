# cake shop


#### Characters:

- the confused customer *Mrs Rose Frosting*
- the agent *Miss Cherry Flour*

#### Shop Name and theme

*we bake fantasy into reality*
parady the disney logo in cake?! (castle as a cake)

Initially the developers are setting up the index page for their cake shop. They are a specialist cake shop and make the cake for the customer -> they make the fantasy cakes of their customers come true. Comunication is very important, and so they want co-browsing funcionality to show the different options, guide, and to offer greater support to clients.

First step:
 - create an index page (shop front) without Surfly functionality
   - then add the basic widget with no adaptations
 
Second step:
 - change color of chatbox/ drawing mode/ disable a few things 
 - then create own button (a cake?)

Third step 
 - remove the red banner - create landing page with own popup window (cake and name of cake shop, give a session id - if on the phone to the agent please pass this over to them now, otherwise please wait for an agent to join your session - automatically close popup when follower joins?)

Fourth step (ordering a cake in the session)
 - show a form -> the agent can see payment details - enable field masking 
 - disable the buy button

Fith step 
 - show a popup and form at the end for feedback (and then show the results on another page)
 
Sixth step
 - we want to show a reciept at the end -> use session continuation

#### Advanced options

Seventh step
- logging sales made by the agent (surfly.log()) -> write as csv to an excel spreadsheet 

Eigth step
 - add a blacklist for a seperate business (baking shop with ingredients) - maybe the agents are only working for the cake shop and don't understand the baking side so well

Ninth step 
 - add metadata 

Final step

We realsied that we don't need all the functionality e.g document sharing, so we will instead integrate zoopim, and just have the co-browsing functionality.  Also allows us to have own control option/ exit button.

 - totally invisable 
 - remove UI and put own chat box and buttons 
 - show stealth mode (don't even need a button) remove everything. 
