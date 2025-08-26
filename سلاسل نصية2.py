import re

gmail= ''''Life is an adventure—chase your goals, but don’t forget to enjoy the ride! Need inspiration? Reach out:

DreamBig@gmail.com

SuccessJourney@hotmail.com

StayMotivated@yahoo.com

Sometimes, a little gamin energy (like pranking your friends with funny emails to NoReply@fake-mail.com) keeps things fun. But serious dreams need action!

Tips for Success:

Plan wisely – contact GoalSetters@gmail.com for tools.

Stay curious – email AskWhy@science-lover.com for ideas.

Never quit – spam NeverGiveUp@motivation.org (just kidding… or not!).

Remember: Every email you send (even to ImaginaryFriend@mail.com) could lead to something great. Now go rock your dreams—gamin style!

'''
group_gmail = re.findall(r'[\w\._]+@[\w\._]+', gmail)

if group_gmail:
    print(group_gmail)

else:
    print("t")




















