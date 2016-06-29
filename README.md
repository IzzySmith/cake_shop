# cake shop

#### Pages

- the index (link to Surfly session) fake links to themed cakes and designs (wedding/ birthday/ anniversary/ english high tea, an order button (to the form), ask for assistance (surfly)) 
  - zoopim will be added here
- landing page (start session) -> it is a popup with session id and text
- form (during session) payment details
- thankyou for ordering page 
- -> then, at the end of sessionpopup with survey inside 
- reciept
- login page?

#### Characters:

- the confused customer *Mrs Rose Frosting*
- the agent *Miss Cherry Flour*

#### Shop Name and theme

Colours: 
  - light blue 

Name: 


Slogan: *baking dreams come true*

parody the disney logo in cake?! (castle as a cake)

Initially the developers are setting up the index page for their cake shop. They are a specialist cake shop and make the cake for the customer -> they make the fantasy cakes of their customers come true. Comunication is very important, and so they want co-browsing funcionality to show the different options, guide, and to offer greater support to clients. They decide to integrate Surfly: 

*add inbound/ outbound information?*

#### The story flow 

First step:
 - create an index page (shop front) without Surfly functionality **first commit**
   - then add the basic widget with no adaptations **second commit**
   
It doesnt sit as well on the website as they wanted so they experiment with the colors and options
They then decide to remove the button entirley and have people use a cake instead
 
Second step:
 - change color of chatbox/ drawing mode/ disable a few things **third commit - comments detailing exact changes** 
 - then create own button (a cake?) **fourth commit**

They decide that the red banner is unsuitable, so remove it and then create a landing page, with a popup. They say that some of their clients still ask for help over the phone, so an agent can direct them to a Surfly session and then join them with the session id from the 'start' panel in the admin page. 

Third step 
 - remove the red banner **fith commit**
 - create landing page with own popup window (cake and name of cake shop, give a session id - if on the phone to the agent please pass this over to them now, otherwise please wait for an agent to join your session - automatically close popup when follower joins?) **sixth commit**

Then we decide, we are happy with the integration, and want to test it, so enter Mrs flour and Mrs Frosting. Mrs Frosting starts a session, and then Mrs Flour joins. During the session, the developers notice a few things they want to change when Mrs Frosting placed her order. 

Fourth step (ordering a cake in the session)
 - show a form -> the agent can see payment details - enable field masking **seventh commit** 
 - disable the buy button **eigth commit**

Then they want feedback from the session, so they add a popup window, and Mrs Frosting fills this in, 
explain the changes to the widget. 

Fith step 
 - show a popup and form at the end for feedback (and then show the results on another page) **ninth commit**

Finally, we retrieve Mrs Frostings order after the popup has closed. 
 
Sixth step
 - we want to show a reciept at the end -> use session continuation **tenth commit**

#### Advanced options

The developers are happy with the flow and wantto make some small adjustments - they decide to log the sales made by Mrs FLour. (maybe they work on commission). 

Seventh step
- logging sales made by the agent (surfly.log()) -> write as csv to an excel spreadsheet **eleventh commit**

Realise that they need to restrict access to certain pages

Eigth step
 - add a blacklist for a seperate business (baking shop with ingredients) - maybe the agents are only working for the cake shop and don't understand the baking side so well **twelfth commit**

Then they have repeat customers/ loyal customers that they want to give a more personal experience to -> these customers have login details and pass names and email data to the agent(s). 

Ninth step 
 - add metadata **thirteenth commit**

At this point they decide that the functionality is not needed, and strip everything down to purely co-browsing

Final step

- We realsied that we don't need all the functionality e.g document sharing, so we will instead integrate zoopim, and just have the co-browsing functionality. Also allows us to have own control option/ exit button. 

 - totally invisable 
 - remove UI and put own chat box and buttons **fourteenth commit** 
 - show stealth mode (don't even need a button) remove everything. (not a commit, just demonstration)
 - Create exit button **fifteenth commit**
 - Integrate Zoopim **sixteenth commit**
