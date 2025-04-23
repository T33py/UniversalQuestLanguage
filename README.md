# Universal Quest Language
I want to make a format for storing quest data as independent files with a more easily/humanly readable format than JSON or XML.

The idea would be that each file describes a "quest event". These events link to each other through ID references which should be suficiently flexible.

Then the whole thing can either be parsed into a dict and saved into a propper dataformat for easy use in the game, or it can be read at launch to allow dynamic addition of quests.
Part of it is having structured and unstructured data, so I can combine set functionality for hooks into efficient template classes in engine and random data that can be stored in a dict and accessed when needed in the game logic.

## Why is it like this
I just want to make a drag n' drop folder that allows me to start writing quests in .uql files.

This should all be done with language/engine native features to avoid messing around with dependencies.

## Syntax

 - "__" starts a section / denotes a piece of information or variable.
 - "#" is a comment.

## Vocabulary
TODO: figure out what to expand??

Section headers with parsing.

Any sections not handled by this set should be interpreted by the game code that implements the quests.

### __ID__
Integer id of the quest.

### __REQUIRES__
This contains a list of things that the player needs to attain.
This is implementation specific?

### __PRICE__
List of things requirements to activate this event.

### __REWARDS__
List of rewards the player recieves for completing the quest.

### __RELATED_QUESTS__
Reference for the other quests this is related to. This is a set of ID's sepperated by newline symbols (\n).

### __ACTIVATES__
References to other quest events that need to be activated/set up or something like that when this is triggered. This is a set of ID's sepperated by newline symbols (\n).