# Universal Quest Language
I want to make a format for storing quest data as independent files with a more easily readable format than JSON or XML.
The idea would be that each file describes a "quest event". These events link to each other through ID references which should be suficiently flexible.


## Syntax

 - "__" starts a section / denotes a piece of information or variable
 - "#" is a comment

## Vocabulary

### __ID__
The quest id - this should be unique

### __TITLE__
Quests need names/titles/headings or whatever

### __TYPE__
The type of quest template this maps to. The idea would be that this would be implementation specific for each game.
[quest, breadcrumb, conclusion, item]

### __DESCRIPTION__
Description of the contents of the file.
This is intended to give developer notes that don't get cropped like comments in the file.

### __TOOLTIP__
The quests tooltip.

### __BLURB__
The quests blurb, if a tooltip is insuficient

### __REQUIRES__
This contains a list of things that the player needs to attain.
This is implementation specific?

### __PRICE__
The price of activating this event.

### __PRICE_TEXT__
Template for formatting the price for the UI.
This is going to be implementation dependent.

### __REWARD__
Reward for completing the quest

### __NEXT_QUEST__
References for the next quest if this is a questline

### __ACTIVATES__
References to other quest events that need to be activated/set up or whatever when this is triggered.

### __TRIGGERS__
TODO: figure out whether I need triggers - it seems painfull
on_quest_created