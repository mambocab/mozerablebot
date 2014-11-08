You were looking for a bot, and then you found a bot. A love letter to Morrissey.

## Use

This repo has the stuff you need to run the bot on Red Hat's OpenShift infrastructure. Most of the files in this repo are from `rhc` default project setup. I used a gear with a Python 3.3 and Cron cartridge.

The meat of the bot itself is in `tweet.py`. This assembles and tweets the tweet each time it's called. This assumes you have some kind of infrastructure, like a `cron` job, to regularly call the script.

I may be constructing my Wordnik API calls incorrectly, because I sometimes see plural words leaking through. Until I figure it out, I'm using the `inflect` library to convert plural nouns to singular ones. I had to manually install `inflect` on my OpenShift instance by `ssh`ing in and running `pip`; your mileage may vary there.

The `cron` script that runs the bot is in `.openshift/cron/minutely/tweet.sh`. It's called every minute by virtue of being in `.openshift/cron/minutely`. This is what determines how often the tweeting script is called. It should be called about 5 times per day, as per the modulo in the `if` condition. I may change how this frequency is calculated in the future, but it's fine for now, right? Right.

## Acknowledgments

Uses the [badwords list](https://github.com/dariusk/wordfilter/blob/master/lib/badwords.json) from [Darius Kazemi's `wordfilter` library](https://github.com/dariusk/wordfilter/). I welcome any reports of racist, sexist, ablist, transphobic, etc. language as GitHub issues or over Twitter.

Profile image from (The Guardian)[http://www.theguardian.com/music/2010/sep/03/morrissey-simon-armitage-interview].
