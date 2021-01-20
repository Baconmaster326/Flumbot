# Flumbot

### What is this?

This is a Discord bot written using the discord.py API, written in 100% python. 

### What does it do?

Flumbot does a variety of things, meant mainly to simulate another person in a discord call. He'll play clips, has games, and a shop and currency system.
Most of his clips used come from the community, where anyone can add clips to the bot's database. All you need is a youtube link, under a certain duration
and the bot on a Discord channel. The content in the bot is meant to come from the community, and this is the framework. I'll highlight some more of his commands below.

### Commands

- Midimania - A game where you have 30 seconds to listen to a midi, and correctly identify the song... (Uses Fluidsynth for midi to wav conversion)

- Midimaniadx - A game where you have 30 seconds to listen to a midi, and correctly identify a questionable selection of song names... (Uses Fluidsynth for midi to wav conversion)

- Geddit - Uses praw (Reddit Python API) to grab top 250 posts on all, you must match the title given, to the subreddit...

- Gedditdx - Uses praw and PIL (Python Imaging Library) to grab the 250 posts on all, and you must match the title to the picture...

- Autopilot - Uses librosa library to play a random clip from it's community library at a random time, emulating a real person who knows only how to speak in youtube videos

- And more! - many more commands found by typing 'help' in discord, or browsing the code found here

### TODO

- Flum Game (WIP) - A text based adventure, with elements of Undertale's kill or spare system
  - Weapon Generation is completely finished
  - User formatting for saving, color, naming weapons is complete
  - Dev interface mode for adding ASCII-art to game complete
  - (75%) Dialog and story components
  - (15%) Battle Mechanics
  - (40%) Flavortext and area descriptions
  - (0%) Armor System and Generation

- Shop (WIP) - Uses the currency (marcs) won from the games.
  - Roulette - spend some marcs for a chance at more, like free parking in monopoly.
  - Weapon Shop - spend some marcs on generating a weapon, instead of finding one in flum game.
  - (WIP) Streamlining the navigation of the shop, and adding more to do.
