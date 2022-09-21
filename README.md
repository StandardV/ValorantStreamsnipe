# Valorant Stream Snipe
  Screenshot game name,double check with twitch to see if the account's streaming

## Probability 
  First off, let set aside the moral or ethical issue, I made this just because. Base on probability, the chances of meeting a twitch streamer in your match is really high in weekend or in holiday simply because everyone in their freetime could just start the stream and play, won't hurt that much to performance or anything that are related.
  
  In total, I've played 5 matches in the weekend and 5 matches in the weekday to rule out the difference. 
      I've met up to 4 streamers out of 5 spike rush matches in total in the weekend (count both team)
      I've only met 1 streamers out of 5 spike rush matches in total in the weekday (count the enemy team)
  Therefore, base on statistic and  what I've seen up until now, it's safe to say that it is really depend on what hours do people started streaming the most, their free time, or even the day in the week that people could just chill and play.
  
  (I've actually entered one stream and heard a streamer non-stop complain about me auto pick sova in spike rush, that match was dodged. We meet again, I autopicked again and he complain again lol XD.)
  
  ## What this script do:
  Here is an example of what part that of the screen that it take screen shots (You can look at anything or even moving meanwhile, but it's best if you look at a dark surface while doing so, about 20% better):
  
![Tesseract](https://user-images.githubusercontent.com/76143641/191545830-dcbdcd89-d731-433b-b82a-52d232c7d35c.png)

It will look through the name, using OCR to write it down, and just check on twitch if the account is there and streaming. If account's not available or not streaming it will say Unavailable, else, it'd say Online

![Screenshot (574)](https://user-images.githubusercontent.com/76143641/191546903-22b04a3e-7ce2-4da4-a668-7601199d50d4.png)]

Just to prove that it's working:
Here's Lee stream:

![Screenshot (576)](https://user-images.githubusercontent.com/76143641/191553340-3c1ce992-ce74-4ee1-9855-eb84706086f5.png)

Input:

![Tesseract](https://user-images.githubusercontent.com/76143641/191553582-356bf356-e4d8-472b-ba5e-ce56e39397b9.png)

Output:

![Screenshot (575)](https://user-images.githubusercontent.com/76143641/191553675-d5c47f99-a896-45f1-ae79-464d0e64232e.png)

  ## How to use:
  It is really simple. You just need to turn the script on, enter a match, during the buying phase, click tab to see all of the opponent usernames that are nicely packaged together and press (-) as a predetermined key or you could change it into what ever you want. Wait about 1 second, recieve the output, and continue on playing!

  ## Chances for development
  
  As you can see right now, it is just a 5 minutes script, still a lot of room for development but who knows, I might do that one day if I want to or people are interested in it.
  An example of what could be seen from the above demonstration is, if your user name is Unattractive for example, it will just look for an account with twitch user name Unattractive (If you read this, and your user name is the same as twitch name, I'd reccomend you change it :> ), check if they're online and print it out on the console. But for further development or anyone that read this post that interest, you can do it yourself
  
   - Create a function of switching texts that some specific characters can be swap around, interchange with each other or just simply delete some specific character from the output of that username
   - Or make a name collecting twitch bot, what it could do is joining twitch streamer, gather their name then put it in a large text file that can be read later for any related function, a lot of bot's already up there, this one just have a little weird little function compare to others (https://twitchinsights.net/bots)
